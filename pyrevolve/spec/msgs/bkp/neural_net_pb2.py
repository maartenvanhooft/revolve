# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: neural_net.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import parameter_pb2 as parameter__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='neural_net.proto',
  package='revolve.msgs',
  syntax='proto2',
  serialized_pb=_b('\n\x10neural_net.proto\x12\x0crevolve.msgs\x1a\x0fparameter.proto\"<\n\x10NeuralConnection\x12\x0b\n\x03src\x18\x01 \x02(\t\x12\x0b\n\x03\x64st\x18\x02 \x02(\t\x12\x0e\n\x06weight\x18\x03 \x02(\x01\"i\n\x06Neuron\x12\n\n\x02id\x18\x01 \x02(\t\x12\r\n\x05layer\x18\x02 \x02(\t\x12\x0c\n\x04type\x18\x03 \x02(\t\x12\x0e\n\x06partId\x18\x04 \x01(\t\x12&\n\x05param\x18\x05 \x03(\x0b\x32\x17.revolve.msgs.Parameter\"i\n\rNeuralNetwork\x12$\n\x06neuron\x18\x01 \x03(\x0b\x32\x14.revolve.msgs.Neuron\x12\x32\n\nconnection\x18\x02 \x03(\x0b\x32\x1e.revolve.msgs.NeuralConnection\"\xb9\x01\n\x13ModifyNeuralNetwork\x12\x15\n\rremove_hidden\x18\x01 \x03(\t\x12(\n\nadd_hidden\x18\x02 \x03(\x0b\x32\x14.revolve.msgs.Neuron\x12,\n\x0eset_parameters\x18\x04 \x03(\x0b\x32\x14.revolve.msgs.Neuron\x12\x33\n\x0bset_weights\x18\x03 \x03(\x0b\x32\x1e.revolve.msgs.NeuralConnection')
  ,
  dependencies=[parameter__pb2.DESCRIPTOR,])




_NEURALCONNECTION = _descriptor.Descriptor(
  name='NeuralConnection',
  full_name='revolve.msgs.NeuralConnection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='revolve.msgs.NeuralConnection.src', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dst', full_name='revolve.msgs.NeuralConnection.dst', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='revolve.msgs.NeuralConnection.weight', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=111,
)


_NEURON = _descriptor.Descriptor(
  name='Neuron',
  full_name='revolve.msgs.Neuron',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='revolve.msgs.Neuron.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='layer', full_name='revolve.msgs.Neuron.layer', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='revolve.msgs.Neuron.type', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partId', full_name='revolve.msgs.Neuron.partId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='param', full_name='revolve.msgs.Neuron.param', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=218,
)


_NEURALNETWORK = _descriptor.Descriptor(
  name='NeuralNetwork',
  full_name='revolve.msgs.NeuralNetwork',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='neuron', full_name='revolve.msgs.NeuralNetwork.neuron', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection', full_name='revolve.msgs.NeuralNetwork.connection', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=220,
  serialized_end=325,
)


_MODIFYNEURALNETWORK = _descriptor.Descriptor(
  name='ModifyNeuralNetwork',
  full_name='revolve.msgs.ModifyNeuralNetwork',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='remove_hidden', full_name='revolve.msgs.ModifyNeuralNetwork.remove_hidden', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='add_hidden', full_name='revolve.msgs.ModifyNeuralNetwork.add_hidden', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_parameters', full_name='revolve.msgs.ModifyNeuralNetwork.set_parameters', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_weights', full_name='revolve.msgs.ModifyNeuralNetwork.set_weights', index=3,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=328,
  serialized_end=513,
)

_NEURON.fields_by_name['param'].message_type = parameter__pb2._PARAMETER
_NEURALNETWORK.fields_by_name['neuron'].message_type = _NEURON
_NEURALNETWORK.fields_by_name['connection'].message_type = _NEURALCONNECTION
_MODIFYNEURALNETWORK.fields_by_name['add_hidden'].message_type = _NEURON
_MODIFYNEURALNETWORK.fields_by_name['set_parameters'].message_type = _NEURON
_MODIFYNEURALNETWORK.fields_by_name['set_weights'].message_type = _NEURALCONNECTION
DESCRIPTOR.message_types_by_name['NeuralConnection'] = _NEURALCONNECTION
DESCRIPTOR.message_types_by_name['Neuron'] = _NEURON
DESCRIPTOR.message_types_by_name['NeuralNetwork'] = _NEURALNETWORK
DESCRIPTOR.message_types_by_name['ModifyNeuralNetwork'] = _MODIFYNEURALNETWORK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NeuralConnection = _reflection.GeneratedProtocolMessageType('NeuralConnection', (_message.Message,), dict(
  DESCRIPTOR = _NEURALCONNECTION,
  __module__ = 'neural_net_pb2'
  # @@protoc_insertion_point(class_scope:revolve.msgs.NeuralConnection)
  ))
_sym_db.RegisterMessage(NeuralConnection)

Neuron = _reflection.GeneratedProtocolMessageType('Neuron', (_message.Message,), dict(
  DESCRIPTOR = _NEURON,
  __module__ = 'neural_net_pb2'
  # @@protoc_insertion_point(class_scope:revolve.msgs.Neuron)
  ))
_sym_db.RegisterMessage(Neuron)

NeuralNetwork = _reflection.GeneratedProtocolMessageType('NeuralNetwork', (_message.Message,), dict(
  DESCRIPTOR = _NEURALNETWORK,
  __module__ = 'neural_net_pb2'
  # @@protoc_insertion_point(class_scope:revolve.msgs.NeuralNetwork)
  ))
_sym_db.RegisterMessage(NeuralNetwork)

ModifyNeuralNetwork = _reflection.GeneratedProtocolMessageType('ModifyNeuralNetwork', (_message.Message,), dict(
  DESCRIPTOR = _MODIFYNEURALNETWORK,
  __module__ = 'neural_net_pb2'
  # @@protoc_insertion_point(class_scope:revolve.msgs.ModifyNeuralNetwork)
  ))
_sym_db.RegisterMessage(ModifyNeuralNetwork)


# @@protoc_insertion_point(module_scope)