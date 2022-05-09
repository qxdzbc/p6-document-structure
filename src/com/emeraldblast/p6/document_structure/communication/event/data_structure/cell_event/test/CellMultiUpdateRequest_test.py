import unittest

from com.emeraldblast.p6.document_structure.communication.event.data_structure.cell_event.CellMultiUpdateRequest import \
    CellMultiUpdateRequest

from com.emeraldblast.p6.document_structure.cell.address.CellAddresses import CellAddresses
from com.emeraldblast.p6.document_structure.workbook.key.WorkbookKeys import WorkbookKeys
from com.emeraldblast.p6.proto.CellProtos_pb2 import CellMultiUpdateRequestProto, CellUpdateContentProto, \
    CellUpdateEntryProto


class CellMultiUpdateRequest_test(unittest.TestCase):
    def test_fromProtoBytes(self):
        proto = CellMultiUpdateRequestProto()
        proto.workbookKey.CopyFrom(WorkbookKeys.fromNameAndPath("b123",None).toProtoObj())
        proto.worksheetName = "Sheet1"

        contentProto = CellUpdateContentProto()
        contentProto.formula = "formula_123"
        contentProto.literal = "literal_abc"
        entryProto = CellUpdateEntryProto()
        entryProto.content.CopyFrom(contentProto)
        addr = CellAddresses.fromLabel("@Q12")
        entryProto.cellAddress.CopyFrom(addr.toProtoObj())

        proto.cellUpdate.extend([entryProto])

        c = CellMultiUpdateRequest.fromProtoBytes(proto.SerializeToString())




if __name__ == '__main__':
    unittest.main()
