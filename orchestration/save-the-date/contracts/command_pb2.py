# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcommand.proto\x12\x0c\x63ommandqueue\"\x95\x01\n\x07\x43ommand\x12\x12\n\ncommand_id\x18\x01 \x01(\t\x12\x14\n\x0cservice_name\x18\x02 \x01(\t\x12\x14\n\x0c\x63ommand_type\x18\x03 \x01(\t\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\x12\x10\n\x08priority\x18\x05 \x01(\x05\x12\x13\n\x0bretry_count\x18\x06 \x01(\x05\x12\x12\n\ncreated_at\x18\x07 \x01(\t\"?\n\x15\x45nqueueCommandRequest\x12&\n\x07\x63ommand\x18\x01 \x01(\x0b\x32\x15.commandqueue.Command\":\n\x16\x45nqueueCommandResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"A\n\x15\x44\x65queueCommandRequest\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x12\n\ncommand_id\x18\x02 \x01(\t\"b\n\x16\x44\x65queueCommandResponse\x12&\n\x07\x63ommand\x18\x01 \x01(\x0b\x32\x15.commandqueue.Command\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x0f\n\x07message\x18\x03 \x01(\t\"?\n\x13RetryCommandRequest\x12\x12\n\ncommand_id\x18\x01 \x01(\t\x12\x14\n\x0cservice_name\x18\x02 \x01(\t\"8\n\x14RetryCommandResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xa6\x02\n\x13\x43ommandQueueService\x12[\n\x0e\x45nqueueCommand\x12#.commandqueue.EnqueueCommandRequest\x1a$.commandqueue.EnqueueCommandResponse\x12[\n\x0e\x44\x65queueCommand\x12#.commandqueue.DequeueCommandRequest\x1a$.commandqueue.DequeueCommandResponse\x12U\n\x0cRetryCommand\x12!.commandqueue.RetryCommandRequest\x1a\".commandqueue.RetryCommandResponseB\x14\xaa\x02\x11\x63ontracts.commandb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'command_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\021contracts.command'
  _globals['_COMMAND']._serialized_start=32
  _globals['_COMMAND']._serialized_end=181
  _globals['_ENQUEUECOMMANDREQUEST']._serialized_start=183
  _globals['_ENQUEUECOMMANDREQUEST']._serialized_end=246
  _globals['_ENQUEUECOMMANDRESPONSE']._serialized_start=248
  _globals['_ENQUEUECOMMANDRESPONSE']._serialized_end=306
  _globals['_DEQUEUECOMMANDREQUEST']._serialized_start=308
  _globals['_DEQUEUECOMMANDREQUEST']._serialized_end=373
  _globals['_DEQUEUECOMMANDRESPONSE']._serialized_start=375
  _globals['_DEQUEUECOMMANDRESPONSE']._serialized_end=473
  _globals['_RETRYCOMMANDREQUEST']._serialized_start=475
  _globals['_RETRYCOMMANDREQUEST']._serialized_end=538
  _globals['_RETRYCOMMANDRESPONSE']._serialized_start=540
  _globals['_RETRYCOMMANDRESPONSE']._serialized_end=596
  _globals['_COMMANDQUEUESERVICE']._serialized_start=599
  _globals['_COMMANDQUEUESERVICE']._serialized_end=893
# @@protoc_insertion_point(module_scope)