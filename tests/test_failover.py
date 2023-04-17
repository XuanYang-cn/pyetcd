import os
import pytest
import mock

import pyetcd


@pytest.mark.skipif(not os.environ.get('ETCDCTL_ENDPOINTS'),
                    reason="Expected etcd to have been run by pifpaf")
class TestFailoverClient(object):
    @pytest.fixture
    def etcd(self):
        endpoint_urls = os.environ.get('ETCDCTL_ENDPOINTS').split(',')
        timeout = 5
        endpoints = []
        for url in endpoint_urls:
            url = urlparse(url)
            endpoints.append(pyetcd.Endpoint(host=url.hostname,
                                            port=url.port,
                                            secure=False))
        with pyetcd.MultiEndpointEtcd3Client(endpoints=endpoints,
                                            timeout=timeout,
                                            failover=True) as client:
            yield client

        @retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
        def delete_keys_definitely():
            # clean up after fixture goes out of scope
            etcdctl('del', '--prefix', '/')
            out = etcdctl('get', '--prefix', '/')
            assert 'kvs' not in out

        delete_keys_definitely()

    def test_endpoint_offline(self, etcd):
        original_endpoint = etcd.endpoint_in_use
        assert not original_endpoint.is_failed()
        exception = Testpyetcd.MockedException(grpc.StatusCode.UNAVAILABLE)
        kv_mock = mock.PropertyMock()
        kv_mock.Range.side_effect = exception
        with mock.patch('pyetcd.MultiEndpointEtcd3Client.kvstub',
                        new_callable=mock.PropertyMock) as property_mock:
            property_mock.return_value = kv_mock
            with pytest.raises(pyetcd.exceptions.ConnectionFailedError):
                etcd.get("foo")
        assert etcd.endpoint_in_use is original_endpoint
        assert etcd.endpoint_in_use.is_failed()
        etcd.get("foo")
        assert etcd.endpoint_in_use is not original_endpoint
        assert not etcd.endpoint_in_use.is_failed()

    def test_failover_during_watch(self, etcd):
        class Interceptor(grpc.StreamStreamClientInterceptor):
            def intercept_stream_stream(self, continuation,
                                        client_call_details, request_iterator):
                response_iterator = continuation(client_call_details,
                                                 request_iterator)

                def new_iterator():
                    yield next(response_iterator)
                    with etcd.watcher._new_watch_cond:
                        while True:
                            etcd.watcher._new_watch_cond.wait()
                            if etcd.watcher._new_watch is None:
                                break
                    with response_iterator._state.condition:
                        response_iterator._state.code = \
                            grpc.StatusCode.UNAVAILABLE
                    yield next(response_iterator)
                return new_iterator()

        original_endpoint = etcd.endpoint_in_use
        assert not original_endpoint.is_failed()
        failing_channel = grpc.intercept_channel(original_endpoint.channel,
                                                 Interceptor())
        with mock.patch.object(original_endpoint, "channel", failing_channel):
            iterator, cancel = etcd.watch("foo")
            with pytest.raises(pyetcd.exceptions.ConnectionFailedError):
                next(iterator)
        assert etcd.endpoint_in_use is original_endpoint
        assert etcd.endpoint_in_use.is_failed()
        cancel()
        assert etcd.endpoint_in_use is not original_endpoint
        assert not etcd.endpoint_in_use.is_failed()
        iterator, cancel = etcd.watch("foo")
        etcd.put("foo", b"foo")
        assert next(iterator)
        cancel()
