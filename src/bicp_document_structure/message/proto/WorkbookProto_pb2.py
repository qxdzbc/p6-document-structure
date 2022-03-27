# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WorkbookProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import Common_pb2 as Common__pb2
from . import DocProto_pb2 as DocProto__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13WorkbookProto.proto\x12\x1d\x63om.github.xadkile.p6.app.msg\x1a\x0c\x43ommon.proto\x1a\x0e\x44ocProto.proto\"\xe4\x01\n\x14RenameWorksheetProto\x12\x44\n\x0bworkbookKey\x18\x01 \x01(\x0b\x32/.com.github.xadkile.p6.app.msg.WorkbookKeyProto\x12\x0f\n\x07oldName\x18\x02 \x01(\t\x12\r\n\x05index\x18\x03 \x01(\x05\x12\x0f\n\x07newName\x18\x04 \x01(\t\x12\x0f\n\x07isError\x18\x05 \x01(\x08\x12\x44\n\x0b\x65rrorReport\x18\x06 \x01(\x0b\x32/.com.github.xadkile.p6.app.msg.ErrorReportProto\"\xd0\x01\n\x17\x43reateNewWorksheetProto\x12\x44\n\x0bworkbookKey\x18\x01 \x01(\x0b\x32/.com.github.xadkile.p6.app.msg.WorkbookKeyProto\x12\x18\n\x10newWorksheetName\x18\x02 \x01(\t\x12\x0f\n\x07isError\x18\x03 \x01(\x08\x12\x44\n\x0b\x65rrorReport\x18\x04 \x01(\x0b\x32/.com.github.xadkile.p6.app.msg.ErrorReportProtob\x06proto3')



_RENAMEWORKSHEETPROTO = DESCRIPTOR.message_types_by_name['RenameWorksheetProto']
_CREATENEWWORKSHEETPROTO = DESCRIPTOR.message_types_by_name['CreateNewWorksheetProto']
RenameWorksheetProto = _reflection.GeneratedProtocolMessageType('RenameWorksheetProto', (_message.Message,), {
  'DESCRIPTOR' : _RENAMEWORKSHEETPROTO,
  '__module__' : 'WorkbookProto_pb2'
  # @@protoc_insertion_point(class_scope:com.github.xadkile.p6.app.msg.RenameWorksheetProto)
  })
_sym_db.RegisterMessage(RenameWorksheetProto)

CreateNewWorksheetProto = _reflection.GeneratedProtocolMessageType('CreateNewWorksheetProto', (_message.Message,), {
  'DESCRIPTOR' : _CREATENEWWORKSHEETPROTO,
  '__module__' : 'WorkbookProto_pb2'
  # @@protoc_insertion_point(class_scope:com.github.xadkile.p6.app.msg.CreateNewWorksheetProto)
  })
_sym_db.RegisterMessage(CreateNewWorksheetProto)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RENAMEWORKSHEETPROTO._serialized_start=85
  _RENAMEWORKSHEETPROTO._serialized_end=313
  _CREATENEWWORKSHEETPROTO._serialized_start=316
  _CREATENEWWORKSHEETPROTO._serialized_end=524
# @@protoc_insertion_point(module_scope)
