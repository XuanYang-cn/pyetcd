import mock
from pyetcd.client import EtcdTokenCallCredentials

class TestEtcdTokenCallCredentials(object):
    def test_token_callback(self):
        e = EtcdTokenCallCredentials('foo')
        callback = mock.MagicMock()
        e(None, callback)
        metadata = (('token', 'foo'),)
        callback.assert_called_once_with(metadata, None)
