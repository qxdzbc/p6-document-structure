import unittest
from pathlib import Path

from com.emeraldblast.p6.document_structure.communication.event.data_structure.app_event.SetActiveWorksheetRequest import \
    SetActiveWorksheetRequest
from com.emeraldblast.p6.document_structure.workbook.key.WorkbookKeys import WorkbookKeys
from com.emeraldblast.p6.proto.AppEventProtos_pb2 import SetActiveWorksheetRequestProto


class SetActiveWorksheetRequest_test(unittest.TestCase):
    def test_fromProtoBytes(self):
        wk = WorkbookKeys.fromNameAndPath("B",Path("abc").absolute())

        proto = SetActiveWorksheetRequestProto()
        proto.workbookKey.CopyFrom(wk.toProtoObj())
        proto.worksheetName = "worksheetName"

        o = SetActiveWorksheetRequest.fromProtoBytes(proto.SerializeToString())
        self.assertEqual(wk,o.workbookKey)
        self.assertEqual(proto.worksheetName,o.worksheetName)
    def test_toProto(self):
        wk = WorkbookKeys.fromNameAndPath("B", Path("abc").absolute())
        request = SetActiveWorksheetRequest(
            workbookKey = wk,
            worksheetName = "Name123"
        )

        proto = request.toProtoObj()
        self.assertEqual(wk.toProtoObj(), proto.workbookKey)
        self.assertEqual(request.worksheetName, proto.worksheetName)



if __name__ == '__main__':
    unittest.main()
