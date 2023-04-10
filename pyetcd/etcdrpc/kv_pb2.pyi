from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ["kv", "prev_kv", "type"]
    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DELETE: Event.EventType
    KV_FIELD_NUMBER: _ClassVar[int]
    PREV_KV_FIELD_NUMBER: _ClassVar[int]
    PUT: Event.EventType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    kv: KeyValue
    prev_kv: KeyValue
    type: Event.EventType
    def __init__(self, type: _Optional[_Union[Event.EventType, str]] = ..., kv: _Optional[_Union[KeyValue, _Mapping]] = ..., prev_kv: _Optional[_Union[KeyValue, _Mapping]] = ...) -> None: ...

class KeyValue(_message.Message):
    __slots__ = ["create_revision", "key", "lease", "mod_revision", "value", "version"]
    CREATE_REVISION_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LEASE_FIELD_NUMBER: _ClassVar[int]
    MOD_REVISION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    create_revision: int
    key: bytes
    lease: int
    mod_revision: int
    value: bytes
    version: int
    def __init__(self, key: _Optional[bytes] = ..., create_revision: _Optional[int] = ..., mod_revision: _Optional[int] = ..., version: _Optional[int] = ..., value: _Optional[bytes] = ..., lease: _Optional[int] = ...) -> None: ...
