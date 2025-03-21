# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: rpc.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'rpc.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import kv_pb2 as kv__pb2
from . import auth_pb2 as auth__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\trpc.proto\x12\x0c\x65tcdserverpb\x1a\x08kv.proto\x1a\nauth.proto\"\\\n\x0eResponseHeader\x12\x12\n\ncluster_id\x18\x01 \x01(\x04\x12\x11\n\tmember_id\x18\x02 \x01(\x04\x12\x10\n\x08revision\x18\x03 \x01(\x03\x12\x11\n\traft_term\x18\x04 \x01(\x04\"\xe4\x03\n\x0cRangeRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x11\n\trange_end\x18\x02 \x01(\x0c\x12\r\n\x05limit\x18\x03 \x01(\x03\x12\x10\n\x08revision\x18\x04 \x01(\x03\x12\x38\n\nsort_order\x18\x05 \x01(\x0e\x32$.etcdserverpb.RangeRequest.SortOrder\x12:\n\x0bsort_target\x18\x06 \x01(\x0e\x32%.etcdserverpb.RangeRequest.SortTarget\x12\x14\n\x0cserializable\x18\x07 \x01(\x08\x12\x11\n\tkeys_only\x18\x08 \x01(\x08\x12\x12\n\ncount_only\x18\t \x01(\x08\x12\x18\n\x10min_mod_revision\x18\n \x01(\x03\x12\x18\n\x10max_mod_revision\x18\x0b \x01(\x03\x12\x1b\n\x13min_create_revision\x18\x0c \x01(\x03\x12\x1b\n\x13max_create_revision\x18\r \x01(\x03\".\n\tSortOrder\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06\x41SCEND\x10\x01\x12\x0b\n\x07\x44\x45SCEND\x10\x02\"B\n\nSortTarget\x12\x07\n\x03KEY\x10\x00\x12\x0b\n\x07VERSION\x10\x01\x12\n\n\x06\x43REATE\x10\x02\x12\x07\n\x03MOD\x10\x03\x12\t\n\x05VALUE\x10\x04\"y\n\rRangeResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\x1d\n\x03kvs\x18\x02 \x03(\x0b\x32\x10.mvccpb.KeyValue\x12\x0c\n\x04more\x18\x03 \x01(\x08\x12\r\n\x05\x63ount\x18\x04 \x01(\x03\"t\n\nPutRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\r\n\x05lease\x18\x03 \x01(\x03\x12\x0f\n\x07prev_kv\x18\x04 \x01(\x08\x12\x14\n\x0cignore_value\x18\x05 \x01(\x08\x12\x14\n\x0cignore_lease\x18\x06 \x01(\x08\"^\n\x0bPutResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12!\n\x07prev_kv\x18\x02 \x01(\x0b\x32\x10.mvccpb.KeyValue\"E\n\x12\x44\x65leteRangeRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x11\n\trange_end\x18\x02 \x01(\x0c\x12\x0f\n\x07prev_kv\x18\x03 \x01(\x08\"x\n\x13\x44\x65leteRangeResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\x0f\n\x07\x64\x65leted\x18\x02 \x01(\x03\x12\"\n\x08prev_kvs\x18\x03 \x03(\x0b\x32\x10.mvccpb.KeyValue\"\xef\x01\n\tRequestOp\x12\x33\n\rrequest_range\x18\x01 \x01(\x0b\x32\x1a.etcdserverpb.RangeRequestH\x00\x12/\n\x0brequest_put\x18\x02 \x01(\x0b\x32\x18.etcdserverpb.PutRequestH\x00\x12@\n\x14request_delete_range\x18\x03 \x01(\x0b\x32 .etcdserverpb.DeleteRangeRequestH\x00\x12/\n\x0brequest_txn\x18\x04 \x01(\x0b\x32\x18.etcdserverpb.TxnRequestH\x00\x42\t\n\x07request\"\xf9\x01\n\nResponseOp\x12\x35\n\x0eresponse_range\x18\x01 \x01(\x0b\x32\x1b.etcdserverpb.RangeResponseH\x00\x12\x31\n\x0cresponse_put\x18\x02 \x01(\x0b\x32\x19.etcdserverpb.PutResponseH\x00\x12\x42\n\x15response_delete_range\x18\x03 \x01(\x0b\x32!.etcdserverpb.DeleteRangeResponseH\x00\x12\x31\n\x0cresponse_txn\x18\x04 \x01(\x0b\x32\x19.etcdserverpb.TxnResponseH\x00\x42\n\n\x08response\"\x96\x03\n\x07\x43ompare\x12\x33\n\x06result\x18\x01 \x01(\x0e\x32#.etcdserverpb.Compare.CompareResult\x12\x33\n\x06target\x18\x02 \x01(\x0e\x32#.etcdserverpb.Compare.CompareTarget\x12\x0b\n\x03key\x18\x03 \x01(\x0c\x12\x11\n\x07version\x18\x04 \x01(\x03H\x00\x12\x19\n\x0f\x63reate_revision\x18\x05 \x01(\x03H\x00\x12\x16\n\x0cmod_revision\x18\x06 \x01(\x03H\x00\x12\x0f\n\x05value\x18\x07 \x01(\x0cH\x00\x12\x0f\n\x05lease\x18\x08 \x01(\x03H\x00\x12\x11\n\trange_end\x18@ \x01(\x0c\"@\n\rCompareResult\x12\t\n\x05\x45QUAL\x10\x00\x12\x0b\n\x07GREATER\x10\x01\x12\x08\n\x04LESS\x10\x02\x12\r\n\tNOT_EQUAL\x10\x03\"G\n\rCompareTarget\x12\x0b\n\x07VERSION\x10\x00\x12\n\n\x06\x43REATE\x10\x01\x12\x07\n\x03MOD\x10\x02\x12\t\n\x05VALUE\x10\x03\x12\t\n\x05LEASE\x10\x04\x42\x0e\n\x0ctarget_union\"\x88\x01\n\nTxnRequest\x12&\n\x07\x63ompare\x18\x01 \x03(\x0b\x32\x15.etcdserverpb.Compare\x12(\n\x07success\x18\x02 \x03(\x0b\x32\x17.etcdserverpb.RequestOp\x12(\n\x07\x66\x61ilure\x18\x03 \x03(\x0b\x32\x17.etcdserverpb.RequestOp\"{\n\x0bTxnResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\x11\n\tsucceeded\x18\x02 \x01(\x08\x12+\n\tresponses\x18\x03 \x03(\x0b\x32\x18.etcdserverpb.ResponseOp\"7\n\x11\x43ompactionRequest\x12\x10\n\x08revision\x18\x01 \x01(\x03\x12\x10\n\x08physical\x18\x02 \x01(\x08\"B\n\x12\x43ompactionResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\"\r\n\x0bHashRequest\"J\n\x0cHashResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\x0c\n\x04hash\x18\x02 \x01(\r\"!\n\rHashKVRequest\x12\x10\n\x08revision\x18\x01 \x01(\x03\"f\n\x0eHashKVResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\x0c\n\x04hash\x18\x02 \x01(\r\x12\x18\n\x10\x63ompact_revision\x18\x03 \x01(\x03\"\x11\n\x0fSnapshotRequest\"g\n\x10SnapshotResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\x17\n\x0fremaining_bytes\x18\x02 \x01(\x04\x12\x0c\n\x04\x62lob\x18\x03 \x01(\x0c\"\xd7\x01\n\x0cWatchRequest\x12:\n\x0e\x63reate_request\x18\x01 \x01(\x0b\x32 .etcdserverpb.WatchCreateRequestH\x00\x12:\n\x0e\x63\x61ncel_request\x18\x02 \x01(\x0b\x32 .etcdserverpb.WatchCancelRequestH\x00\x12>\n\x10progress_request\x18\x03 \x01(\x0b\x32\".etcdserverpb.WatchProgressRequestH\x00\x42\x0f\n\rrequest_union\"\xdb\x01\n\x12WatchCreateRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x11\n\trange_end\x18\x02 \x01(\x0c\x12\x16\n\x0estart_revision\x18\x03 \x01(\x03\x12\x17\n\x0fprogress_notify\x18\x04 \x01(\x08\x12<\n\x07\x66ilters\x18\x05 \x03(\x0e\x32+.etcdserverpb.WatchCreateRequest.FilterType\x12\x0f\n\x07prev_kv\x18\x06 \x01(\x08\"%\n\nFilterType\x12\t\n\x05NOPUT\x10\x00\x12\x0c\n\x08NODELETE\x10\x01\"&\n\x12WatchCancelRequest\x12\x10\n\x08watch_id\x18\x01 \x01(\x03\"\x16\n\x14WatchProgressRequest\"\xc2\x01\n\rWatchResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\x10\n\x08watch_id\x18\x02 \x01(\x03\x12\x0f\n\x07\x63reated\x18\x03 \x01(\x08\x12\x10\n\x08\x63\x61nceled\x18\x04 \x01(\x08\x12\x18\n\x10\x63ompact_revision\x18\x05 \x01(\x03\x12\x15\n\rcancel_reason\x18\x06 \x01(\t\x12\x1d\n\x06\x65vents\x18\x0b \x03(\x0b\x32\r.mvccpb.Event\",\n\x11LeaseGrantRequest\x12\x0b\n\x03TTL\x18\x01 \x01(\x03\x12\n\n\x02ID\x18\x02 \x01(\x03\"j\n\x12LeaseGrantResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\n\n\x02ID\x18\x02 \x01(\x03\x12\x0b\n\x03TTL\x18\x03 \x01(\x03\x12\r\n\x05\x65rror\x18\x04 \x01(\t\" \n\x12LeaseRevokeRequest\x12\n\n\x02ID\x18\x01 \x01(\x03\"C\n\x13LeaseRevokeResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\"#\n\x15LeaseKeepAliveRequest\x12\n\n\x02ID\x18\x01 \x01(\x03\"_\n\x16LeaseKeepAliveResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\n\n\x02ID\x18\x02 \x01(\x03\x12\x0b\n\x03TTL\x18\x03 \x01(\x03\"2\n\x16LeaseTimeToLiveRequest\x12\n\n\x02ID\x18\x01 \x01(\x03\x12\x0c\n\x04keys\x18\x02 \x01(\x08\"\x82\x01\n\x17LeaseTimeToLiveResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\n\n\x02ID\x18\x02 \x01(\x03\x12\x0b\n\x03TTL\x18\x03 \x01(\x03\x12\x12\n\ngrantedTTL\x18\x04 \x01(\x03\x12\x0c\n\x04keys\x18\x05 \x03(\x0c\"H\n\x06Member\x12\n\n\x02ID\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08peerURLs\x18\x03 \x03(\t\x12\x12\n\nclientURLs\x18\x04 \x03(\t\"$\n\x10MemberAddRequest\x12\x10\n\x08peerURLs\x18\x01 \x03(\t\"\x8e\x01\n\x11MemberAddResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12$\n\x06member\x18\x02 \x01(\x0b\x32\x14.etcdserverpb.Member\x12%\n\x07members\x18\x03 \x03(\x0b\x32\x14.etcdserverpb.Member\"!\n\x13MemberRemoveRequest\x12\n\n\x02ID\x18\x01 \x01(\x04\"k\n\x14MemberRemoveResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12%\n\x07members\x18\x02 \x03(\x0b\x32\x14.etcdserverpb.Member\"3\n\x13MemberUpdateRequest\x12\n\n\x02ID\x18\x01 \x01(\x04\x12\x10\n\x08peerURLs\x18\x02 \x03(\t\"k\n\x14MemberUpdateResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12%\n\x07members\x18\x02 \x03(\x0b\x32\x14.etcdserverpb.Member\"\x13\n\x11MemberListRequest\"i\n\x12MemberListResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12%\n\x07members\x18\x02 \x03(\x0b\x32\x14.etcdserverpb.Member\"\x13\n\x11\x44\x65\x66ragmentRequest\"B\n\x12\x44\x65\x66ragmentResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\"%\n\x11MoveLeaderRequest\x12\x10\n\x08targetID\x18\x01 \x01(\x04\"B\n\x12MoveLeaderResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\"\xb6\x01\n\x0c\x41larmRequest\x12\x36\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32&.etcdserverpb.AlarmRequest.AlarmAction\x12\x10\n\x08memberID\x18\x02 \x01(\x04\x12&\n\x05\x61larm\x18\x03 \x01(\x0e\x32\x17.etcdserverpb.AlarmType\"4\n\x0b\x41larmAction\x12\x07\n\x03GET\x10\x00\x12\x0c\n\x08\x41\x43TIVATE\x10\x01\x12\x0e\n\nDEACTIVATE\x10\x02\"G\n\x0b\x41larmMember\x12\x10\n\x08memberID\x18\x01 \x01(\x04\x12&\n\x05\x61larm\x18\x02 \x01(\x0e\x32\x17.etcdserverpb.AlarmType\"h\n\rAlarmResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12)\n\x06\x61larms\x18\x02 \x03(\x0b\x32\x19.etcdserverpb.AlarmMember\"\x0f\n\rStatusRequest\"\x94\x01\n\x0eStatusResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x62Size\x18\x03 \x01(\x03\x12\x0e\n\x06leader\x18\x04 \x01(\x04\x12\x11\n\traftIndex\x18\x05 \x01(\x04\x12\x10\n\x08raftTerm\x18\x06 \x01(\x04\"\x13\n\x11\x41uthEnableRequest\"\x14\n\x12\x41uthDisableRequest\"5\n\x13\x41uthenticateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"4\n\x12\x41uthUserAddRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\"\n\x12\x41uthUserGetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"%\n\x15\x41uthUserDeleteRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"?\n\x1d\x41uthUserChangePasswordRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"6\n\x18\x41uthUserGrantRoleRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0c\n\x04role\x18\x02 \x01(\t\"7\n\x19\x41uthUserRevokeRoleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04role\x18\x02 \x01(\t\"\"\n\x12\x41uthRoleAddRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\"\n\x12\x41uthRoleGetRequest\x12\x0c\n\x04role\x18\x01 \x01(\t\"\x15\n\x13\x41uthUserListRequest\"\x15\n\x13\x41uthRoleListRequest\"%\n\x15\x41uthRoleDeleteRequest\x12\x0c\n\x04role\x18\x01 \x01(\t\"P\n\x1e\x41uthRoleGrantPermissionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12 \n\x04perm\x18\x02 \x01(\x0b\x32\x12.authpb.Permission\"O\n\x1f\x41uthRoleRevokePermissionRequest\x12\x0c\n\x04role\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x11\n\trange_end\x18\x03 \x01(\t\"B\n\x12\x41uthEnableResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\"C\n\x13\x41uthDisableResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\"S\n\x14\x41uthenticateResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\r\n\x05token\x18\x02 \x01(\t\"C\n\x13\x41uthUserAddResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\"R\n\x13\x41uthUserGetResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\r\n\x05roles\x18\x02 \x03(\t\"F\n\x16\x41uthUserDeleteResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\"N\n\x1e\x41uthUserChangePasswordResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\"I\n\x19\x41uthUserGrantRoleResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\"J\n\x1a\x41uthUserRevokeRoleResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\"C\n\x13\x41uthRoleAddResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\"e\n\x13\x41uthRoleGetResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12 \n\x04perm\x18\x02 \x03(\x0b\x32\x12.authpb.Permission\"S\n\x14\x41uthRoleListResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\r\n\x05roles\x18\x02 \x03(\t\"S\n\x14\x41uthUserListResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\r\n\x05users\x18\x02 \x03(\t\"F\n\x16\x41uthRoleDeleteResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\"O\n\x1f\x41uthRoleGrantPermissionResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\"P\n AuthRoleRevokePermissionResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader*\"\n\tAlarmType\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07NOSPACE\x10\x01\x32\xea\x02\n\x02KV\x12\x42\n\x05Range\x12\x1a.etcdserverpb.RangeRequest\x1a\x1b.etcdserverpb.RangeResponse\"\x00\x12<\n\x03Put\x12\x18.etcdserverpb.PutRequest\x1a\x19.etcdserverpb.PutResponse\"\x00\x12T\n\x0b\x44\x65leteRange\x12 .etcdserverpb.DeleteRangeRequest\x1a!.etcdserverpb.DeleteRangeResponse\"\x00\x12<\n\x03Txn\x12\x18.etcdserverpb.TxnRequest\x1a\x19.etcdserverpb.TxnResponse\"\x00\x12N\n\x07\x43ompact\x12\x1f.etcdserverpb.CompactionRequest\x1a .etcdserverpb.CompactionResponse\"\x00\x32\x9e\x01\n\x05Watch\x12M\n\x08Progress\x12\".etcdserverpb.WatchProgressRequest\x1a\x1b.etcdserverpb.WatchResponse\"\x00\x12\x46\n\x05Watch\x12\x1a.etcdserverpb.WatchRequest\x1a\x1b.etcdserverpb.WatchResponse\"\x00(\x01\x30\x01\x32\xf5\x02\n\x05Lease\x12Q\n\nLeaseGrant\x12\x1f.etcdserverpb.LeaseGrantRequest\x1a .etcdserverpb.LeaseGrantResponse\"\x00\x12T\n\x0bLeaseRevoke\x12 .etcdserverpb.LeaseRevokeRequest\x1a!.etcdserverpb.LeaseRevokeResponse\"\x00\x12\x61\n\x0eLeaseKeepAlive\x12#.etcdserverpb.LeaseKeepAliveRequest\x1a$.etcdserverpb.LeaseKeepAliveResponse\"\x00(\x01\x30\x01\x12`\n\x0fLeaseTimeToLive\x12$.etcdserverpb.LeaseTimeToLiveRequest\x1a%.etcdserverpb.LeaseTimeToLiveResponse\"\x00\x32\xde\x02\n\x07\x43luster\x12N\n\tMemberAdd\x12\x1e.etcdserverpb.MemberAddRequest\x1a\x1f.etcdserverpb.MemberAddResponse\"\x00\x12W\n\x0cMemberRemove\x12!.etcdserverpb.MemberRemoveRequest\x1a\".etcdserverpb.MemberRemoveResponse\"\x00\x12W\n\x0cMemberUpdate\x12!.etcdserverpb.MemberUpdateRequest\x1a\".etcdserverpb.MemberUpdateResponse\"\x00\x12Q\n\nMemberList\x12\x1f.etcdserverpb.MemberListRequest\x1a .etcdserverpb.MemberListResponse\"\x00\x32\x95\x04\n\x0bMaintenance\x12\x42\n\x05\x41larm\x12\x1a.etcdserverpb.AlarmRequest\x1a\x1b.etcdserverpb.AlarmResponse\"\x00\x12\x45\n\x06Status\x12\x1b.etcdserverpb.StatusRequest\x1a\x1c.etcdserverpb.StatusResponse\"\x00\x12Q\n\nDefragment\x12\x1f.etcdserverpb.DefragmentRequest\x1a .etcdserverpb.DefragmentResponse\"\x00\x12?\n\x04Hash\x12\x19.etcdserverpb.HashRequest\x1a\x1a.etcdserverpb.HashResponse\"\x00\x12\x45\n\x06HashKV\x12\x1b.etcdserverpb.HashKVRequest\x1a\x1c.etcdserverpb.HashKVResponse\"\x00\x12M\n\x08Snapshot\x12\x1d.etcdserverpb.SnapshotRequest\x1a\x1e.etcdserverpb.SnapshotResponse\"\x00\x30\x01\x12Q\n\nMoveLeader\x12\x1f.etcdserverpb.MoveLeaderRequest\x1a .etcdserverpb.MoveLeaderResponse\"\x00\x32\xdd\x0b\n\x04\x41uth\x12Q\n\nAuthEnable\x12\x1f.etcdserverpb.AuthEnableRequest\x1a .etcdserverpb.AuthEnableResponse\"\x00\x12T\n\x0b\x41uthDisable\x12 .etcdserverpb.AuthDisableRequest\x1a!.etcdserverpb.AuthDisableResponse\"\x00\x12W\n\x0c\x41uthenticate\x12!.etcdserverpb.AuthenticateRequest\x1a\".etcdserverpb.AuthenticateResponse\"\x00\x12P\n\x07UserAdd\x12 .etcdserverpb.AuthUserAddRequest\x1a!.etcdserverpb.AuthUserAddResponse\"\x00\x12P\n\x07UserGet\x12 .etcdserverpb.AuthUserGetRequest\x1a!.etcdserverpb.AuthUserGetResponse\"\x00\x12S\n\x08UserList\x12!.etcdserverpb.AuthUserListRequest\x1a\".etcdserverpb.AuthUserListResponse\"\x00\x12Y\n\nUserDelete\x12#.etcdserverpb.AuthUserDeleteRequest\x1a$.etcdserverpb.AuthUserDeleteResponse\"\x00\x12q\n\x12UserChangePassword\x12+.etcdserverpb.AuthUserChangePasswordRequest\x1a,.etcdserverpb.AuthUserChangePasswordResponse\"\x00\x12\x62\n\rUserGrantRole\x12&.etcdserverpb.AuthUserGrantRoleRequest\x1a\'.etcdserverpb.AuthUserGrantRoleResponse\"\x00\x12\x65\n\x0eUserRevokeRole\x12\'.etcdserverpb.AuthUserRevokeRoleRequest\x1a(.etcdserverpb.AuthUserRevokeRoleResponse\"\x00\x12P\n\x07RoleAdd\x12 .etcdserverpb.AuthRoleAddRequest\x1a!.etcdserverpb.AuthRoleAddResponse\"\x00\x12P\n\x07RoleGet\x12 .etcdserverpb.AuthRoleGetRequest\x1a!.etcdserverpb.AuthRoleGetResponse\"\x00\x12S\n\x08RoleList\x12!.etcdserverpb.AuthRoleListRequest\x1a\".etcdserverpb.AuthRoleListResponse\"\x00\x12Y\n\nRoleDelete\x12#.etcdserverpb.AuthRoleDeleteRequest\x1a$.etcdserverpb.AuthRoleDeleteResponse\"\x00\x12t\n\x13RoleGrantPermission\x12,.etcdserverpb.AuthRoleGrantPermissionRequest\x1a-.etcdserverpb.AuthRoleGrantPermissionResponse\"\x00\x12w\n\x14RoleRevokePermission\x12-.etcdserverpb.AuthRoleRevokePermissionRequest\x1a..etcdserverpb.AuthRoleRevokePermissionResponse\"\x00\x42)\n\x11io.etcd.jetcd.apiB\nJetcdProtoP\x01\xa2\x02\x05Jetcdb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021io.etcd.jetcd.apiB\nJetcdProtoP\001\242\002\005Jetcd'
  _globals['_ALARMTYPE']._serialized_start=7482
  _globals['_ALARMTYPE']._serialized_end=7516
  _globals['_RESPONSEHEADER']._serialized_start=49
  _globals['_RESPONSEHEADER']._serialized_end=141
  _globals['_RANGEREQUEST']._serialized_start=144
  _globals['_RANGEREQUEST']._serialized_end=628
  _globals['_RANGEREQUEST_SORTORDER']._serialized_start=514
  _globals['_RANGEREQUEST_SORTORDER']._serialized_end=560
  _globals['_RANGEREQUEST_SORTTARGET']._serialized_start=562
  _globals['_RANGEREQUEST_SORTTARGET']._serialized_end=628
  _globals['_RANGERESPONSE']._serialized_start=630
  _globals['_RANGERESPONSE']._serialized_end=751
  _globals['_PUTREQUEST']._serialized_start=753
  _globals['_PUTREQUEST']._serialized_end=869
  _globals['_PUTRESPONSE']._serialized_start=871
  _globals['_PUTRESPONSE']._serialized_end=965
  _globals['_DELETERANGEREQUEST']._serialized_start=967
  _globals['_DELETERANGEREQUEST']._serialized_end=1036
  _globals['_DELETERANGERESPONSE']._serialized_start=1038
  _globals['_DELETERANGERESPONSE']._serialized_end=1158
  _globals['_REQUESTOP']._serialized_start=1161
  _globals['_REQUESTOP']._serialized_end=1400
  _globals['_RESPONSEOP']._serialized_start=1403
  _globals['_RESPONSEOP']._serialized_end=1652
  _globals['_COMPARE']._serialized_start=1655
  _globals['_COMPARE']._serialized_end=2061
  _globals['_COMPARE_COMPARERESULT']._serialized_start=1908
  _globals['_COMPARE_COMPARERESULT']._serialized_end=1972
  _globals['_COMPARE_COMPARETARGET']._serialized_start=1974
  _globals['_COMPARE_COMPARETARGET']._serialized_end=2045
  _globals['_TXNREQUEST']._serialized_start=2064
  _globals['_TXNREQUEST']._serialized_end=2200
  _globals['_TXNRESPONSE']._serialized_start=2202
  _globals['_TXNRESPONSE']._serialized_end=2325
  _globals['_COMPACTIONREQUEST']._serialized_start=2327
  _globals['_COMPACTIONREQUEST']._serialized_end=2382
  _globals['_COMPACTIONRESPONSE']._serialized_start=2384
  _globals['_COMPACTIONRESPONSE']._serialized_end=2450
  _globals['_HASHREQUEST']._serialized_start=2452
  _globals['_HASHREQUEST']._serialized_end=2465
  _globals['_HASHRESPONSE']._serialized_start=2467
  _globals['_HASHRESPONSE']._serialized_end=2541
  _globals['_HASHKVREQUEST']._serialized_start=2543
  _globals['_HASHKVREQUEST']._serialized_end=2576
  _globals['_HASHKVRESPONSE']._serialized_start=2578
  _globals['_HASHKVRESPONSE']._serialized_end=2680
  _globals['_SNAPSHOTREQUEST']._serialized_start=2682
  _globals['_SNAPSHOTREQUEST']._serialized_end=2699
  _globals['_SNAPSHOTRESPONSE']._serialized_start=2701
  _globals['_SNAPSHOTRESPONSE']._serialized_end=2804
  _globals['_WATCHREQUEST']._serialized_start=2807
  _globals['_WATCHREQUEST']._serialized_end=3022
  _globals['_WATCHCREATEREQUEST']._serialized_start=3025
  _globals['_WATCHCREATEREQUEST']._serialized_end=3244
  _globals['_WATCHCREATEREQUEST_FILTERTYPE']._serialized_start=3207
  _globals['_WATCHCREATEREQUEST_FILTERTYPE']._serialized_end=3244
  _globals['_WATCHCANCELREQUEST']._serialized_start=3246
  _globals['_WATCHCANCELREQUEST']._serialized_end=3284
  _globals['_WATCHPROGRESSREQUEST']._serialized_start=3286
  _globals['_WATCHPROGRESSREQUEST']._serialized_end=3308
  _globals['_WATCHRESPONSE']._serialized_start=3311
  _globals['_WATCHRESPONSE']._serialized_end=3505
  _globals['_LEASEGRANTREQUEST']._serialized_start=3507
  _globals['_LEASEGRANTREQUEST']._serialized_end=3551
  _globals['_LEASEGRANTRESPONSE']._serialized_start=3553
  _globals['_LEASEGRANTRESPONSE']._serialized_end=3659
  _globals['_LEASEREVOKEREQUEST']._serialized_start=3661
  _globals['_LEASEREVOKEREQUEST']._serialized_end=3693
  _globals['_LEASEREVOKERESPONSE']._serialized_start=3695
  _globals['_LEASEREVOKERESPONSE']._serialized_end=3762
  _globals['_LEASEKEEPALIVEREQUEST']._serialized_start=3764
  _globals['_LEASEKEEPALIVEREQUEST']._serialized_end=3799
  _globals['_LEASEKEEPALIVERESPONSE']._serialized_start=3801
  _globals['_LEASEKEEPALIVERESPONSE']._serialized_end=3896
  _globals['_LEASETIMETOLIVEREQUEST']._serialized_start=3898
  _globals['_LEASETIMETOLIVEREQUEST']._serialized_end=3948
  _globals['_LEASETIMETOLIVERESPONSE']._serialized_start=3951
  _globals['_LEASETIMETOLIVERESPONSE']._serialized_end=4081
  _globals['_MEMBER']._serialized_start=4083
  _globals['_MEMBER']._serialized_end=4155
  _globals['_MEMBERADDREQUEST']._serialized_start=4157
  _globals['_MEMBERADDREQUEST']._serialized_end=4193
  _globals['_MEMBERADDRESPONSE']._serialized_start=4196
  _globals['_MEMBERADDRESPONSE']._serialized_end=4338
  _globals['_MEMBERREMOVEREQUEST']._serialized_start=4340
  _globals['_MEMBERREMOVEREQUEST']._serialized_end=4373
  _globals['_MEMBERREMOVERESPONSE']._serialized_start=4375
  _globals['_MEMBERREMOVERESPONSE']._serialized_end=4482
  _globals['_MEMBERUPDATEREQUEST']._serialized_start=4484
  _globals['_MEMBERUPDATEREQUEST']._serialized_end=4535
  _globals['_MEMBERUPDATERESPONSE']._serialized_start=4537
  _globals['_MEMBERUPDATERESPONSE']._serialized_end=4644
  _globals['_MEMBERLISTREQUEST']._serialized_start=4646
  _globals['_MEMBERLISTREQUEST']._serialized_end=4665
  _globals['_MEMBERLISTRESPONSE']._serialized_start=4667
  _globals['_MEMBERLISTRESPONSE']._serialized_end=4772
  _globals['_DEFRAGMENTREQUEST']._serialized_start=4774
  _globals['_DEFRAGMENTREQUEST']._serialized_end=4793
  _globals['_DEFRAGMENTRESPONSE']._serialized_start=4795
  _globals['_DEFRAGMENTRESPONSE']._serialized_end=4861
  _globals['_MOVELEADERREQUEST']._serialized_start=4863
  _globals['_MOVELEADERREQUEST']._serialized_end=4900
  _globals['_MOVELEADERRESPONSE']._serialized_start=4902
  _globals['_MOVELEADERRESPONSE']._serialized_end=4968
  _globals['_ALARMREQUEST']._serialized_start=4971
  _globals['_ALARMREQUEST']._serialized_end=5153
  _globals['_ALARMREQUEST_ALARMACTION']._serialized_start=5101
  _globals['_ALARMREQUEST_ALARMACTION']._serialized_end=5153
  _globals['_ALARMMEMBER']._serialized_start=5155
  _globals['_ALARMMEMBER']._serialized_end=5226
  _globals['_ALARMRESPONSE']._serialized_start=5228
  _globals['_ALARMRESPONSE']._serialized_end=5332
  _globals['_STATUSREQUEST']._serialized_start=5334
  _globals['_STATUSREQUEST']._serialized_end=5349
  _globals['_STATUSRESPONSE']._serialized_start=5352
  _globals['_STATUSRESPONSE']._serialized_end=5500
  _globals['_AUTHENABLEREQUEST']._serialized_start=5502
  _globals['_AUTHENABLEREQUEST']._serialized_end=5521
  _globals['_AUTHDISABLEREQUEST']._serialized_start=5523
  _globals['_AUTHDISABLEREQUEST']._serialized_end=5543
  _globals['_AUTHENTICATEREQUEST']._serialized_start=5545
  _globals['_AUTHENTICATEREQUEST']._serialized_end=5598
  _globals['_AUTHUSERADDREQUEST']._serialized_start=5600
  _globals['_AUTHUSERADDREQUEST']._serialized_end=5652
  _globals['_AUTHUSERGETREQUEST']._serialized_start=5654
  _globals['_AUTHUSERGETREQUEST']._serialized_end=5688
  _globals['_AUTHUSERDELETEREQUEST']._serialized_start=5690
  _globals['_AUTHUSERDELETEREQUEST']._serialized_end=5727
  _globals['_AUTHUSERCHANGEPASSWORDREQUEST']._serialized_start=5729
  _globals['_AUTHUSERCHANGEPASSWORDREQUEST']._serialized_end=5792
  _globals['_AUTHUSERGRANTROLEREQUEST']._serialized_start=5794
  _globals['_AUTHUSERGRANTROLEREQUEST']._serialized_end=5848
  _globals['_AUTHUSERREVOKEROLEREQUEST']._serialized_start=5850
  _globals['_AUTHUSERREVOKEROLEREQUEST']._serialized_end=5905
  _globals['_AUTHROLEADDREQUEST']._serialized_start=5907
  _globals['_AUTHROLEADDREQUEST']._serialized_end=5941
  _globals['_AUTHROLEGETREQUEST']._serialized_start=5943
  _globals['_AUTHROLEGETREQUEST']._serialized_end=5977
  _globals['_AUTHUSERLISTREQUEST']._serialized_start=5979
  _globals['_AUTHUSERLISTREQUEST']._serialized_end=6000
  _globals['_AUTHROLELISTREQUEST']._serialized_start=6002
  _globals['_AUTHROLELISTREQUEST']._serialized_end=6023
  _globals['_AUTHROLEDELETEREQUEST']._serialized_start=6025
  _globals['_AUTHROLEDELETEREQUEST']._serialized_end=6062
  _globals['_AUTHROLEGRANTPERMISSIONREQUEST']._serialized_start=6064
  _globals['_AUTHROLEGRANTPERMISSIONREQUEST']._serialized_end=6144
  _globals['_AUTHROLEREVOKEPERMISSIONREQUEST']._serialized_start=6146
  _globals['_AUTHROLEREVOKEPERMISSIONREQUEST']._serialized_end=6225
  _globals['_AUTHENABLERESPONSE']._serialized_start=6227
  _globals['_AUTHENABLERESPONSE']._serialized_end=6293
  _globals['_AUTHDISABLERESPONSE']._serialized_start=6295
  _globals['_AUTHDISABLERESPONSE']._serialized_end=6362
  _globals['_AUTHENTICATERESPONSE']._serialized_start=6364
  _globals['_AUTHENTICATERESPONSE']._serialized_end=6447
  _globals['_AUTHUSERADDRESPONSE']._serialized_start=6449
  _globals['_AUTHUSERADDRESPONSE']._serialized_end=6516
  _globals['_AUTHUSERGETRESPONSE']._serialized_start=6518
  _globals['_AUTHUSERGETRESPONSE']._serialized_end=6600
  _globals['_AUTHUSERDELETERESPONSE']._serialized_start=6602
  _globals['_AUTHUSERDELETERESPONSE']._serialized_end=6672
  _globals['_AUTHUSERCHANGEPASSWORDRESPONSE']._serialized_start=6674
  _globals['_AUTHUSERCHANGEPASSWORDRESPONSE']._serialized_end=6752
  _globals['_AUTHUSERGRANTROLERESPONSE']._serialized_start=6754
  _globals['_AUTHUSERGRANTROLERESPONSE']._serialized_end=6827
  _globals['_AUTHUSERREVOKEROLERESPONSE']._serialized_start=6829
  _globals['_AUTHUSERREVOKEROLERESPONSE']._serialized_end=6903
  _globals['_AUTHROLEADDRESPONSE']._serialized_start=6905
  _globals['_AUTHROLEADDRESPONSE']._serialized_end=6972
  _globals['_AUTHROLEGETRESPONSE']._serialized_start=6974
  _globals['_AUTHROLEGETRESPONSE']._serialized_end=7075
  _globals['_AUTHROLELISTRESPONSE']._serialized_start=7077
  _globals['_AUTHROLELISTRESPONSE']._serialized_end=7160
  _globals['_AUTHUSERLISTRESPONSE']._serialized_start=7162
  _globals['_AUTHUSERLISTRESPONSE']._serialized_end=7245
  _globals['_AUTHROLEDELETERESPONSE']._serialized_start=7247
  _globals['_AUTHROLEDELETERESPONSE']._serialized_end=7317
  _globals['_AUTHROLEGRANTPERMISSIONRESPONSE']._serialized_start=7319
  _globals['_AUTHROLEGRANTPERMISSIONRESPONSE']._serialized_end=7398
  _globals['_AUTHROLEREVOKEPERMISSIONRESPONSE']._serialized_start=7400
  _globals['_AUTHROLEREVOKEPERMISSIONRESPONSE']._serialized_end=7480
  _globals['_KV']._serialized_start=7519
  _globals['_KV']._serialized_end=7881
  _globals['_WATCH']._serialized_start=7884
  _globals['_WATCH']._serialized_end=8042
  _globals['_LEASE']._serialized_start=8045
  _globals['_LEASE']._serialized_end=8418
  _globals['_CLUSTER']._serialized_start=8421
  _globals['_CLUSTER']._serialized_end=8771
  _globals['_MAINTENANCE']._serialized_start=8774
  _globals['_MAINTENANCE']._serialized_end=9307
  _globals['_AUTH']._serialized_start=9310
  _globals['_AUTH']._serialized_end=10811
# @@protoc_insertion_point(module_scope)
