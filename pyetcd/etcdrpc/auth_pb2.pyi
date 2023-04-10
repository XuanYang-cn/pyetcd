from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Permission(_message.Message):
    __slots__ = ["key", "permType", "range_end"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    KEY_FIELD_NUMBER: _ClassVar[int]
    PERMTYPE_FIELD_NUMBER: _ClassVar[int]
    RANGE_END_FIELD_NUMBER: _ClassVar[int]
    READ: Permission.Type
    READWRITE: Permission.Type
    WRITE: Permission.Type
    key: bytes
    permType: Permission.Type
    range_end: bytes
    def __init__(self, permType: _Optional[_Union[Permission.Type, str]] = ..., key: _Optional[bytes] = ..., range_end: _Optional[bytes] = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ["keyPermission", "name"]
    KEYPERMISSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    keyPermission: _containers.RepeatedCompositeFieldContainer[Permission]
    name: bytes
    def __init__(self, name: _Optional[bytes] = ..., keyPermission: _Optional[_Iterable[_Union[Permission, _Mapping]]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["name", "password", "roles"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    name: bytes
    password: bytes
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[bytes] = ..., password: _Optional[bytes] = ..., roles: _Optional[_Iterable[str]] = ...) -> None: ...
