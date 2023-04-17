import os
import pytest
import mock
import subprocess
import pyetcd
import grpc
from pyetcd import etcdrpc

def etcdctl(*args):
    endpoint = os.environ.get('PYTHON_ETCD_HTTP_URL')
    if endpoint:
        args = ['--endpoints', endpoint] + list(args)
    args = ['/tmp/etcd-download-test/etcdctl', '-w', 'json'] + list(args)
    process_output = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #  print(f"YX: etcdclt write: {process_output}")
    return process_output.stdout.decode('utf-8')

class TestClient:
    @pytest.fixture
    def etcd(self):
        yield pyetcd.client()

    def test_sort_target(self, etcd):
        key = 'key'.encode('utf-8')
        sort_target = {
            None: etcdrpc.RangeRequest.KEY,
            'key': etcdrpc.RangeRequest.KEY,
            'version': etcdrpc.RangeRequest.VERSION,
            'create': etcdrpc.RangeRequest.CREATE,
            'mod': etcdrpc.RangeRequest.MOD,
            'value': etcdrpc.RangeRequest.VALUE,
        }

        for input, expected in sort_target.items():
            range_request = etcd._build_get_range_request(key,
                                                          sort_target=input)
            assert range_request.sort_target == expected
        with pytest.raises(ValueError):
            etcd._build_get_range_request(key, sort_target='feelsbadman')

    def test_sort_order(self, etcd):
        key = 'key'.encode('utf-8')
        sort_target = {
            None: etcdrpc.RangeRequest.NONE,
            'ascend': etcdrpc.RangeRequest.ASCEND,
            'descend': etcdrpc.RangeRequest.DESCEND,
        }

        for input, expected in sort_target.items():
            range_request = etcd._build_get_range_request(key,
                                                          sort_order=input)
            assert range_request.sort_order == expected
        with pytest.raises(ValueError):
            etcd._build_get_range_request(key, sort_order='feelsbadman')

    def test_secure_channel(self):
        client = pyetcd.client(
            ca_cert="tests/ca.crt",
            cert_key="tests/client.key",
            cert_cert="tests/client.crt"
        )
        assert client.uses_secure_channel is True

    def test_secure_channel_ca_cert_only(self):
        client = pyetcd.client(
            ca_cert="tests/ca.crt",
            cert_key=None,
            cert_cert=None
        )
        assert client.uses_secure_channel is True

    def test_secure_channel_ca_cert_and_key_raise_exception(self):
        with pytest.raises(ValueError):
            pyetcd.client(
                ca_cert='tests/ca.crt',
                cert_key='tests/client.crt',
                cert_cert=None)

        with pytest.raises(ValueError):
            pyetcd.client(
                ca_cert='tests/ca.crt',
                cert_key=None,
                cert_cert='tests/client.crt')

    def test_compact(self, etcd):
        with pytest.raises(grpc.RpcError):
            etcd.compact(10000)

    def test_channel_with_no_cert(self):
        client = pyetcd.client(
            ca_cert=None,
            cert_key=None,
            cert_cert=None
        )
        assert client.uses_secure_channel is False

    @mock.patch('pyetcd.etcdrpc.AuthStub')
    def test_user_pwd_auth(self, auth_mock):
        auth_resp_mock = mock.MagicMock()
        auth_resp_mock.token = 'foo'
        auth_mock.Authenticate = auth_resp_mock
        self._enable_auth_in_etcd()

        # Create a client using username and password auth
        client = pyetcd.client(
            user='root',
            password='pwd'
        )

        assert client.call_credentials is not None
        self._disable_auth_in_etcd()

    def test_user_or_pwd_auth_raises_exception(self):
        with pytest.raises(Exception):
            pyetcd.client(user='usr')

        with pytest.raises(Exception):
            pyetcd.client(password='pwd')

    def _enable_auth_in_etcd(self):
        etcdctl(*['user', 'add', 'root:pwd'])
        etcdctl(*['auth', 'enable'])

    def _disable_auth_in_etcd(self):
        etcdctl(*['--user', 'root:pwd', 'auth', 'disable'])
        etcdctl(*['user', 'remove', 'root'])
