from pathlib import Path
from typing import Union, Optional

from com.qxdzbc.p6.document_structure.util.CommonError import CommonErrors
from com.qxdzbc.p6.document_structure.util.report.error.ErrorReport import ErrorReport
from com.qxdzbc.p6.document_structure.util.result.Err import Err
from com.qxdzbc.p6.document_structure.util.result.Ok import Ok
from com.qxdzbc.p6.document_structure.util.result.Result import Result
from com.qxdzbc.p6.document_structure.util.result.Results import Results
from com.qxdzbc.p6.document_structure.workbook.WorkBook import Workbook
from com.qxdzbc.p6.document_structure.workbook.WorkbookErrors import WorkbookErrors
from com.qxdzbc.p6.document_structure.workbook.key.WorkbookKey import WorkbookKey
from com.qxdzbc.p6.document_structure.workbook.key.WorkbookKeyImp import WorkbookKeyImp
from com.qxdzbc.p6.document_structure.workbook.key.WorkbookKeys import WorkbookKeys
from com.qxdzbc.p6.document_structure.worksheet.Worksheet import Worksheet
from com.qxdzbc.p6.new_architecture.common.RpcUtils import RpcUtils
from com.qxdzbc.p6.new_architecture.di.RpcServiceContainer import RpcServiceContainer
from com.qxdzbc.p6.new_architecture.rpc.RpcErrors import RpcErrors
from com.qxdzbc.p6.new_architecture.rpc.RpcValues import RpcValues
from com.qxdzbc.p6.new_architecture.rpc.StubProvider import RpcStubProvider
from com.qxdzbc.p6.new_architecture.rpc.data_structure.SingleSignalResponse import \
    SingleSignalResponse
from com.qxdzbc.p6.new_architecture.rpc.data_structure.worksheet.WorksheetId import \
    WorksheetId
from com.qxdzbc.p6.new_architecture.rpc.data_structure.workbook.AddWorksheetRequest import AddWorksheetRequest
from com.qxdzbc.p6.new_architecture.rpc.data_structure.workbook.CreateNewWorksheetRequest import \
    CreateNewWorksheetRequest
from com.qxdzbc.p6.new_architecture.rpc.data_structure.workbook.GetAllWorksheetsResponse import \
    GetAllWorksheetsResponse
from com.qxdzbc.p6.new_architecture.rpc.data_structure.workbook.GetWorksheetResponse import GetWorksheetResponse
from com.qxdzbc.p6.new_architecture.rpc.data_structure.workbook.RenameWorksheetRequest import \
    RenameWorksheetRequest
from com.qxdzbc.p6.new_architecture.rpc.data_structure.workbook.SetWbNameRequest import SetWbNameRequest
from com.qxdzbc.p6.new_architecture.rpc.data_structure.workbook.WorksheetWithErrorReportMsg import \
    WorksheetWithErrorReportMsg
from com.qxdzbc.p6.new_architecture.rpc.data_structure.worksheet.WorksheetIdWithIndex import WorksheetIdWithIndex
from com.qxdzbc.p6.new_architecture.worksheet.RpcWorksheet import RpcWorksheet
from com.qxdzbc.p6.proto.CommonProtos_pb2 import SingleSignalResponseProto
from com.qxdzbc.p6.proto.WorksheetProtos_pb2 import GetWorksheetResponseProto
from com.qxdzbc.p6.proto.WorkbookProtos_pb2 import WorksheetWithErrorReportMsgProto
from com.qxdzbc.p6.proto.rpc.WorkbookService_pb2_grpc import WorkbookServiceStub


class RpcWorkbook(Workbook):
    _serverDownReport = RpcErrors.RpcServerIsDown \
        .report("Can't get sheet count because rpc server is down.")
    _serverDownException = _serverDownReport.toException()

    @staticmethod
    def fromNameAndPath(
            name: str,
            path: Optional[Path] = None,
            stubProvider: RpcStubProvider = RpcServiceContainer.insecureRpcServiceProvider()
    ):
        return RpcWorkbook(
            wbKey = WorkbookKeyImp(name, path),
            stubProvider = stubProvider
        )


    def __init__(
            self,
            wbKey:WorkbookKey,
            stubProvider: RpcStubProvider = RpcServiceContainer.insecureRpcServiceProvider()
    ):
        self.__key = wbKey
        self._stubProvider = stubProvider

    def __eq__(self, o: object) -> bool:
        if isinstance(o,Workbook):
            return self.workbookKey == o.key
        else:
            return False

    def setStubProvider(self, stubProvider: RpcStubProvider):
        self._stubProvider = stubProvider

    @property
    def _wbsv(self) -> Optional[WorkbookServiceStub]:
        return self._stubProvider.wbService

    ### >> Workbook << ###

    @property
    def worksheets(self) -> list[Worksheet]:
        def f() -> list[Worksheet]:
            outProto = self._wbsv.getAllWorksheets(self.workbookKey.toProtoObj())
            out = GetAllWorksheetsResponse.fromProto(outProto)
            return out.worksheets

        return self._onWbsvOk(f)

    @property
    def workbookKey(self) -> WorkbookKey:
        return self.__key

    @workbookKey.setter
    def workbookKey(self, newKey: WorkbookKey):
        self.__key = newKey

    def setActiveWorksheetRs(self, indexOrName: Union[int, str]) -> Result[None, ErrorReport]:
        if isinstance(indexOrName, int):
            return self.setActiveWorksheetByIndexRs(indexOrName)
        elif isinstance(indexOrName, str):
            return self.setActiveWorksheetByNameRs(indexOrName)
        else:
            return Err(CommonErrors.WrongTypeReport("nameOrIndex", "str or int"))

    def setActiveWorksheetByNameRs(self, name: str) -> Result[None, ErrorReport]:
        request = WorksheetIdWithIndex(
            wbKey = self.workbookKey,
            wsName = name
        )
        return self.setActiveWsRpcRs(request)

    def setActiveWorksheetByIndexRs(self, index: int) -> Result[None, ErrorReport]:
        request = WorksheetIdWithIndex(
            wbKey = self.workbookKey,
            wsIndex = index,
        )
        return self.setActiveWsRpcRs(request)

    def setActiveWsRpcRs(self, request: WorksheetIdWithIndex) -> Result[None, ErrorReport]:
        def f() -> Result[None, ErrorReport]:
            outProto: SingleSignalResponseProto = self._wbsv.setActiveWorksheet(
                request = request.toProtoObj())
            out = SingleSignalResponse.fromProto(outProto)
            if out.isError():
                return Err(out.errorReport)
            else:
                return Ok(None)

        return self._onWbsvOkRs(f)

    @property
    def activeWorksheet(self) -> Optional[Worksheet]:
        def f() -> Optional[Worksheet]:
            wbsv = self._wbsv
            outProto: GetWorksheetResponseProto = wbsv.getActiveWorksheet(self.workbookKey.toProtoObj())
            out = GetWorksheetResponse.fromProto(outProto)
            wsId =out.wsId
            if wsId:
                return RpcWorksheet(
                    name =wsId.wsName,
                    wbKey = wsId.wbKey,
                    stubProvider = self._stubProvider
                )
            else:
                return None

        return self._onWbsvOk(f)

    def isEmpty(self) -> bool:
        return self.sheetCount == 0

    def _onWbsvOkRs(self, f):
        return RpcUtils.onServiceOkRs(self._wbsv,f)

    def _onWbsvOk(self, f):
        return RpcUtils.onServiceOkOrRaise(self._wbsv, f)

    def _makeGetWsRpcRequestRs(self, request: WorksheetIdWithIndex) -> Result[Worksheet, ErrorReport]:
        def repStr(index, name) -> str:
            if name:
                return f"Worksheet \"{name}\" does not exist"
            if index:
                return f"Worksheet at index \"{index}\" does not exist"
            else:
                raise CommonErrors.WrongTypeReport("nameOrIndex", "str or int").toException()

        def f():
            outProto: GetWorksheetResponseProto = self._wbsv.getWorksheet(request = request.toProtoObj())
            out:GetWorksheetResponse = GetWorksheetResponse.fromProto(outProto)
            wsId = out.wsId

            if wsId:
                return Ok(wsId)
            else:
                return Err(WorkbookErrors.WorksheetNotExistReport.report(repStr(request.wsIndex, request.wsName)))

        return self._onWbsvOkRs(f)

    def getWorksheetByNameRs(self, name: str) -> Result[Worksheet, ErrorReport]:
        req = WorksheetId(
            wbKey = self.workbookKey,
            wsName = name
        )
        return self._makeGetWsRpcRequestRs(req)

    def getWorksheetByIndexRs(self, index: int) -> Result[Worksheet, ErrorReport]:
        req = WorksheetIdWithIndex(
            wbKey = self.workbookKey,
            wsIndex = index
        )
        return self._makeGetWsRpcRequestRs(req)

    def getWorksheetRs(self, nameOrIndex: Union[str, int]) -> Result[Worksheet, ErrorReport]:
        if isinstance(nameOrIndex, str):
            return self.getWorksheetByNameRs(nameOrIndex)
        elif isinstance(nameOrIndex, int):
            return self.getWorksheetByIndexRs(nameOrIndex)
        else:
            return Err(CommonErrors.WrongTypeReport("nameOrIndex", "str or int"))

    @property
    def sheetCount(self) -> int:
        if self._wbsv is not None:
            out: RpcValues.Int64Value = self._wbsv.sheetCount(
                request = self.workbookKey.toProtoObj()
            )
            return out.value
        else:
            raise RpcWorkbook._serverDownException

    @property
    def path(self) -> Path:
        return self.workbookKey.filePath

    @path.setter
    def path(self, newPath: Path):
        self.key = WorkbookKeys.fromNameAndPath(self.name, newPath)

    @property
    def name(self) -> str:
        return self.workbookKey.fileName

    @workbookKey.setter
    def key(self, newKey: WorkbookKey):
        if self._wbsv is not None:
            if newKey == self.__key:
                return
            else:
                outProto = self._wbsv.setWbKey(
                    request = SetWbNameRequest(
                        wbKey = self.__key,
                        newWbKey = newKey
                    ).toProtoObj()
                )
                out: SingleSignalResponse = SingleSignalResponse.fromProto(outProto)
                err = out.errorReport
                if err is not None:
                    raise err.toException()
                else:
                    self.__key = newKey
        else:
            raise RpcWorkbook._serverDownException

    def createNewWorksheetRs(self, newSheetName: Optional[str] = None) -> Result[Worksheet, ErrorReport]:
        def f() -> Result[Worksheet, ErrorReport]:
            req = CreateNewWorksheetRequest(
                wbKey = self.__key,
                newWorksheetName = newSheetName
            ).toProtoObj()
            outProto: WorksheetWithErrorReportMsgProto = self._wbsv.createNewWorksheet(request = req)
            out = WorksheetWithErrorReportMsg.fromProto(outProto)
            if out.isErr():
                return Err(out.errorReport)
            else:
                ws = RpcWorksheet(
                    name=out.wsName,
                    wbKey = self.__key,
                    stubProvider =self._stubProvider
                )
                return Ok(ws)

        return self._onWbsvOkRs(f)

    def _deleteWorksheetRsRpc(self, request: WorksheetIdWithIndex) -> Result[None, ErrorReport]:
        def f() -> Result[None, ErrorReport]:
            req = request.toProtoObj()
            outProto: SingleSignalResponseProto = self._wbsv.deleteWorksheet(request = req)
            out = SingleSignalResponse.fromProto(outProto)
            return out.toRs()

        return self._onWbsvOkRs(f)

    def deleteWorksheetByNameRs(self, sheetName: str) -> Result[None, ErrorReport]:
        req = WorksheetIdWithIndex(
            wbKey = self.__key,
            wsName = sheetName
        )
        return self._deleteWorksheetRsRpc(req)

    def deleteWorksheetByIndexRs(self, index: int) -> Result[None, ErrorReport]:
        req = WorksheetIdWithIndex(
            wbKey = self.__key,
            wsIndex = index
        )
        return self._deleteWorksheetRsRpc(req)

    def addWorksheetRs(self, ws: Worksheet) -> Result[Worksheet, ErrorReport]:
        def f() -> Result[None, ErrorReport]:
            req = AddWorksheetRequest(
                wbKey = self.__key,
                worksheet = ws
            )
            outProto: SingleSignalResponseProto = self._wbsv.addWorksheet(request = req.toProtoObj())
            out = SingleSignalResponse.fromProto(outProto)
            if out.isOk():
                ws.workbook = self
                return Ok(ws)
            else:
                return out.toRs()

        return self._onWbsvOkRs(f)

    def renameWorksheetName(self, oldName: str, newName: str):
        rs = self.renameWorksheetNameRs(oldName, newName)
        return Results.extractOrRaise(rs)

    def renameWorksheetNameRs(self, oldName: str, newName: str) -> Result[None, ErrorReport]:
        def f() -> Result[None, ErrorReport]:
            req = RenameWorksheetRequest(
                wbKey = self.__key,
                oldName = oldName,
                newName = newName
            )
            outProto: SingleSignalResponseProto = self._wbsv.renameWorksheet(request = req.toProtoObj())
            out = SingleSignalResponse.fromProto(outProto)
            return out.toRs()
        return self._onWbsvOkRs(f)

    @property
    def rootWorkbook(self) -> 'Workbook':
        return self
