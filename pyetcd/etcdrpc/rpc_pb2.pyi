from . import kv_pb2 as _kv_pb2
import from . import auth_pb2 as _auth_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
NONE: AlarmType
NOSPACE: AlarmType

class AlarmMember(_message.Message):
    __slots__ = ["alarm", "memberID"]
    ALARM_FIELD_NUMBER: _ClassVar[int]
    MEMBERID_FIELD_NUMBER: _ClassVar[int]
    alarm: AlarmType
    memberID: int
    def __init__(self, memberID: _Optional[int] = ..., alarm: _Optional[_Union[AlarmType, str]] = ...) -> None: ...

class AlarmRequest(_message.Message):
    __slots__ = ["action", "alarm", "memberID"]
    class AlarmAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ACTIVATE: AlarmRequest.AlarmAction
    ALARM_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATE: AlarmRequest.AlarmAction
    GET: AlarmRequest.AlarmAction
    MEMBERID_FIELD_NUMBER: _ClassVar[int]
    action: AlarmRequest.AlarmAction
    alarm: AlarmType
    memberID: int
    def __init__(self, action: _Optional[_Union[AlarmRequest.AlarmAction, str]] = ..., memberID: _Optional[int] = ..., alarm: _Optional[_Union[AlarmType, str]] = ...) -> None: ...

class AlarmResponse(_message.Message):
    __slots__ = ["alarms", "header"]
    ALARMS_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    alarms: _containers.RepeatedCompositeFieldContainer[AlarmMember]
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., alarms: _Optional[_Iterable[_Union[AlarmMember, _Mapping]]] = ...) -> None: ...

class AuthDisableRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AuthDisableResponse(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ...) -> None: ...

class AuthEnableRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AuthEnableResponse(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ...) -> None: ...

class AuthRoleAddRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AuthRoleAddResponse(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ...) -> None: ...

class AuthRoleDeleteRequest(_message.Message):
    __slots__ = ["role"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: str
    def __init__(self, role: _Optional[str] = ...) -> None: ...

class AuthRoleDeleteResponse(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ...) -> None: ...

class AuthRoleGetRequest(_message.Message):
    __slots__ = ["role"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: str
    def __init__(self, role: _Optional[str] = ...) -> None: ...

class AuthRoleGetResponse(_message.Message):
    __slots__ = ["header", "perm"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PERM_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    perm: _containers.RepeatedCompositeFieldContainer[_auth_pb2.Permission]
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., perm: _Optional[_Iterable[_Union[_auth_pb2.Permission, _Mapping]]] = ...) -> None: ...

class AuthRoleGrantPermissionRequest(_message.Message):
    __slots__ = ["name", "perm"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERM_FIELD_NUMBER: _ClassVar[int]
    name: str
    perm: _auth_pb2.Permission
    def __init__(self, name: _Optional[str] = ..., perm: _Optional[_Union[_auth_pb2.Permission, _Mapping]] = ...) -> None: ...

class AuthRoleGrantPermissionResponse(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ...) -> None: ...

class AuthRoleListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AuthRoleListResponse(_message.Message):
    __slots__ = ["header", "roles"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., roles: _Optional[_Iterable[str]] = ...) -> None: ...

class AuthRoleRevokePermissionRequest(_message.Message):
    __slots__ = ["key", "range_end", "role"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    RANGE_END_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    key: str
    range_end: str
    role: str
    def __init__(self, role: _Optional[str] = ..., key: _Optional[str] = ..., range_end: _Optional[str] = ...) -> None: ...

class AuthRoleRevokePermissionResponse(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ...) -> None: ...

class AuthUserAddRequest(_message.Message):
    __slots__ = ["name", "password"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    name: str
    password: str
    def __init__(self, name: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AuthUserAddResponse(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ...) -> None: ...

class AuthUserChangePasswordRequest(_message.Message):
    __slots__ = ["name", "password"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    name: str
    password: str
    def __init__(self, name: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AuthUserChangePasswordResponse(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ...) -> None: ...

class AuthUserDeleteRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AuthUserDeleteResponse(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ...) -> None: ...

class AuthUserGetRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AuthUserGetResponse(_message.Message):
    __slots__ = ["header", "roles"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., roles: _Optional[_Iterable[str]] = ...) -> None: ...

class AuthUserGrantRoleRequest(_message.Message):
    __slots__ = ["role", "user"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    role: str
    user: str
    def __init__(self, user: _Optional[str] = ..., role: _Optional[str] = ...) -> None: ...

class AuthUserGrantRoleResponse(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ...) -> None: ...

class AuthUserListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AuthUserListResponse(_message.Message):
    __slots__ = ["header", "users"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    users: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., users: _Optional[_Iterable[str]] = ...) -> None: ...

class AuthUserRevokeRoleRequest(_message.Message):
    __slots__ = ["name", "role"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    role: str
    def __init__(self, name: _Optional[str] = ..., role: _Optional[str] = ...) -> None: ...

class AuthUserRevokeRoleResponse(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ...) -> None: ...

class AuthenticateRequest(_message.Message):
    __slots__ = ["name", "password"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    name: str
    password: str
    def __init__(self, name: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AuthenticateResponse(_message.Message):
    __slots__ = ["header", "token"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    token: str
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., token: _Optional[str] = ...) -> None: ...

class CompactionRequest(_message.Message):
    __slots__ = ["physical", "revision"]
    PHYSICAL_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    physical: bool
    revision: int
    def __init__(self, revision: _Optional[int] = ..., physical: bool = ...) -> None: ...

class CompactionResponse(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ...) -> None: ...

class Compare(_message.Message):
    __slots__ = ["create_revision", "key", "lease", "mod_revision", "range_end", "result", "target", "value", "version"]
    class CompareResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class CompareTarget(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CREATE: Compare.CompareTarget
    CREATE_REVISION_FIELD_NUMBER: _ClassVar[int]
    EQUAL: Compare.CompareResult
    GREATER: Compare.CompareResult
    KEY_FIELD_NUMBER: _ClassVar[int]
    LEASE: Compare.CompareTarget
    LEASE_FIELD_NUMBER: _ClassVar[int]
    LESS: Compare.CompareResult
    MOD: Compare.CompareTarget
    MOD_REVISION_FIELD_NUMBER: _ClassVar[int]
    NOT_EQUAL: Compare.CompareResult
    RANGE_END_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VALUE: Compare.CompareTarget
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VERSION: Compare.CompareTarget
    VERSION_FIELD_NUMBER: _ClassVar[int]
    create_revision: int
    key: bytes
    lease: int
    mod_revision: int
    range_end: bytes
    result: Compare.CompareResult
    target: Compare.CompareTarget
    value: bytes
    version: int
    def __init__(self, result: _Optional[_Union[Compare.CompareResult, str]] = ..., target: _Optional[_Union[Compare.CompareTarget, str]] = ..., key: _Optional[bytes] = ..., version: _Optional[int] = ..., create_revision: _Optional[int] = ..., mod_revision: _Optional[int] = ..., value: _Optional[bytes] = ..., lease: _Optional[int] = ..., range_end: _Optional[bytes] = ...) -> None: ...

class DefragmentRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DefragmentResponse(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ...) -> None: ...

class DeleteRangeRequest(_message.Message):
    __slots__ = ["key", "prev_kv", "range_end"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    PREV_KV_FIELD_NUMBER: _ClassVar[int]
    RANGE_END_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    prev_kv: bool
    range_end: bytes
    def __init__(self, key: _Optional[bytes] = ..., range_end: _Optional[bytes] = ..., prev_kv: bool = ...) -> None: ...

class DeleteRangeResponse(_message.Message):
    __slots__ = ["deleted", "header", "prev_kvs"]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PREV_KVS_FIELD_NUMBER: _ClassVar[int]
    deleted: int
    header: ResponseHeader
    prev_kvs: _containers.RepeatedCompositeFieldContainer[_kv_pb2.KeyValue]
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., deleted: _Optional[int] = ..., prev_kvs: _Optional[_Iterable[_Union[_kv_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

class HashKVRequest(_message.Message):
    __slots__ = ["revision"]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    revision: int
    def __init__(self, revision: _Optional[int] = ...) -> None: ...

class HashKVResponse(_message.Message):
    __slots__ = ["compact_revision", "hash", "header"]
    COMPACT_REVISION_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    compact_revision: int
    hash: int
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., hash: _Optional[int] = ..., compact_revision: _Optional[int] = ...) -> None: ...

class HashRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class HashResponse(_message.Message):
    __slots__ = ["hash", "header"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    hash: int
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., hash: _Optional[int] = ...) -> None: ...

class LeaseGrantRequest(_message.Message):
    __slots__ = ["ID", "TTL"]
    ID: int
    ID_FIELD_NUMBER: _ClassVar[int]
    TTL: int
    TTL_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, TTL: _Optional[int] = ..., ID: _Optional[int] = ...) -> None: ...

class LeaseGrantResponse(_message.Message):
    __slots__ = ["ID", "TTL", "error", "header"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ID: int
    ID_FIELD_NUMBER: _ClassVar[int]
    TTL: int
    TTL_FIELD_NUMBER: _ClassVar[int]
    error: str
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., ID: _Optional[int] = ..., TTL: _Optional[int] = ..., error: _Optional[str] = ...) -> None: ...

class LeaseKeepAliveRequest(_message.Message):
    __slots__ = ["ID"]
    ID: int
    ID_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, ID: _Optional[int] = ...) -> None: ...

class LeaseKeepAliveResponse(_message.Message):
    __slots__ = ["ID", "TTL", "header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ID: int
    ID_FIELD_NUMBER: _ClassVar[int]
    TTL: int
    TTL_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., ID: _Optional[int] = ..., TTL: _Optional[int] = ...) -> None: ...

class LeaseRevokeRequest(_message.Message):
    __slots__ = ["ID"]
    ID: int
    ID_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, ID: _Optional[int] = ...) -> None: ...

class LeaseRevokeResponse(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ...) -> None: ...

class LeaseTimeToLiveRequest(_message.Message):
    __slots__ = ["ID", "keys"]
    ID: int
    ID_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: bool
    def __init__(self, ID: _Optional[int] = ..., keys: bool = ...) -> None: ...

class LeaseTimeToLiveResponse(_message.Message):
    __slots__ = ["ID", "TTL", "grantedTTL", "header", "keys"]
    GRANTEDTTL_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ID: int
    ID_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    TTL: int
    TTL_FIELD_NUMBER: _ClassVar[int]
    grantedTTL: int
    header: ResponseHeader
    keys: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., ID: _Optional[int] = ..., TTL: _Optional[int] = ..., grantedTTL: _Optional[int] = ..., keys: _Optional[_Iterable[bytes]] = ...) -> None: ...

class Member(_message.Message):
    __slots__ = ["ID", "clientURLs", "name", "peerURLs"]
    CLIENTURLS_FIELD_NUMBER: _ClassVar[int]
    ID: int
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PEERURLS_FIELD_NUMBER: _ClassVar[int]
    clientURLs: _containers.RepeatedScalarFieldContainer[str]
    name: str
    peerURLs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ID: _Optional[int] = ..., name: _Optional[str] = ..., peerURLs: _Optional[_Iterable[str]] = ..., clientURLs: _Optional[_Iterable[str]] = ...) -> None: ...

class MemberAddRequest(_message.Message):
    __slots__ = ["peerURLs"]
    PEERURLS_FIELD_NUMBER: _ClassVar[int]
    peerURLs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, peerURLs: _Optional[_Iterable[str]] = ...) -> None: ...

class MemberAddResponse(_message.Message):
    __slots__ = ["header", "member", "members"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    member: Member
    members: _containers.RepeatedCompositeFieldContainer[Member]
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., member: _Optional[_Union[Member, _Mapping]] = ..., members: _Optional[_Iterable[_Union[Member, _Mapping]]] = ...) -> None: ...

class MemberListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MemberListResponse(_message.Message):
    __slots__ = ["header", "members"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    members: _containers.RepeatedCompositeFieldContainer[Member]
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., members: _Optional[_Iterable[_Union[Member, _Mapping]]] = ...) -> None: ...

class MemberRemoveRequest(_message.Message):
    __slots__ = ["ID"]
    ID: int
    ID_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, ID: _Optional[int] = ...) -> None: ...

class MemberRemoveResponse(_message.Message):
    __slots__ = ["header", "members"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    members: _containers.RepeatedCompositeFieldContainer[Member]
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., members: _Optional[_Iterable[_Union[Member, _Mapping]]] = ...) -> None: ...

class MemberUpdateRequest(_message.Message):
    __slots__ = ["ID", "peerURLs"]
    ID: int
    ID_FIELD_NUMBER: _ClassVar[int]
    PEERURLS_FIELD_NUMBER: _ClassVar[int]
    peerURLs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ID: _Optional[int] = ..., peerURLs: _Optional[_Iterable[str]] = ...) -> None: ...

class MemberUpdateResponse(_message.Message):
    __slots__ = ["header", "members"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    members: _containers.RepeatedCompositeFieldContainer[Member]
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., members: _Optional[_Iterable[_Union[Member, _Mapping]]] = ...) -> None: ...

class MoveLeaderRequest(_message.Message):
    __slots__ = ["targetID"]
    TARGETID_FIELD_NUMBER: _ClassVar[int]
    targetID: int
    def __init__(self, targetID: _Optional[int] = ...) -> None: ...

class MoveLeaderResponse(_message.Message):
    __slots__ = ["header"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ...) -> None: ...

class PutRequest(_message.Message):
    __slots__ = ["ignore_lease", "ignore_value", "key", "lease", "prev_kv", "value"]
    IGNORE_LEASE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_VALUE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LEASE_FIELD_NUMBER: _ClassVar[int]
    PREV_KV_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ignore_lease: bool
    ignore_value: bool
    key: bytes
    lease: int
    prev_kv: bool
    value: bytes
    def __init__(self, key: _Optional[bytes] = ..., value: _Optional[bytes] = ..., lease: _Optional[int] = ..., prev_kv: bool = ..., ignore_value: bool = ..., ignore_lease: bool = ...) -> None: ...

class PutResponse(_message.Message):
    __slots__ = ["header", "prev_kv"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PREV_KV_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    prev_kv: _kv_pb2.KeyValue
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., prev_kv: _Optional[_Union[_kv_pb2.KeyValue, _Mapping]] = ...) -> None: ...

class RangeRequest(_message.Message):
    __slots__ = ["count_only", "key", "keys_only", "limit", "max_create_revision", "max_mod_revision", "min_create_revision", "min_mod_revision", "range_end", "revision", "serializable", "sort_order", "sort_target"]
    class SortOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class SortTarget(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ASCEND: RangeRequest.SortOrder
    COUNT_ONLY_FIELD_NUMBER: _ClassVar[int]
    CREATE: RangeRequest.SortTarget
    DESCEND: RangeRequest.SortOrder
    KEY: RangeRequest.SortTarget
    KEYS_ONLY_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    MAX_CREATE_REVISION_FIELD_NUMBER: _ClassVar[int]
    MAX_MOD_REVISION_FIELD_NUMBER: _ClassVar[int]
    MIN_CREATE_REVISION_FIELD_NUMBER: _ClassVar[int]
    MIN_MOD_REVISION_FIELD_NUMBER: _ClassVar[int]
    MOD: RangeRequest.SortTarget
    NONE: RangeRequest.SortOrder
    RANGE_END_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    SERIALIZABLE_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    SORT_TARGET_FIELD_NUMBER: _ClassVar[int]
    VALUE: RangeRequest.SortTarget
    VERSION: RangeRequest.SortTarget
    count_only: bool
    key: bytes
    keys_only: bool
    limit: int
    max_create_revision: int
    max_mod_revision: int
    min_create_revision: int
    min_mod_revision: int
    range_end: bytes
    revision: int
    serializable: bool
    sort_order: RangeRequest.SortOrder
    sort_target: RangeRequest.SortTarget
    def __init__(self, key: _Optional[bytes] = ..., range_end: _Optional[bytes] = ..., limit: _Optional[int] = ..., revision: _Optional[int] = ..., sort_order: _Optional[_Union[RangeRequest.SortOrder, str]] = ..., sort_target: _Optional[_Union[RangeRequest.SortTarget, str]] = ..., serializable: bool = ..., keys_only: bool = ..., count_only: bool = ..., min_mod_revision: _Optional[int] = ..., max_mod_revision: _Optional[int] = ..., min_create_revision: _Optional[int] = ..., max_create_revision: _Optional[int] = ...) -> None: ...

class RangeResponse(_message.Message):
    __slots__ = ["count", "header", "kvs", "more"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    KVS_FIELD_NUMBER: _ClassVar[int]
    MORE_FIELD_NUMBER: _ClassVar[int]
    count: int
    header: ResponseHeader
    kvs: _containers.RepeatedCompositeFieldContainer[_kv_pb2.KeyValue]
    more: bool
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., kvs: _Optional[_Iterable[_Union[_kv_pb2.KeyValue, _Mapping]]] = ..., more: bool = ..., count: _Optional[int] = ...) -> None: ...

class RequestOp(_message.Message):
    __slots__ = ["request_delete_range", "request_put", "request_range", "request_txn"]
    REQUEST_DELETE_RANGE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_PUT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_RANGE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TXN_FIELD_NUMBER: _ClassVar[int]
    request_delete_range: DeleteRangeRequest
    request_put: PutRequest
    request_range: RangeRequest
    request_txn: TxnRequest
    def __init__(self, request_range: _Optional[_Union[RangeRequest, _Mapping]] = ..., request_put: _Optional[_Union[PutRequest, _Mapping]] = ..., request_delete_range: _Optional[_Union[DeleteRangeRequest, _Mapping]] = ..., request_txn: _Optional[_Union[TxnRequest, _Mapping]] = ...) -> None: ...

class ResponseHeader(_message.Message):
    __slots__ = ["cluster_id", "member_id", "raft_term", "revision"]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    RAFT_TERM_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    member_id: int
    raft_term: int
    revision: int
    def __init__(self, cluster_id: _Optional[int] = ..., member_id: _Optional[int] = ..., revision: _Optional[int] = ..., raft_term: _Optional[int] = ...) -> None: ...

class ResponseOp(_message.Message):
    __slots__ = ["response_delete_range", "response_put", "response_range", "response_txn"]
    RESPONSE_DELETE_RANGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_PUT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_RANGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TXN_FIELD_NUMBER: _ClassVar[int]
    response_delete_range: DeleteRangeResponse
    response_put: PutResponse
    response_range: RangeResponse
    response_txn: TxnResponse
    def __init__(self, response_range: _Optional[_Union[RangeResponse, _Mapping]] = ..., response_put: _Optional[_Union[PutResponse, _Mapping]] = ..., response_delete_range: _Optional[_Union[DeleteRangeResponse, _Mapping]] = ..., response_txn: _Optional[_Union[TxnResponse, _Mapping]] = ...) -> None: ...

class SnapshotRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SnapshotResponse(_message.Message):
    __slots__ = ["blob", "header", "remaining_bytes"]
    BLOB_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    REMAINING_BYTES_FIELD_NUMBER: _ClassVar[int]
    blob: bytes
    header: ResponseHeader
    remaining_bytes: int
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., remaining_bytes: _Optional[int] = ..., blob: _Optional[bytes] = ...) -> None: ...

class StatusRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StatusResponse(_message.Message):
    __slots__ = ["dbSize", "header", "leader", "raftIndex", "raftTerm", "version"]
    DBSIZE_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    LEADER_FIELD_NUMBER: _ClassVar[int]
    RAFTINDEX_FIELD_NUMBER: _ClassVar[int]
    RAFTTERM_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    dbSize: int
    header: ResponseHeader
    leader: int
    raftIndex: int
    raftTerm: int
    version: str
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., version: _Optional[str] = ..., dbSize: _Optional[int] = ..., leader: _Optional[int] = ..., raftIndex: _Optional[int] = ..., raftTerm: _Optional[int] = ...) -> None: ...

class TxnRequest(_message.Message):
    __slots__ = ["compare", "failure", "success"]
    COMPARE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    compare: _containers.RepeatedCompositeFieldContainer[Compare]
    failure: _containers.RepeatedCompositeFieldContainer[RequestOp]
    success: _containers.RepeatedCompositeFieldContainer[RequestOp]
    def __init__(self, compare: _Optional[_Iterable[_Union[Compare, _Mapping]]] = ..., success: _Optional[_Iterable[_Union[RequestOp, _Mapping]]] = ..., failure: _Optional[_Iterable[_Union[RequestOp, _Mapping]]] = ...) -> None: ...

class TxnResponse(_message.Message):
    __slots__ = ["header", "responses", "succeeded"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
    header: ResponseHeader
    responses: _containers.RepeatedCompositeFieldContainer[ResponseOp]
    succeeded: bool
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., succeeded: bool = ..., responses: _Optional[_Iterable[_Union[ResponseOp, _Mapping]]] = ...) -> None: ...

class WatchCancelRequest(_message.Message):
    __slots__ = ["watch_id"]
    WATCH_ID_FIELD_NUMBER: _ClassVar[int]
    watch_id: int
    def __init__(self, watch_id: _Optional[int] = ...) -> None: ...

class WatchCreateRequest(_message.Message):
    __slots__ = ["filters", "key", "prev_kv", "progress_notify", "range_end", "start_revision"]
    class FilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NODELETE: WatchCreateRequest.FilterType
    NOPUT: WatchCreateRequest.FilterType
    PREV_KV_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_NOTIFY_FIELD_NUMBER: _ClassVar[int]
    RANGE_END_FIELD_NUMBER: _ClassVar[int]
    START_REVISION_FIELD_NUMBER: _ClassVar[int]
    filters: _containers.RepeatedScalarFieldContainer[WatchCreateRequest.FilterType]
    key: bytes
    prev_kv: bool
    progress_notify: bool
    range_end: bytes
    start_revision: int
    def __init__(self, key: _Optional[bytes] = ..., range_end: _Optional[bytes] = ..., start_revision: _Optional[int] = ..., progress_notify: bool = ..., filters: _Optional[_Iterable[_Union[WatchCreateRequest.FilterType, str]]] = ..., prev_kv: bool = ...) -> None: ...

class WatchProgressRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class WatchRequest(_message.Message):
    __slots__ = ["cancel_request", "create_request", "progress_request"]
    CANCEL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CREATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    cancel_request: WatchCancelRequest
    create_request: WatchCreateRequest
    progress_request: WatchProgressRequest
    def __init__(self, create_request: _Optional[_Union[WatchCreateRequest, _Mapping]] = ..., cancel_request: _Optional[_Union[WatchCancelRequest, _Mapping]] = ..., progress_request: _Optional[_Union[WatchProgressRequest, _Mapping]] = ...) -> None: ...

class WatchResponse(_message.Message):
    __slots__ = ["cancel_reason", "canceled", "compact_revision", "created", "events", "header", "watch_id"]
    CANCELED_FIELD_NUMBER: _ClassVar[int]
    CANCEL_REASON_FIELD_NUMBER: _ClassVar[int]
    COMPACT_REVISION_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    WATCH_ID_FIELD_NUMBER: _ClassVar[int]
    cancel_reason: str
    canceled: bool
    compact_revision: int
    created: bool
    events: _containers.RepeatedCompositeFieldContainer[_kv_pb2.Event]
    header: ResponseHeader
    watch_id: int
    def __init__(self, header: _Optional[_Union[ResponseHeader, _Mapping]] = ..., watch_id: _Optional[int] = ..., created: bool = ..., canceled: bool = ..., compact_revision: _Optional[int] = ..., cancel_reason: _Optional[str] = ..., events: _Optional[_Iterable[_Union[_kv_pb2.Event, _Mapping]]] = ...) -> None: ...

class AlarmType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
