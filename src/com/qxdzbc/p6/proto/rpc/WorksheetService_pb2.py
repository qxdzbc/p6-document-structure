# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/qxdzbc/p6/proto/rpc/WorksheetService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.qxdzbc.p6.proto import CommonProtos_pb2 as com_dot_qxdzbc_dot_p6_dot_proto_dot_CommonProtos__pb2
from com.qxdzbc.p6.proto import DocProtos_pb2 as com_dot_qxdzbc_dot_p6_dot_proto_dot_DocProtos__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from com.qxdzbc.p6.proto import WorksheetProtos_pb2 as com_dot_qxdzbc_dot_p6_dot_proto_dot_WorksheetProtos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.com/qxdzbc/p6/proto/rpc/WorksheetService.proto\x12\x17\x63om.qxdzbc.p6.proto.rpc\x1a&com/qxdzbc/p6/proto/CommonProtos.proto\x1a#com/qxdzbc/p6/proto/DocProtos.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a)com/qxdzbc/p6/proto/WorksheetProtos.proto2\xea\t\n\x10WorksheetService\x12]\n\x07getCell\x12 .com.qxdzbc.p6.proto.CellIdProto\x1a..com.qxdzbc.p6.proto.SingleSignalResponseProto\"\x00\x12\x63\n\ngetAllCell\x12%.com.qxdzbc.p6.proto.WorksheetIdProto\x1a,.com.qxdzbc.p6.proto.GetAllCellResponseProto\"\x00\x12\x64\n\x0cgetCellCount\x12%.com.qxdzbc.p6.proto.WorksheetIdProto\x1a+.com.qxdzbc.p6.proto.CellCountResponseProto\"\x00\x12n\n\x13getUsedRangeAddress\x12%.com.qxdzbc.p6.proto.WorksheetIdProto\x1a..com.qxdzbc.p6.proto.GetUsedRangeResponseProto\"\x00\x12[\n\x05paste\x12 .com.qxdzbc.p6.proto.CellIdProto\x1a..com.qxdzbc.p6.proto.SingleSignalResponseProto\"\x00\x12[\n\x07\x61\x64\x64\x43\x65ll\x12\x1e.com.qxdzbc.p6.proto.CellProto\x1a..com.qxdzbc.p6.proto.SingleSignalResponseProto\"\x00\x12`\n\nremoveCell\x12 .com.qxdzbc.p6.proto.CellIdProto\x1a..com.qxdzbc.p6.proto.SingleSignalResponseProto\"\x00\x12h\n\rremoveAllCell\x12%.com.qxdzbc.p6.proto.WorksheetIdProto\x1a..com.qxdzbc.p6.proto.SingleSignalResponseProto\"\x00\x12\x62\n\x0bremoveRange\x12!.com.qxdzbc.p6.proto.RangeIdProto\x1a..com.qxdzbc.p6.proto.SingleSignalResponseProto\"\x00\x12k\n\x0e\x63ontainAddress\x12\x34.com.qxdzbc.p6.proto.CheckContainAddressRequestProto\x1a!.com.qxdzbc.p6.proto.BoolMsgProto\"\x00\x12g\n\x08loadData\x12).com.qxdzbc.p6.proto.LoadDataRequestProto\x1a..com.qxdzbc.p6.proto.SingleSignalResponseProto\"\x00\x12|\n\x16updateMultiCellContent\x12\x30.com.qxdzbc.p6.proto.MultiCellUpdateRequestProto\x1a..com.qxdzbc.p6.proto.SingleSignalResponseProto\"\x00\x62\x06proto3')



_WORKSHEETSERVICE = DESCRIPTOR.services_by_name['WorksheetService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WORKSHEETSERVICE._serialized_start=257
  _WORKSHEETSERVICE._serialized_end=1515
# @@protoc_insertion_point(module_scope)
