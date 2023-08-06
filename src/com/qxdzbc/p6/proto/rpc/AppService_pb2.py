# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/qxdzbc/p6/proto/rpc/AppService.proto
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
from com.qxdzbc.p6.proto import WorksheetProtos_pb2 as com_dot_qxdzbc_dot_p6_dot_proto_dot_WorksheetProtos__pb2
from com.qxdzbc.p6.proto import AppProtos_pb2 as com_dot_qxdzbc_dot_p6_dot_proto_dot_AppProtos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(com/qxdzbc/p6/proto/rpc/AppService.proto\x12\x17\x63om.qxdzbc.p6.proto.rpc\x1a&com/qxdzbc/p6/proto/CommonProtos.proto\x1a#com/qxdzbc/p6/proto/DocProtos.proto\x1a)com/qxdzbc/p6/proto/WorksheetProtos.proto\x1a#com/qxdzbc/p6/proto/AppProtos.proto2\xe4\x08\n\nAppService\x12u\n\x0bgetWorkbook\x12,.com.qxdzbc.p6.proto.GetWorkbookRequestProto\x1a\x36.com.qxdzbc.p6.proto.WorkbookKeyWithErrorResponseProto\"\x00\x12~\n\x11\x63reateNewWorkbook\x12\x32.com.qxdzbc.p6.proto.CreateNewWorkbookRequestProto\x1a\x33.com.qxdzbc.p6.proto.CreateNewWorkbookResponseProto\"\x00\x12n\n\x11getActiveWorkbook\x12\x1f.com.qxdzbc.p6.proto.EmptyProto\x1a\x36.com.qxdzbc.p6.proto.WorkbookKeyWithErrorResponseProto\"\x00\x12l\n\x11setActiveWorkbook\x12%.com.qxdzbc.p6.proto.WorkbookKeyProto\x1a..com.qxdzbc.p6.proto.SingleSignalResponseProto\"\x00\x12g\n\x12getActiveWorksheet\x12\x1f.com.qxdzbc.p6.proto.EmptyProto\x1a..com.qxdzbc.p6.proto.GetWorksheetResponseProto\"\x00\x12u\n\x12saveWorkbookAtPath\x12-.com.qxdzbc.p6.proto.SaveWorkbookRequestProto\x1a..com.qxdzbc.p6.proto.SaveWorkbookResponseProto\"\x00\x12o\n\x0cloadWorkbook\x12-.com.qxdzbc.p6.proto.LoadWorkbookRequestProto\x1a..com.qxdzbc.p6.proto.LoadWorkbookResponseProto\"\x00\x12h\n\rcloseWorkbook\x12%.com.qxdzbc.p6.proto.WorkbookKeyProto\x1a..com.qxdzbc.p6.proto.SingleSignalResponseProto\"\x00\x12^\n\x10\x63heckWbExistence\x12%.com.qxdzbc.p6.proto.WorkbookKeyProto\x1a!.com.qxdzbc.p6.proto.BoolMsgProto\"\x00\x12\x66\n\x0fgetAllWorkbooks\x12\x1f.com.qxdzbc.p6.proto.EmptyProto\x1a\x30.com.qxdzbc.p6.proto.GetAllWorkbookResponseProto\"\x00\x62\x06proto3')



_APPSERVICE = DESCRIPTOR.services_by_name['AppService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _APPSERVICE._serialized_start=227
  _APPSERVICE._serialized_end=1351
# @@protoc_insertion_point(module_scope)
