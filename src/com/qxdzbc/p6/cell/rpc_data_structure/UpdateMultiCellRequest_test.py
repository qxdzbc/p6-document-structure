import unittest

from com.qxdzbc.p6.cell.address.CellAddresses import CellAddresses
from com.qxdzbc.p6.workbook.key.WorkbookKeys import WorkbookKeys
from com.qxdzbc.p6.cell.rpc_data_structure.UpdateMultiCellRequest import \
    UpdateMultiCellRequest


class UpdateMultiCellRequest_test(unittest.TestCase):
    pass
    # def test_fromProtoBytes(self):
    #     proto = CellMultiUpdateRequestProto()
    #     proto.workbookKey.CopyFrom(WorkbookKeys.fromNameAndPath("b123",None).toProtoObj())
    #     proto.worksheetName = "Sheet1"
    #
    #     contentProto = CellUpdateContentProto()
    #     contentProto.formula = "formula_123"
    #     contentProto.literal = "literal_abc"
    #     entryProto = CellUpdateEntryProto()
    #     entryProto.content.CopyFrom(contentProto)
    #     addr = CellAddresses.fromLabel("Q12")
    #     entryProto.cellAddress.CopyFrom(addr.toProtoObj())
    #
    #     proto.cellUpdate.extend([entryProto])
    #
    #     c = CellMultiUpdateRequest.fromProtoBytes(proto.SerializeToString())




if __name__ == '__main__':
    unittest.main()
