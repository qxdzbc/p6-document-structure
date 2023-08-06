# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/qxdzbc/p6/proto/rpc/WorkbookService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.qxdzbc.p6.proto import CommonProtos_pb2 as com_dot_qxdzbc_dot_p6_dot_proto_dot_CommonProtos__pb2
from com.qxdzbc.p6.proto import WorksheetProtos_pb2 as com_dot_qxdzbc_dot_p6_dot_proto_dot_WorksheetProtos__pb2
from com.qxdzbc.p6.proto import WorkbookProtos_pb2 as com_dot_qxdzbc_dot_p6_dot_proto_dot_WorkbookProtos__pb2
from com.qxdzbc.p6.proto import DocProtos_pb2 as com_dot_qxdzbc_dot_p6_dot_proto_dot_DocProtos__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-com/qxdzbc/p6/proto/rpc/WorkbookService.proto\x12\x17\x63om.qxdzbc.p6.proto.rpc\x1a&com/qxdzbc/p6/proto/CommonProtos.proto\x1a)com/qxdzbc/p6/proto/WorksheetProtos.proto\x1a(com/qxdzbc/p6/proto/WorkbookProtos.proto\x1a#com/qxdzbc/p6/proto/DocProtos.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/protobuf/empty.proto2\xe6\t\n\x0fWorkbookService\x12O\n\x07wsCount\x12%.com.qxdzbc.p6.proto.WorkbookKeyProto\x1a\x1b.google.protobuf.Int64Value\"\x00\x12g\n\x08setWbKey\x12).com.qxdzbc.p6.proto.SetWbKeyRequestProto\x1a..com.qxdzbc.p6.proto.SingleSignalResponseProto\"\x00\x12o\n\x10getAllWorksheets\x12%.com.qxdzbc.p6.proto.WorkbookKeyProto\x1a\x32.com.qxdzbc.p6.proto.GetAllWorksheetsResponseProto\"\x00\x12v\n\x12setActiveWorksheet\x12..com.qxdzbc.p6.proto.WorksheetIdWithIndexProto\x1a..com.qxdzbc.p6.proto.SingleSignalResponseProto\"\x00\x12m\n\x12getActiveWorksheet\x12%.com.qxdzbc.p6.proto.WorkbookKeyProto\x1a..com.qxdzbc.p6.proto.GetWorksheetResponseProto\"\x00\x12p\n\x0cgetWorksheet\x12..com.qxdzbc.p6.proto.WorksheetIdWithIndexProto\x1a..com.qxdzbc.p6.proto.GetWorksheetResponseProto\"\x00\x12\x82\x01\n\x12\x63reateNewWorksheet\x12\x33.com.qxdzbc.p6.proto.CreateNewWorksheetRequestProto\x1a\x35.com.qxdzbc.p6.proto.WorksheetWithErrorReportMsgProto\"\x00\x12s\n\x0fremoveWorksheet\x12..com.qxdzbc.p6.proto.WorksheetIdWithIndexProto\x1a..com.qxdzbc.p6.proto.SingleSignalResponseProto\"\x00\x12m\n\x12removeAllWorksheet\x12%.com.qxdzbc.p6.proto.WorkbookKeyProto\x1a..com.qxdzbc.p6.proto.SingleSignalResponseProto\"\x00\x12o\n\x0c\x61\x64\x64Worksheet\x12-.com.qxdzbc.p6.proto.AddWorksheetRequestProto\x1a..com.qxdzbc.p6.proto.SingleSignalResponseProto\"\x00\x12u\n\x0frenameWorksheet\x12\x30.com.qxdzbc.p6.proto.RenameWorksheetRequestProto\x1a..com.qxdzbc.p6.proto.SingleSignalResponseProto\"\x00\x62\x06proto3')



_WORKBOOKSERVICE = DESCRIPTOR.services_by_name['WorkbookService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WORKBOOKSERVICE._serialized_start=298
  _WORKBOOKSERVICE._serialized_end=1552
# @@protoc_insertion_point(module_scope)
