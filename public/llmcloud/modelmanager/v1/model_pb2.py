# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: public/llmcloud/modelmanager/v1/model.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+public/llmcloud/modelmanager/v1/model.proto\x12\x1fpublic.llmcloud.modelmanager.v1\"\xbd\x01\n\x0cModelDetails\x12\x16\n\x06\x66\x61mily\x18\x01 \x01(\tR\x06\x66\x61mily\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\x12\x12\n\x04size\x18\x03 \x01(\tR\x04size\x12\'\n\x0fsequence_length\x18\x04 \x01(\rR\x0esequenceLength\x12\x10\n\x03tag\x18\x05 \x01(\tR\x03tag\x12\x18\n\x07license\x18\x06 \x01(\tR\x07license\x12\x12\n\x04name\x18\x07 \x01(\tR\x04name\"%\n\tModelMeta\x12\x18\n\x07\x63reated\x18\x01 \x01(\rR\x07\x63reated\"\xa0\x01\n\x05Model\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12G\n\x07\x64\x65tails\x18\x02 \x01(\x0b\x32-.public.llmcloud.modelmanager.v1.ModelDetailsR\x07\x64\x65tails\x12>\n\x04meta\x18\x03 \x01(\x0b\x32*.public.llmcloud.modelmanager.v1.ModelMetaR\x04metaB\x9d\x02\n#com.public.llmcloud.modelmanager.v1B\nModelProtoP\x01ZIgit.groq.io/cloud/go-proto/public/llmcloud/modelmanager/v1;modelmanagerv1\xa2\x02\x03PLM\xaa\x02\x1fPublic.Llmcloud.Modelmanager.V1\xca\x02 Public_\\Llmcloud\\Modelmanager\\V1\xe2\x02,Public_\\Llmcloud\\Modelmanager\\V1\\GPBMetadata\xea\x02\"Public::Llmcloud::Modelmanager::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.llmcloud.modelmanager.v1.model_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#com.public.llmcloud.modelmanager.v1B\nModelProtoP\001ZIgit.groq.io/cloud/go-proto/public/llmcloud/modelmanager/v1;modelmanagerv1\242\002\003PLM\252\002\037Public.Llmcloud.Modelmanager.V1\312\002 Public_\\Llmcloud\\Modelmanager\\V1\342\002,Public_\\Llmcloud\\Modelmanager\\V1\\GPBMetadata\352\002\"Public::Llmcloud::Modelmanager::V1'
  _globals['_MODELDETAILS']._serialized_start=81
  _globals['_MODELDETAILS']._serialized_end=270
  _globals['_MODELMETA']._serialized_start=272
  _globals['_MODELMETA']._serialized_end=309
  _globals['_MODEL']._serialized_start=312
  _globals['_MODEL']._serialized_end=472
# @@protoc_insertion_point(module_scope)
