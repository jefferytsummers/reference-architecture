# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04user\" \n\x0eGetUserRequest\x12\x0e\n\x06userId\x18\x01 \x01(\t\"\x1c\n\x0cGetUserReply\x12\x0c\n\x04name\x18\x01 \x01(\t\"<\n\x15UpdateUserNameRequest\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x13\n\x0bupdatedName\x18\x02 \x01(\t\"&\n\x13UpdateUserNameReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32;\n\x04User\x12\x33\n\x07GetUser\x12\x14.user.GetUserRequest\x1a\x12.user.GetUserReplyB\x11\xaa\x02\x0e\x63ontracts.userb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\016contracts.user'
  _globals['_GETUSERREQUEST']._serialized_start=20
  _globals['_GETUSERREQUEST']._serialized_end=52
  _globals['_GETUSERREPLY']._serialized_start=54
  _globals['_GETUSERREPLY']._serialized_end=82
  _globals['_UPDATEUSERNAMEREQUEST']._serialized_start=84
  _globals['_UPDATEUSERNAMEREQUEST']._serialized_end=144
  _globals['_UPDATEUSERNAMEREPLY']._serialized_start=146
  _globals['_UPDATEUSERNAMEREPLY']._serialized_end=184
  _globals['_USER']._serialized_start=186
  _globals['_USER']._serialized_end=245
# @@protoc_insertion_point(module_scope)
