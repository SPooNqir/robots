# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: robots.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
import groups_pb2 as groups__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='robots.proto',
  package='robots',
  syntax='proto3',
  serialized_options=b'Z\032github.com/SPooNqir/robots\222A\217\004\022\201\001\n\021Spoon - Robots WS\"e\n\020Spoon Cloud Team\0221https://gitlab.com/SpoonQIR/Cloud/services/robots\032\036sebastien.lavayssiere@spoon.ai2\0050.0.1*\002\002\0012\020application/json:\020application/jsonRP\n\003403\022I\nGReturned when the user does not have permission to access the resource.R;\n\003404\0224\n*Returned when the resource does not exist.\022\006\n\004\232\002\001\007RW\n\003418\022P\n\rI\'m a teapot.\022?\n=\032;.grpc.gateway.examples.internal.proto.examplepb.NumericEnumZ#\n!\n\nApiKeyAuth\022\023\010\002\032\rAuthorization \002b\020\n\016\n\nApiKeyAuth\022\000rB\n\rlink for docs\0221https://gitlab.com/SpoonQIR/Cloud/services/robots',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0crobots.proto\x12\x06robots\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x0cgroups.proto\"\xdb\x01\n\x05Robot\x12\n\n\x02id\x18\x01 \x01(\x04\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0b\n\x03gps\x18\x03 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\x12\x0b\n\x03mac\x18\x05 \x01(\t\x12\x1d\n\x06groups\x18\x06 \x03(\x0b\x32\r.groups.Group\x12\r\n\x05paths\x18\x07 \x03(\t\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x0b\n\x03key\x18\t \x01(\t\x12\x14\n\x0c\x64irectusUser\x18\n \x01(\t\x12\x18\n\x10\x64irectusPassword\x18\x0b \x01(\t\x12\x13\n\x0bpubsubTopic\x18\x0c \x01(\t\"Q\n\x06Robots\x12\x1b\n\x04list\x18\x01 \x03(\x0b\x32\r.robots.Robot\x12\r\n\x05limit\x18\x02 \x01(\x04\x12\x0e\n\x06offset\x18\x03 \x01(\x04\x12\x0b\n\x03max\x18\x04 \x01(\x04\"\x19\n\x06SaFile\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\"9\n\x0cRobotMessage\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04send\x18\x03 \x01(\x08\"M\n\rDirectusToken\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x0f\n\x07\x65xpires\x18\x02 \x01(\x03\x12\x15\n\rrefresh_token\x18\x03 \x01(\t2\xeb\x06\n\x06robots\x12<\n\x06GetAll\x12\x0e.robots.Robots\x1a\x0e.robots.Robots\"\x12\x82\xd3\xe4\x93\x02\x0c\x12\n/v1/robots\x12L\n\x08GetGraph\x12\x16.google.protobuf.Empty\x1a\x0e.groups.Groups\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v1/robots/graph\x12?\n\x03Get\x12\r.robots.Robot\x1a\r.robots.Robot\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/robots/id/{id}\x12_\n\x10GetDirectusToken\x12\r.robots.Robot\x1a\x15.robots.DirectusToken\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/robots/directustoken/{id}\x12\x65\n\x12GetMyDirectusToken\x12\x16.google.protobuf.Empty\x1a\x15.robots.DirectusToken\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/robots/directustoken\x12J\n\nGetByGroup\x12\r.groups.Group\x1a\x0e.robots.Robots\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/robots/group/{id}\x12N\n\tGetSAFile\x12\r.robots.Robot\x1a\x0e.robots.SaFile\"\"\x82\xd3\xe4\x93\x02\x1c\"\x1a/v1/robots/id/{id}/sa-file\x12:\n\x03\x41\x64\x64\x12\r.robots.Robot\x1a\r.robots.Robot\"\x15\x82\xd3\xe4\x93\x02\x0f\"\n/v1/robots:\x01*\x12]\n\x0bSendToRobot\x12\x14.robots.RobotMessage\x1a\x14.robots.RobotMessage\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/v1/robots/message/{id}:\x01*\x12=\n\x06Update\x12\r.robots.Robot\x1a\r.robots.Robot\"\x15\x82\xd3\xe4\x93\x02\x0f\x32\n/v1/robots:\x01*\x12V\n\x10UpdateMacAddress\x12\r.robots.Robot\x1a\r.robots.Robot\"$\x82\xd3\xe4\x93\x02\x1e\x1a\x1c/v1/robots/id/{id}/mac/{mac}B\xaf\x04Z\x1agithub.com/SPooNqir/robots\x92\x41\x8f\x04\x12\x81\x01\n\x11Spoon - Robots WS\"e\n\x10Spoon Cloud Team\x12\x31https://gitlab.com/SpoonQIR/Cloud/services/robots\x1a\x1esebastien.lavayssiere@spoon.ai2\x05\x30.0.1*\x02\x02\x01\x32\x10\x61pplication/json:\x10\x61pplication/jsonRP\n\x03\x34\x30\x33\x12I\nGReturned when the user does not have permission to access the resource.R;\n\x03\x34\x30\x34\x12\x34\n*Returned when the resource does not exist.\x12\x06\n\x04\x9a\x02\x01\x07RW\n\x03\x34\x31\x38\x12P\n\rI\'m a teapot.\x12?\n=\x1a;.grpc.gateway.examples.internal.proto.examplepb.NumericEnumZ#\n!\n\nApiKeyAuth\x12\x13\x08\x02\x1a\rAuthorization \x02\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00rB\n\rlink for docs\x12\x31https://gitlab.com/SpoonQIR/Cloud/services/robotsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,protoc__gen__openapiv2_dot_options_dot_annotations__pb2.DESCRIPTOR,groups__pb2.DESCRIPTOR,])




_ROBOT = _descriptor.Descriptor(
  name='Robot',
  full_name='robots.Robot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='robots.Robot.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='robots.Robot.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gps', full_name='robots.Robot.gps', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='robots.Robot.address', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mac', full_name='robots.Robot.mac', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='groups', full_name='robots.Robot.groups', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='paths', full_name='robots.Robot.paths', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='robots.Robot.name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='robots.Robot.key', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='directusUser', full_name='robots.Robot.directusUser', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='directusPassword', full_name='robots.Robot.directusPassword', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pubsubTopic', full_name='robots.Robot.pubsubTopic', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=365,
)


_ROBOTS = _descriptor.Descriptor(
  name='Robots',
  full_name='robots.Robots',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='robots.Robots.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='robots.Robots.limit', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='robots.Robots.offset', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max', full_name='robots.Robots.max', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=367,
  serialized_end=448,
)


_SAFILE = _descriptor.Descriptor(
  name='SaFile',
  full_name='robots.SaFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='robots.SaFile.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=450,
  serialized_end=475,
)


_ROBOTMESSAGE = _descriptor.Descriptor(
  name='RobotMessage',
  full_name='robots.RobotMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='robots.RobotMessage.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='robots.RobotMessage.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='send', full_name='robots.RobotMessage.send', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=477,
  serialized_end=534,
)


_DIRECTUSTOKEN = _descriptor.Descriptor(
  name='DirectusToken',
  full_name='robots.DirectusToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='robots.DirectusToken.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expires', full_name='robots.DirectusToken.expires', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='refresh_token', full_name='robots.DirectusToken.refresh_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=536,
  serialized_end=613,
)

_ROBOT.fields_by_name['groups'].message_type = groups__pb2._GROUP
_ROBOTS.fields_by_name['list'].message_type = _ROBOT
DESCRIPTOR.message_types_by_name['Robot'] = _ROBOT
DESCRIPTOR.message_types_by_name['Robots'] = _ROBOTS
DESCRIPTOR.message_types_by_name['SaFile'] = _SAFILE
DESCRIPTOR.message_types_by_name['RobotMessage'] = _ROBOTMESSAGE
DESCRIPTOR.message_types_by_name['DirectusToken'] = _DIRECTUSTOKEN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Robot = _reflection.GeneratedProtocolMessageType('Robot', (_message.Message,), {
  'DESCRIPTOR' : _ROBOT,
  '__module__' : 'robots_pb2'
  # @@protoc_insertion_point(class_scope:robots.Robot)
  })
_sym_db.RegisterMessage(Robot)

Robots = _reflection.GeneratedProtocolMessageType('Robots', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTS,
  '__module__' : 'robots_pb2'
  # @@protoc_insertion_point(class_scope:robots.Robots)
  })
_sym_db.RegisterMessage(Robots)

SaFile = _reflection.GeneratedProtocolMessageType('SaFile', (_message.Message,), {
  'DESCRIPTOR' : _SAFILE,
  '__module__' : 'robots_pb2'
  # @@protoc_insertion_point(class_scope:robots.SaFile)
  })
_sym_db.RegisterMessage(SaFile)

RobotMessage = _reflection.GeneratedProtocolMessageType('RobotMessage', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTMESSAGE,
  '__module__' : 'robots_pb2'
  # @@protoc_insertion_point(class_scope:robots.RobotMessage)
  })
_sym_db.RegisterMessage(RobotMessage)

DirectusToken = _reflection.GeneratedProtocolMessageType('DirectusToken', (_message.Message,), {
  'DESCRIPTOR' : _DIRECTUSTOKEN,
  '__module__' : 'robots_pb2'
  # @@protoc_insertion_point(class_scope:robots.DirectusToken)
  })
_sym_db.RegisterMessage(DirectusToken)


DESCRIPTOR._options = None

_ROBOTS = _descriptor.ServiceDescriptor(
  name='robots',
  full_name='robots.robots',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=616,
  serialized_end=1491,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAll',
    full_name='robots.robots.GetAll',
    index=0,
    containing_service=None,
    input_type=_ROBOTS,
    output_type=_ROBOTS,
    serialized_options=b'\202\323\344\223\002\014\022\n/v1/robots',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetGraph',
    full_name='robots.robots.GetGraph',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=groups__pb2._GROUPS,
    serialized_options=b'\202\323\344\223\002\022\022\020/v1/robots/graph',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='robots.robots.Get',
    index=2,
    containing_service=None,
    input_type=_ROBOT,
    output_type=_ROBOT,
    serialized_options=b'\202\323\344\223\002\024\022\022/v1/robots/id/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDirectusToken',
    full_name='robots.robots.GetDirectusToken',
    index=3,
    containing_service=None,
    input_type=_ROBOT,
    output_type=_DIRECTUSTOKEN,
    serialized_options=b'\202\323\344\223\002\037\022\035/v1/robots/directustoken/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMyDirectusToken',
    full_name='robots.robots.GetMyDirectusToken',
    index=4,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_DIRECTUSTOKEN,
    serialized_options=b'\202\323\344\223\002\032\022\030/v1/robots/directustoken',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetByGroup',
    full_name='robots.robots.GetByGroup',
    index=5,
    containing_service=None,
    input_type=groups__pb2._GROUP,
    output_type=_ROBOTS,
    serialized_options=b'\202\323\344\223\002\027\022\025/v1/robots/group/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSAFile',
    full_name='robots.robots.GetSAFile',
    index=6,
    containing_service=None,
    input_type=_ROBOT,
    output_type=_SAFILE,
    serialized_options=b'\202\323\344\223\002\034\"\032/v1/robots/id/{id}/sa-file',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Add',
    full_name='robots.robots.Add',
    index=7,
    containing_service=None,
    input_type=_ROBOT,
    output_type=_ROBOT,
    serialized_options=b'\202\323\344\223\002\017\"\n/v1/robots:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendToRobot',
    full_name='robots.robots.SendToRobot',
    index=8,
    containing_service=None,
    input_type=_ROBOTMESSAGE,
    output_type=_ROBOTMESSAGE,
    serialized_options=b'\202\323\344\223\002\034\"\027/v1/robots/message/{id}:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='robots.robots.Update',
    index=9,
    containing_service=None,
    input_type=_ROBOT,
    output_type=_ROBOT,
    serialized_options=b'\202\323\344\223\002\0172\n/v1/robots:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateMacAddress',
    full_name='robots.robots.UpdateMacAddress',
    index=10,
    containing_service=None,
    input_type=_ROBOT,
    output_type=_ROBOT,
    serialized_options=b'\202\323\344\223\002\036\032\034/v1/robots/id/{id}/mac/{mac}',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROBOTS)

DESCRIPTOR.services_by_name['robots'] = _ROBOTS

# @@protoc_insertion_point(module_scope)
