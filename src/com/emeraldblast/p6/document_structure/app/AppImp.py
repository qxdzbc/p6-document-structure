from typing import Optional, Union

import zmq

from com.emeraldblast.p6.document_structure.app.App import App
from com.emeraldblast.p6.document_structure.app.errors.AppErrors import AppErrors
from com.emeraldblast.p6.document_structure.app.workbook_container.WorkbookContainer import WorkbookContainer
from com.emeraldblast.p6.document_structure.app.workbook_container.WorkbookContainerImp import WorkbookContainerImp
from com.emeraldblast.p6.document_structure.communication.SocketProvider import SocketProvider
from com.emeraldblast.p6.document_structure.communication.SocketProviderImp import SocketProviderImp
from com.emeraldblast.p6.document_structure.communication.event.P6Events import P6Events
from com.emeraldblast.p6.document_structure.communication.event_server.EventServer import EventServer
from com.emeraldblast.p6.document_structure.communication.event_server.EventServerImp import EventServerImp
from com.emeraldblast.p6.document_structure.communication.event_server.reactors.EventServerReactors import \
    EventServerReactors
from com.emeraldblast.p6.document_structure.communication.internal_reactor.InternalNotifierProvider import \
    InternalNotifierProvider
from com.emeraldblast.p6.document_structure.communication.internal_reactor.eventData.AppEventData import EventData
from com.emeraldblast.p6.document_structure.communication.reactor.EventReactorContainer import EventReactorContainer
from com.emeraldblast.p6.document_structure.communication.reactor.EventReactorContainers import EventReactorContainers
from com.emeraldblast.p6.document_structure.file.loader.P6FileLoader import P6FileLoader
from com.emeraldblast.p6.document_structure.file.loader.P6FileLoaders import P6FileLoaders
from com.emeraldblast.p6.document_structure.file.saver.P6FileSaver import P6FileSaver
from com.emeraldblast.p6.document_structure.file.saver.P6FileSavers import P6FileSavers
from com.emeraldblast.p6.document_structure.util.Util import makeGetter
from com.emeraldblast.p6.document_structure.util.report.error.ErrorReport import ErrorReport
from com.emeraldblast.p6.document_structure.util.result.Err import Err
from com.emeraldblast.p6.document_structure.util.result.Ok import Ok
from com.emeraldblast.p6.document_structure.util.result.Result import Result
from com.emeraldblast.p6.document_structure.util.result.Results import Results
from com.emeraldblast.p6.document_structure.workbook.WorkBook import Workbook
from com.emeraldblast.p6.document_structure.workbook.WorkbookImp import WorkbookImp
from com.emeraldblast.p6.document_structure.workbook.WorkbookWrapper import WorkbookWrapper
from com.emeraldblast.p6.document_structure.workbook.key.WorkbookKey import WorkbookKey
from com.emeraldblast.p6.document_structure.worksheet.Worksheet import Worksheet


class AppImp(App):
    """
    Standard implementation of App interface
    """

    def __init__(self,
                 workbookContainer: Optional[WorkbookContainer] = None,
                 loader: Optional[P6FileLoader] = None,
                 saver: Optional[P6FileSaver] = None,
                 socketProvider: SocketProvider | None = None,
                 eventReactorContainer: EventReactorContainer[EventData] | None = None,
                 ):
        if workbookContainer is None:
            workbookContainer = WorkbookContainerImp()

        self.__wbCont: WorkbookContainer = workbookContainer
        # x: set default active workbook to the first workbook if possible
        if self.__wbCont.isNotEmpty():
            self.__activeWorkbook: Optional[Workbook] = self.__wbCont.getWorkbookByIndex(0)
        else:
            self.__activeWorkbook: Optional[Workbook] = None

        if loader is None:
            loader = P6FileLoaders.proto()
        if saver is None:
            saver = P6FileSavers.proto()
        self.__wbLoader: P6FileLoader = loader
        self.__wbSaver: P6FileSaver = saver
        self.__newBookIndex: int = 0

        if socketProvider is None:
            socketProvider = SocketProviderImp()
        self.__socketProvider: SocketProvider = socketProvider
        if eventReactorContainer is None:
            eventReactorContainer = EventReactorContainers.mutable()
        self.__reactorContainer: EventReactorContainer[EventData] = eventReactorContainer
        self.__reactorProvider = InternalNotifierProvider(self._getSocketProvider)
        self.__zcontext = zmq.Context.instance()

        self.__initNotifiers()
        self._eventServer = EventServerImp(isDaemon = True)
        self._eventServerReactors = EventServerReactors(
            workbookGetter = self.getBareWorkbookRs,
            appGetter = makeGetter(self)
        )
        self.__initEventServerReactors()

    @property
    def zContext(self):
        return self.__zcontext

    @property
    def eventServer(self) -> EventServer:
        return self._eventServer

    def __initEventServerReactors(self):
        evSv = self._eventServer
        er = self._eventServerReactors

        reactorForWb = {
            P6Events.Workbook.DeleteWorksheet.event: er.deleteWorksheetReactor(),
            P6Events.Workbook.CreateNewWorksheet.event: er.createNewWorksheetReactor(),
        }
        reactorForWs = {
            P6Events.Worksheet.Rename.event: er.renameWorksheet(),
            P6Events.Worksheet.DeleteCell.event: er.deleteCellReactor(),
            P6Events.Worksheet.DeleteMulti.event: er.deleteMultiReactor(),
        }

        reactorForCell = {
            P6Events.Cell.Update.event: er.cellUpdateValueReactor(),
            P6Events.Cell.MultiUpdate.event: er.cellMultiUpdateReactor(),
        }

        reactorForApp= {
            P6Events.App.SetActiveWorksheet.event: er.setActiveWorksheetReactor(),
        }

        d = {
            **reactorForWb,
            **reactorForWs,
            **reactorForCell,
            **reactorForApp,
        }

        for (k,v) in d.items():
            evSv.addReactor(k,v)


    def __initNotifiers(self):
        """create internal reactors that will react to events from the app, workbooks, worksheets, cells, etc """
        container = self.__reactorContainer
        provider = self.__reactorProvider

        for event in P6Events.Cell.allEvents():
            container.addReactor(event, provider.cellNotifier())
        for event in P6Events.Workbook.allEvents():
            container.addReactor(event, provider.workbookNotifier())
        for event in P6Events.Worksheet.allEvents():
            container.addReactor(event, provider.worksheetNotifier())
        for event in P6Events.App.allEvents():
            container.addReactor(event,provider.appNotifier())

    @property
    def eventReactorContainer(self) -> EventReactorContainer:
        return self.__reactorContainer

    ### >> App << ###

    def _getSocketProvider(self) -> SocketProvider | None:
        return self.__socketProvider

    @property
    def socketProvider(self) -> SocketProvider | None:
        return self.__socketProvider

    @socketProvider.setter
    def socketProvider(self, socketProvider):
        self.__socketProvider = socketProvider

    @property
    def _fileSaver(self) -> P6FileSaver:
        return self.__wbSaver

    @property
    def _fileLoader(self) -> P6FileLoader:
        return self.__wbLoader

    def hasNoWorkbook(self) -> bool:
        return self.wbContainer.isEmpty()

    @property
    def activeWorkbook(self) -> Optional[Workbook]:
        if self.__activeWorkbook is None:
            if self.hasNoWorkbook():
                return None
            else:
                self.__activeWorkbook = self.wbContainer.getWorkbookByIndex(0)

        rt = self._makeEventWb(self.__activeWorkbook)
        return rt

    def setActiveWorkbook(self, indexOrNameOrKey: Union[int, str, WorkbookKey]):
        setRs = self.setActiveWorkbookRs(indexOrNameOrKey)
        return Results.extractOrRaise(setRs)

    def setActiveWorkbookRs(self, indexOrNameOrKey: Union[int, str, WorkbookKey]) -> Result[Workbook, ErrorReport]:
        wb = self.getWorkbookOrNone(indexOrNameOrKey)
        if wb is not None:
            if isinstance(wb, WorkbookWrapper):
                self.__activeWorkbook = wb.innerWorkbook
            else:
                self.__activeWorkbook = wb
            return Ok(self.__activeWorkbook)
        else:
            return Err(
                ErrorReport(
                    header = AppErrors.WorkbookNotExist.header,
                    data = AppErrors.WorkbookNotExist.Data(indexOrNameOrKey)
                )
            )

    @property
    def wbContainer(self) -> WorkbookContainer:
        return self.__wbCont

    @property
    def activeSheet(self) -> Optional[Worksheet]:
        if self.activeWorkbook is not None:
            return self.activeWorkbook.activeWorksheet
        else:
            return None

    def createDefaultNewWorkbookRs(self, name: str | None = None) -> Result[Workbook, ErrorReport]:
        newWbRs: Result[Workbook, ErrorReport] = self.createNewWorkbookRs(name)
        if newWbRs.isOk():
            wb = newWbRs.value
            wb.createNewWorksheetRs()
        return newWbRs

    def createNewWorkbook(self, name: Optional[str] = None) -> Workbook:
        createRs: Result[Workbook, ErrorReport] = self.createNewWorkbookRs(name)
        return Results.extractOrRaise(createRs)

    def createNewWorkbookRs(self, name: Optional[str] = None) -> Result[Workbook, ErrorReport]:
        if name is None:
            # x: create default name for new workbook
            name = "Workbook{}".format(self.__newBookIndex)
            while self.hasWorkbook(name):
                self.__newBookIndex += 1
                name = "Workbook{}".format(self.__newBookIndex)

        if not self.hasWorkbook(name):
            wb = WorkbookImp(name)
            eventNewWb = self._makeEventWb(wb)
            self.wbContainer.addWorkbook(wb)
            return Ok(eventNewWb)
        else:
            return Err(
                ErrorReport(
                    header = AppErrors.WorkbookAlreadyExist.header,
                    data = AppErrors.WorkbookAlreadyExist.Data(name)
                )
            )
