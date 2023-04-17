import base64
import json
import os
import signal
#  import string
import subprocess
import tempfile
import threading
import time

from contextlib import contextmanager
import grpc

from hypothesis import given, settings
from hypothesis.strategies import characters

import mock

import pytest

from urllib.parse import urlparse

from tenacity import retry, stop_after_attempt, wait_fixed

import pyetcd
import pyetcd.etcdrpc as etcdrpc
import pyetcd.exceptions
import pyetcd.utils as utils
from pyetcd.client import EtcdTokenCallCredentials

etcd_version = os.environ.get('TEST_ETCD_VERSION', 'v3.5.5')
def etcdctl(*args):
    endpoint = os.environ.get('PYTHON_ETCD_HTTP_URL')
    if endpoint:
        args = ['--endpoints', endpoint] + list(args)
    args = ['/tmp/etcd-download-test/etcdctl', '-w', 'json'] + list(args)
    process_output = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return process_output.stdout.decode('utf-8')

@contextmanager
def _out_quorum():
    pids = subprocess.check_output(['pgrep', '-f', 'pifpaf[12]'])
    pids = [int(pid.strip()) for pid in pids.splitlines()]
    try:
        for pid in pids:
            os.kill(pid, signal.SIGSTOP)
        yield
    finally:
        for pid in pids:
            os.kill(pid, signal.SIGCONT)

class TestPyEtcd(object):

    class MockedException(grpc.RpcError):
        def __init__(self, code):
            self._code = code

        def code(self):
            return self._code

    @contextmanager
    def get_clean_etcd(self):
        endpoint = os.environ.get('PYTHON_ETCD_HTTP_URL')
        timeout = 5
        if endpoint:
            url = urlparse(endpoint)
            with pyetcd.client(host=url.hostname,
                              port=url.port,
                              timeout=timeout) as client:
                yield client
        else:
            with pyetcd.client() as client:
                yield client

        @retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
        def delete_keys_definitely():
            # clean up after fixture goes out of scope
            etcdctl('del', '--prefix', '/')
            out = etcdctl('get', '--prefix', '/')
            assert 'kvs' not in out

        delete_keys_definitely()

    @pytest.fixture
    def etcd(self):
        with self.get_clean_etcd() as etcd:
            yield etcd

    def test_get_unknown_key(self, etcd):
        value, meta = etcd.get('probably-invalid-key')
        assert value is None
        assert meta is None

    @given(characters(blacklist_categories=['Cs', 'Cc']))
    def test_get_key(self, string):
        with self.get_clean_etcd() as etcd:
            etcdctl('put', '/doot/a_key', string)
            returned, _ = etcd.get('/doot/a_key')
            assert returned == string.encode()

    @given(characters(blacklist_categories=['Cs', 'Cc']))
    def test_get_random_key(self, string):
        with self.get_clean_etcd() as etcd:
            etcdctl('put', '/doot/' + string, 'dootdoot')
            returned, _ = etcd.get('/doot/' + string)
            assert returned == b'dootdoot'

    @given(
        characters(blacklist_categories=['Cs', 'Cc']),
        characters(blacklist_categories=['Cs', 'Cc']),
    )
    @pytest.mark.skipif(not os.environ.get('ETCDCTL_ENDPOINTS'),
                        reason="Expected etcd to have been run by pifpaf")
    def test_get_key_serializable(self, key, string):
        with self.get_clean_etcd() as etcd:
            etcdctl('put', '/doot/' + key, string)
            with _out_quorum():
                returned, _ = etcd.get('/doot/' + key, serializable=True)
            assert returned == string.encode('utf-8')

    @given(characters(blacklist_categories=['Cs', 'Cc']))
    def test_get_have_cluster_revision(self, string):
        with self.get_clean_etcd() as etcd:
            etcdctl('put', '/doot/' + string, 'dootdoot')
            _, md = etcd.get('/doot/' + string)
            assert md.response_header.revision > 0

    #  @given(characters(blacklist_categories=['Cs', 'Cc']))
    @pytest.mark.parametrize("string", ["a", "b", "abc"])
    def test_put_key(self, string):
        with self.get_clean_etcd() as etcd:
            etcd.put('/doot/put_1', string)
            out = etcdctl('get', '/doot/put_1')
            out = json.loads(out)
            assert base64.b64decode(out['kvs'][0]['value']) == string.encode()

    @given(characters(blacklist_categories=['Cs', 'Cc']))
    def test_put_has_cluster_revision(self, string):
        with self.get_clean_etcd() as etcd:
            response = etcd.put('/doot/put_1', string)
            assert response.header.revision > 0

    @given(characters(blacklist_categories=['Cs', 'Cc']))
    def test_put_has_prev_kv(self, string):
        with self.get_clean_etcd() as etcd:
            etcdctl('put', '/doot/put_1', 'old_value')
            response = etcd.put('/doot/put_1', string, prev_kv=True)
            assert response.prev_kv.value == b'old_value'

    @given(characters(blacklist_categories=['Cs', 'Cc']))
    def test_put_if_not_exists(self, string):
        with self.get_clean_etcd() as etcd:
            txn_status = etcd.put_if_not_exists('/doot/put_1', string)
            assert txn_status is True

            txn_status = etcd.put_if_not_exists('/doot/put_1', string)
            assert txn_status is False

            etcdctl('del', '/doot/put_1')

    def test_delete_key(self, etcd):
        etcdctl('put', '/doot/delete_this', 'delete pls')

        v, _ = etcd.get('/doot/delete_this')
        assert v == b'delete pls'

        deleted = etcd.delete('/doot/delete_this')
        assert deleted is True

        deleted = etcd.delete('/doot/delete_this')
        assert deleted is False

        deleted = etcd.delete('/doot/not_here_dude')
        assert deleted is False

        v, _ = etcd.get('/doot/delete_this')
        assert v is None

    def test_delete_has_cluster_revision(self, etcd):
        response = etcd.delete('/doot/delete_this', return_response=True)
        assert response.header.revision > 0

    def test_delete_has_prev_kv(self, etcd):
        etcdctl('put', '/doot/delete_this', 'old_value')
        response = etcd.delete('/doot/delete_this', prev_kv=True,
                               return_response=True)
        assert response.prev_kvs[0].value == b'old_value'

    def test_delete_keys_with_prefix(self, etcd):
        etcdctl('put', '/foo/1', 'bar')
        etcdctl('put', '/foo/2', 'baz')

        v, _ = etcd.get('/foo/1')
        assert v == b'bar'

        v, _ = etcd.get('/foo/2')
        assert v == b'baz'

        response = etcd.delete_prefix('/foo')
        assert response.deleted == 2

        v, _ = etcd.get('/foo/1')
        assert v is None

        v, _ = etcd.get('/foo/2')
        assert v is None

    def test_new_watch_error(self, etcd):
        # Trigger a failure while waiting on the new watch condition
        with mock.patch.object(etcd.watcher._new_watch_cond, 'wait',
                               side_effect=ValueError):
            with pytest.raises(ValueError):
                etcd.watch('/foo')

        # Ensure a new watch can be created
        events, cancel = etcd.watch('/foo')
        etcdctl('put', '/foo', '42')
        next(events)
        cancel()

    @pytest.mark.skip("TODO")
    def test_watch_key(self, etcd):
        def update_etcd(v):
            etcdctl('put', '/doot/watch', v)
            out = etcdctl('get', '/doot/watch')
            assert base64.b64decode(out['kvs'][0]['value']) == \
                utils.to_bytes(v)

        def update_key():
            # sleep to make watch can get the event
            time.sleep(3)
            update_etcd('0')
            time.sleep(1)
            update_etcd('1')
            time.sleep(1)
            update_etcd('2')
            time.sleep(1)
            update_etcd('3')
            time.sleep(1)

        t = threading.Thread(name="update_key", target=update_key)
        t.start()

        change_count = 0
        events_iterator, cancel = etcd.watch(b'/doot/watch')
        for event in events_iterator:
            assert event.key == b'/doot/watch'
            assert event.value == \
                utils.to_bytes(str(change_count))

            # if cancel worked, we should not receive event 3
            assert event.value != utils.to_bytes('3')

            change_count += 1
            if change_count > 2:
                # if cancel not work, we will block in this for-loop forever
                cancel()

        t.join()

    @pytest.mark.skip("Failed locally")
    def test_watch_key_with_revision_compacted(self, etcd):
        etcdctl('put', '/random', '1')  # Some data to compact

        def update_etcd(v):
            etcdctl('put', '/watchcompation', v)
            out = etcdctl('get', '/watchcompation')
            assert base64.b64decode(out['kvs'][0]['value']) == \
                utils.to_bytes(v)

        def update_key():
            # sleep to make watch can get the event
            time.sleep(3)
            update_etcd('0')
            time.sleep(1)
            update_etcd('1')
            time.sleep(1)
            update_etcd('2')
            time.sleep(1)
            update_etcd('3')
            time.sleep(1)

        t = threading.Thread(name="update_key", target=update_key)
        t.start()

        def watch_compacted_revision_test():
            events_iterator, cancel = etcd.watch(
                b'/watchcompation', start_revision=1)

            error_raised = False
            compacted_revision = 0
            try:
                next(events_iterator)
            except Exception as err:
                error_raised = True
                assert isinstance(err, pyetcd.exceptions.RevisionCompactedError)
                compacted_revision = err.compacted_revision

            assert error_raised is True
            assert compacted_revision == 2

            change_count = 0
            events_iterator, cancel = etcd.watch(
                b'/watchcompation', start_revision=compacted_revision)
            for event in events_iterator:
                assert event.key == b'/watchcompation'
                assert event.value == \
                    utils.to_bytes(str(change_count))

                # if cancel worked, we should not receive event 3
                assert event.value != utils.to_bytes('3')

                change_count += 1
                if change_count > 2:
                    cancel()

        # Compact etcd and test watcher
        etcd.compact(2)

        watch_compacted_revision_test()

        t.join()

    def test_watch_exception_during_watch(self, etcd):
        def pass_exception_to_callback(callback):
            time.sleep(1)
            callback(self.MockedException(grpc.StatusCode.UNAVAILABLE))

        def add_callback_mock(*args, **kwargs):
            callback = args[1]
            t = threading.Thread(name="pass_exception_to_callback",
                                 target=pass_exception_to_callback,
                                 args=[callback])
            t.start()
            return 1

        watcher_mock = mock.MagicMock()
        watcher_mock.add_callback = add_callback_mock
        etcd.watcher = watcher_mock

        events_iterator, cancel = etcd.watch('foo')

        with pytest.raises(pyetcd.exceptions.ConnectionFailedError):
            for _ in events_iterator:
                pass

    def test_watch_timeout_on_establishment(self, etcd):
        foo_etcd = pyetcd.client(timeout=3)

        def slow_watch_mock(*args, **kwargs):
            time.sleep(4)
            return []

        foo_etcd.watcher._watch_stub.Watch = slow_watch_mock  # noqa

        with pytest.raises(pyetcd.exceptions.WatchTimedOut):
            foo_etcd.watch('foo')

    @pytest.mark.skip("Failed locally")
    def test_watch_prefix(self, etcd):
        def update_etcd(v):
            etcdctl('put', '/doot/watch/prefix/' + v, v)
            out = etcdctl('get', '/doot/watch/prefix/' + v)
            assert base64.b64decode(out['kvs'][0]['value']) == \
                utils.to_bytes(v)

        def update_key():
            # sleep to make watch can get the event
            time.sleep(3)
            update_etcd('0')
            time.sleep(1)
            update_etcd('1')
            time.sleep(1)
            update_etcd('2')
            time.sleep(1)
            update_etcd('3')
            time.sleep(1)

        t = threading.Thread(name="update_key_prefix", target=update_key)
        t.start()

        change_count = 0
        events_iterator, cancel = etcd.watch_prefix('/doot/watch/prefix/')
        for event in events_iterator:
            assert event.key == \
                utils.to_bytes('/doot/watch/prefix/{}'.format(change_count))
            assert event.value == \
                utils.to_bytes(str(change_count))

            # if cancel worked, we should not receive event 3
            assert event.value != utils.to_bytes('3')

            change_count += 1
            if change_count > 2:
                # if cancel not work, we will block in this for-loop forever
                cancel()

        t.join()

    @pytest.mark.skip("Failed locally")
    def test_watch_prefix_callback(self, etcd):
        def update_etcd(v):
            etcdctl('put', '/doot/watch/prefix/callback/' + v, v)
            out = etcdctl('get', '/doot/watch/prefix/callback/' + v)
            assert base64.b64decode(out['kvs'][0]['value']) == \
                utils.to_bytes(v)

        def update_key():
            # sleep to make watch can get the event
            time.sleep(3)
            update_etcd('0')
            time.sleep(1)
            update_etcd('1')
            time.sleep(1)

        events = []

        def callback(event):
            events.extend(event.events)

        t = threading.Thread(name="update_key_prefix", target=update_key)
        t.start()

        watch_id = etcd.add_watch_prefix_callback(
            '/doot/watch/prefix/callback/', callback)

        t.join()
        etcd.cancel_watch(watch_id)

        assert len(events) == 2
        assert events[0].key.decode() == '/doot/watch/prefix/callback/0'
        assert events[0].value.decode() == '0'
        assert events[1].key.decode() == '/doot/watch/prefix/callback/1'
        assert events[1].value.decode() == '1'

    @pytest.mark.skip("Failed locally")
    def test_watch_prefix_callback_with_filter(self, etcd):
        def update_etcd(v):
            etcdctl('put', '/doot/watch/prefix/callback/' + v, v)
            out = etcdctl('get', '/doot/watch/prefix/callback/' + v)
            assert base64.b64decode(out['kvs'][0]['value']) == \
                utils.to_bytes(v)

        def delete_etcd(v):
            etcdctl('del', '/doot/watch/prefix/callback/' + v)

        def update_key():
            time.sleep(3)
            update_etcd('0')
            time.sleep(1)
            update_etcd('1')
            time.sleep(1)
            delete_etcd('1')
            time.sleep(1)

        events = []

        def callback(event):
            events.extend(event.events)

        t = threading.Thread(name="update_key_prefix", target=update_key)
        t.start()

        watch_id = etcd.add_watch_prefix_callback(
            '/doot/watch/prefix/callback/',
            callback,
            filters=[etcdrpc.WatchCreateRequest.FilterType.Value('NODELETE')]
        )

        t.join()
        etcd.cancel_watch(watch_id)

        assert len(events) == 2
        assert events[0].key.decode() == '/doot/watch/prefix/callback/0'
        assert events[0].value.decode() == '0'
        assert events[1].key.decode() == '/doot/watch/prefix/callback/1'
        assert events[1].value.decode() == '1'

    def test_sequential_watch_prefix_once(self, etcd):
        try:
            etcd.watch_prefix_once('/doot/', 1)
        except pyetcd.exceptions.WatchTimedOut:
            pass
        try:
            etcd.watch_prefix_once('/doot/', 1)
        except pyetcd.exceptions.WatchTimedOut:
            pass
        try:
            etcd.watch_prefix_once('/doot/', 1)
        except pyetcd.exceptions.WatchTimedOut:
            pass

    def test_watch_responses(self, etcd):
        # Test watch_response & watch_once_response
        revision = etcd.put('/doot/watch', '0').header.revision
        etcd.put('/doot/watch', '1')
        responses_iterator, cancel = \
            etcd.watch_response('/doot/watch', start_revision=revision)

        response_1 = next(responses_iterator)
        cancel()
        response_2 = etcd.watch_once_response('/doot/watch',
                                              start_revision=revision)

        for response in [response_1, response_2]:
            count = 0
            # check that the response contains the etcd revision
            assert response.header.revision > 0
            assert len(response.events) == 2
            for event in response.events:
                assert event.key == b'/doot/watch'
                assert event.value == utils.to_bytes(str(count))
                count += 1

        # Test watch_prefix_response & watch_prefix_once_response
        success_ops = [etcd.transactions.put('/doot/watch/prefix/0', '0'),
                       etcd.transactions.put('/doot/watch/prefix/1', '1')]
        revision = etcd.transaction([], success_ops,
                                    [])[1][0].response_put.header.revision

        responses_iterator, cancel = \
            etcd.watch_prefix_response('/doot/watch/prefix/',
                                       start_revision=revision)

        response_1 = next(responses_iterator)
        cancel()
        response_2 = etcd.watch_prefix_once_response('/doot/watch/prefix/',
                                                     start_revision=revision)

        for response in [response_1, response_2]:
            count = 0
            assert response.header.revision == revision
            assert len(response.events) == 2
            for event in response.events:
                assert event.key == \
                    utils.to_bytes('/doot/watch/prefix/{}'.format(count))
                assert event.value == utils.to_bytes(str(count))
                count += 1

    def test_transaction_success(self, etcd):
        etcdctl('put', '/doot/txn', 'dootdoot')
        etcd.transaction(
            compare=[etcd.transactions.value('/doot/txn') == 'dootdoot'],
            success=[etcd.transactions.put('/doot/txn', 'success')],
            failure=[etcd.transactions.put('/doot/txn', 'failure')]
        )
        out = etcdctl('get', '/doot/txn')
        out = json.loads(out)
        assert base64.b64decode(out['kvs'][0]['value']) == b'success'

    def test_transaction_failure(self, etcd):
        etcdctl('put', '/doot/txn', 'notdootdoot')
        etcd.transaction(
            compare=[etcd.transactions.value('/doot/txn') == 'dootdoot'],
            success=[etcd.transactions.put('/doot/txn', 'success')],
            failure=[etcd.transactions.put('/doot/txn', 'failure')]
        )
        out = etcdctl('get', '/doot/txn')
        out = json.loads(out)
        assert base64.b64decode(out['kvs'][0]['value']) == b'failure'

    def test_ops_to_requests(self, etcd):
        with pytest.raises(Exception):
            etcd._ops_to_requests(['not_transaction_type'])
        with pytest.raises(TypeError):
            etcd._ops_to_requests(0)

    @pytest.mark.skipif(etcd_version < 'v3.3',
                        reason="requires etcd v3.3 or higher")
    def test_nested_transactions(self, etcd):
        etcd.transaction(
            compare=[],
            success=[etcd.transactions.put('/doot/txn1', '1'),
                     etcd.transactions.txn(
                         compare=[],
                         success=[etcd.transactions.put('/doot/txn2', '2')],
                         failure=[])],
            failure=[]
        )
        value, _ = etcd.get('/doot/txn1')
        assert value == b'1'
        value, _ = etcd.get('/doot/txn2')
        assert value == b'2'

    @pytest.mark.skipif(etcd_version < 'v3.3',
                        reason="requires etcd v3.3 or higher")
    def test_transaction_range_conditions(self, etcd):
        etcdctl('put', '/doot/key1', 'dootdoot')
        etcdctl('put', '/doot/key2', 'notdootdoot')
        range_end = utils.prefix_range_end(utils.to_bytes('/doot/'))
        compare = [etcd.transactions.value('/doot/', range_end) == 'dootdoot']
        status, _ = etcd.transaction(compare=compare, success=[], failure=[])
        assert not status
        etcdctl('put', '/doot/key2', 'dootdoot')
        status, _ = etcd.transaction(compare=compare, success=[], failure=[])
        assert status

    def test_replace_success(self, etcd):
        etcd.put('/doot/thing', 'toot')
        status = etcd.replace('/doot/thing', 'toot', 'doot')
        v, _ = etcd.get('/doot/thing')
        assert v == b'doot'
        assert status is True

    def test_replace_fail(self, etcd):
        etcd.put('/doot/thing', 'boot')
        status = etcd.replace('/doot/thing', 'toot', 'doot')
        v, _ = etcd.get('/doot/thing')
        assert v == b'boot'
        assert status is False

    def test_get_prefix(self, etcd):
        for i in range(20):
            etcdctl('put', '/doot/range{}'.format(i), 'i am a range')

        for i in range(5):
            etcdctl('put', '/doot/notrange{}'.format(i), 'i am a not range')

        values = list(etcd.get_prefix('/doot/range'))
        assert len(values) == 20
        for value, _ in values:
            assert value == b'i am a range'

    def test_get_prefix_keys_only(self, etcd):
        for i in range(20):
            etcdctl('put', '/doot/range{}'.format(i), 'i am a range')

        for i in range(5):
            etcdctl('put', '/doot/notrange{}'.format(i), 'i am a not range')

        values = list(etcd.get_prefix('/doot/range', keys_only=True))
        assert len(values) == 20
        for value, meta in values:
            assert meta.key.startswith(b"/doot/range")
            assert not value

    @pytest.mark.skipif(not os.environ.get('ETCDCTL_ENDPOINTS'),
                        reason="Expected etcd to have been run by pifpaf")
    def test_get_prefix_serializable(self, etcd):
        for i in range(20):
            etcdctl('put', '/doot/range{}'.format(i), 'i am a range')

        with _out_quorum():
            values = list(etcd.get_prefix(
                '/doot/range', keys_only=True, serializable=True))

        assert len(values) == 20

    def test_get_prefix_error_handling(self, etcd):
        with pytest.raises(TypeError, match="Don't use "):
            etcd.get_prefix('a_prefix', range_end='end')

    @pytest.mark.skip("Failed locally")
    def test_get_range(self, etcd):
        for char in string.ascii_lowercase:
            if char < 'p':
                etcdctl('put', '/doot/' + char, 'i am in range')
            else:
                etcdctl('put', '/doot/' + char, 'i am not in range')

        values = list(etcd.get_range('/doot/a', '/doot/p'))
        assert len(values) == 15
        for value, _ in values:
            assert value == b'i am in range'

    @pytest.mark.skip("Failed locally")
    def test_all_not_found_error(self, etcd):
        result = list(etcd.get_all())
        assert not result

    def test_range_not_found_error(self, etcd):
        for i in range(5):
            etcdctl('put', '/doot/notrange{}'.format(i), 'i am a not range')

        result = list(etcd.get_prefix('/doot/range'))
        assert not result

    def test_get_all(self, etcd):
        for i in range(20):
            etcdctl('put', '/doot/range{}'.format(i), 'i am in all')

        for i in range(5):
            etcdctl('put', '/doot/notrange{}'.format(i), 'i am in all')
        values = list(etcd.get_all())
        assert len(values) == 25
        for value, _ in values:
            assert value == b'i am in all'

    def test_get_all_keys_only(self, etcd):
        for i in range(20):
            etcdctl('put', '/doot/range{}'.format(i), 'i am in all')

        for i in range(5):
            etcdctl('put', '/doot/notrange{}'.format(i), 'i am in all')
        values = list(etcd.get_all(keys_only=True))
        assert len(values) == 25
        for value, meta in values:
            assert meta.key.startswith(b"/doot/")
            assert not value

    def test_get_count_only(self, etcd):
        for i in range(20):
            etcdctl('put', '/doot/count{}'.format(i), 'i am in all')
        resp = etcd.get_prefix_response(
            key_prefix='/doot/count',
            count_only=True
        )
        assert len(resp.kvs) == 0
        assert resp.count == 20

    def test_get_limit(self, etcd):
        for i in range(20):
            etcdctl('put', '/doot/limit{}'.format(i), 'i am in all')
        for i in range(20):
            resp = etcd.get_prefix_response(key_prefix='/doot/limit', limit=i)
            assert resp.count == 20
            if i == 0 or i == 20:
                assert len(resp.kvs) == 20
                assert resp.more is False
            else:
                assert len(resp.kvs) == i
                assert resp.more is True

    def test_get_revision(self, etcd):
        revisions = []
        for i in range(20):
            resp = etcdctl('put', '/doot/revision{}'.format(i), 'i am in all')
            revisions.append(resp['header']['revision'])
        for i, revision in enumerate(revisions):
            resp = etcd.get_prefix_response(
                key_prefix='/doot/revision',
                revision=revision
            )
            assert resp.count == min(len(revisions), i + 1)

    def test_get_min_mod_revision(self, etcd):
        revisions = []
        for i in range(5):
            resp = etcdctl('put', '/doot/revision', str(i))
            resp = json.loads(resp)
            revisions.append(resp['header']['revision'])
        for revision in revisions:
            resp = etcd.get_response(
                key='/doot/revision',
                min_mod_revision=revision
            )
            assert len(resp.kvs) == 1

    def test_get_max_mod_revision(self, etcd):
        revisions = []
        for i in range(5):
            resp = etcdctl('put', '/doot/revision', str(i))
            resp = json.loads(resp)
            revisions.append(resp['header']['revision'])
        for revision in revisions:
            resp = etcd.get_response(
                key='/doot/revision',
                max_mod_revision=revision
            )
            if revision == revisions[-1]:
                assert len(resp.kvs) == 1
            else:
                assert len(resp.kvs) == 0

    def test_sort_order(self, etcd):
        def remove_prefix(string, prefix):
            return string[len(prefix):]

        initial_keys = 'abcde'
        initial_values = 'qwert'

        for k, v in zip(initial_keys, initial_values):
            etcdctl('put', '/doot/{}'.format(k), v)

        keys = ''
        for value, meta in etcd.get_prefix('/doot', sort_order='ascend'):
            keys += remove_prefix(meta.key.decode('utf-8'), '/doot/')

        assert keys == initial_keys

        reverse_keys = ''
        for value, meta in etcd.get_prefix('/doot', sort_order='descend'):
            reverse_keys += remove_prefix(meta.key.decode('utf-8'), '/doot/')

        assert reverse_keys == ''.join(reversed(initial_keys))

    def test_get_response(self, etcd):
        etcdctl('put', '/foo/key1', 'value1')
        etcdctl('put', '/foo/key2', 'value2')
        response = etcd.get_response('/foo/key1')
        assert response.header.revision > 0
        assert response.count == 1
        assert response.kvs[0].key == b'/foo/key1'
        assert response.kvs[0].value == b'value1'
        response = etcd.get_prefix_response('/foo/', sort_order='ascend')
        assert response.header.revision > 0
        assert response.count == 2
        assert response.kvs[0].key == b'/foo/key1'
        assert response.kvs[0].value == b'value1'
        assert response.kvs[1].key == b'/foo/key2'
        assert response.kvs[1].value == b'value2'
        # Test that the response header is accessible even when the
        # requested key or range of keys does not exist
        etcdctl('del', '--prefix', '/foo/')
        response = etcd.get_response('/foo/key1')
        assert response.count == 0
        assert response.header.revision > 0
        response = etcd.get_prefix_response('/foo/')
        assert response.count == 0
        assert response.header.revision > 0
        response = etcd.get_range_response('/foo/key1', '/foo/key3')
        assert response.count == 0
        assert response.header.revision > 0
        response = etcd.get_all_response()
        assert response.count == 0
        assert response.header.revision > 0

    def test_lease_grant(self, etcd):
        lease = etcd.lease(1)

        assert isinstance(lease.ttl, int)
        assert isinstance(lease.id, int)

    def test_lease_revoke(self, etcd):
        lease = etcd.lease(1)
        lease.revoke()

    @pytest.mark.skipif(etcd_version.startswith('v3.0'),
                        reason="requires etcd v3.1 or higher")
    def test_lease_keys_empty(self, etcd):
        lease = etcd.lease(1)
        assert lease.keys == []

    @pytest.mark.skipif(etcd_version.startswith('v3.0'),
                        reason="requires etcd v3.1 or higher")
    def test_lease_single_key(self, etcd):
        lease = etcd.lease(1)
        etcd.put('/doot/lease_test', 'this is a lease', lease=lease)
        assert lease.keys == [b'/doot/lease_test']

    @pytest.mark.skipif(etcd_version.startswith('v3.0'),
                        reason="requires etcd v3.1 or higher")
    def test_lease_expire(self, etcd):
        key = '/doot/lease_test_expire'
        lease = etcd.lease(1)
        etcd.put(key, 'this is a lease', lease=lease)
        assert lease.keys == [utils.to_bytes(key)]
        v, _ = etcd.get(key)
        assert v == b'this is a lease'
        assert lease.remaining_ttl <= lease.granted_ttl

        # wait for the lease to expire
        time.sleep(lease.granted_ttl + 2)
        v, _ = etcd.get(key)
        assert v is None

    def test_member_list(self, etcd):
        assert len(list(etcd.members)) == 3
        for member in etcd.members:
            assert member.name.startswith('pifpaf')
            for peer_url in member.peer_urls:
                assert peer_url.startswith('http://')
            for client_url in member.client_urls:
                assert client_url.startswith('http://')
            assert isinstance(member.id, int)

    def test_lock_acquire(self, etcd):
        lock = etcd.lock('lock-1', ttl=10)
        assert lock.acquire() is True
        assert etcd.get(lock.key)[0] is not None
        assert lock.acquire(timeout=0) is False
        assert lock.acquire(timeout=1) is False

    def test_lock_release(self, etcd):
        lock = etcd.lock('lock-2', ttl=10)
        assert lock.acquire() is True
        assert etcd.get(lock.key)[0] is not None
        assert lock.release() is True
        v, _ = etcd.get(lock.key)
        assert v is None
        assert lock.acquire() is True
        assert lock.release() is True
        assert lock.acquire(timeout=None) is True

    def test_lock_expire(self, etcd):
        lock = etcd.lock('lock-3', ttl=3)
        assert lock.acquire() is True
        assert etcd.get(lock.key)[0] is not None
        # wait for the lease to expire
        time.sleep(9)
        v, _ = etcd.get(lock.key)
        assert v is None

    def test_lock_refresh(self, etcd):
        lock = etcd.lock('lock-4', ttl=3)
        assert lock.acquire() is True
        assert etcd.get(lock.key)[0] is not None
        # sleep for the same total time as test_lock_expire, but refresh each
        # second
        for _ in range(9):
            time.sleep(1)
            lock.refresh()

        assert etcd.get(lock.key)[0] is not None

    def test_lock_is_acquired(self, etcd):
        lock1 = etcd.lock('lock-5', ttl=2)
        assert lock1.is_acquired() is False

        lock2 = etcd.lock('lock-5', ttl=2)
        lock2.acquire()
        assert lock2.is_acquired() is True
        lock2.release()

        lock3 = etcd.lock('lock-5', ttl=2)
        lock3.acquire()
        assert lock3.is_acquired() is True
        assert lock2.is_acquired() is False

    def test_lock_context_manager(self, etcd):
        with etcd.lock('lock-6', ttl=2) as lock:
            assert lock.is_acquired() is True
        assert lock.is_acquired() is False

    def test_lock_contended(self, etcd):
        lock1 = etcd.lock('lock-7', ttl=2)
        lock1.acquire()
        lock2 = etcd.lock('lock-7', ttl=2)
        lock2.acquire()
        assert lock1.is_acquired() is False
        assert lock2.is_acquired() is True

    def test_lock_double_acquire_release(self, etcd):
        lock = etcd.lock('lock-8', ttl=10)
        assert lock.acquire(0) is True
        assert lock.acquire(0) is False
        assert lock.release() is True

    def test_lock_acquire_none(self, etcd):
        lock = etcd.lock('lock-9', ttl=10)
        assert lock.acquire(None) is True
        # This will succeed after 10 seconds since the TTL will expire and the
        # lock is not refreshed
        assert lock.acquire(None) is True

    def test_lock_acquire_with_timeout(self, etcd):
        lock1 = etcd.lock('lock-10', ttl=10)
        lock2 = etcd.lock('lock-10', ttl=10)

        original_watch = etcd.watch
        watch_called = [0]

        def release_lock_before_watch(*args, **kwargs):
            watch_called[0] += 1
            # Simulates the case where key is expired before watch is called.
            # See https://github.com/kragniz/python-etcd3/issues/1107
            lock1.release()
            return original_watch(*args, **kwargs)

        original_transaction = etcd.transaction
        transaction_called = [0]

        def transaction_wrapper(*args, **kwargs):
            transaction_called[0] += 1
            return original_transaction(*args, **kwargs)

        assert lock1.acquire() is True
        with mock.patch.object(pyetcd.Etcd3Client, 'watch',
                               wraps=release_lock_before_watch):
            with mock.patch.object(pyetcd.Etcd3Client, 'transaction',
                                   wraps=transaction_wrapper):
                assert lock2.acquire(timeout=5) is True

        # watch must be called only for lock2 once
        assert watch_called[0] == 1

        # transaction must be called once for lock1, twice for lock2
        assert transaction_called[0] == 3

    def test_internal_exception_on_internal_error(self, etcd):
        exception = self.MockedException(grpc.StatusCode.INTERNAL)
        kv_mock = mock.PropertyMock()
        kv_mock.Range.side_effect = exception
        with mock.patch('pyetcd.Etcd3Client.kvstub',
                        new_callable=mock.PropertyMock) as property_mock:
            property_mock.return_value = kv_mock
            with pytest.raises(pyetcd.exceptions.InternalServerError):
                etcd.get("foo")

    def test_connection_failure_exception_on_connection_failure(self, etcd):
        exception = self.MockedException(grpc.StatusCode.UNAVAILABLE)
        kv_mock = mock.PropertyMock()
        kv_mock.Range.side_effect = exception
        with mock.patch('pyetcd.Etcd3Client.kvstub',
                        new_callable=mock.PropertyMock) as property_mock:
            property_mock.return_value = kv_mock
            with pytest.raises(pyetcd.exceptions.ConnectionFailedError):
                etcd.get("foo")
            assert etcd.endpoint_in_use.is_failed()

    def test_connection_timeout_exception_on_connection_timeout(self, etcd):
        exception = self.MockedException(grpc.StatusCode.DEADLINE_EXCEEDED)
        kv_mock = mock.PropertyMock()
        kv_mock.Range.side_effect = exception
        with mock.patch('pyetcd.Etcd3Client.kvstub',
                        new_callable=mock.PropertyMock) as property_mock:
            property_mock.return_value = kv_mock
            with pytest.raises(pyetcd.exceptions.ConnectionTimeoutError):
                etcd.get("foo")
            assert etcd.endpoint_in_use.is_failed()

    def test_single_endpoint_failover(self, etcd):
        etcd.failover = True
        exception = self.MockedException(grpc.StatusCode.UNAVAILABLE)
        kv_mock = mock.PropertyMock()
        kv_mock.Range.side_effect = exception
        with mock.patch('pyetcd.Etcd3Client.kvstub',
                        new_callable=mock.PropertyMock) as property_mock:
            property_mock.return_value = kv_mock
            with pytest.raises(pyetcd.exceptions.ConnectionFailedError):
                etcd.get("foo")
        with pytest.raises(pyetcd.exceptions.NoServerAvailableError):
            etcd.get("foo")

    def test_grpc_exception_on_unknown_code(self, etcd):
        exception = self.MockedException(grpc.StatusCode.DATA_LOSS)
        kv_mock = mock.PropertyMock()
        kv_mock.Range.side_effect = exception
        with mock.patch('pyetcd.Etcd3Client.kvstub',
                        new_callable=mock.PropertyMock) as property_mock:
            property_mock.return_value = kv_mock
            with pytest.raises(grpc.RpcError):
                etcd.get("foo")
            assert not etcd.endpoint_in_use.is_failed()

    def test_status_member(self, etcd):
        status = etcd.status()

        assert isinstance(status.leader, pyetcd.members.Member) is True
        assert status.leader.id in [m.id for m in etcd.members]

    def test_hash(self, etcd):
        assert isinstance(etcd.hash(), int)

    def test_snapshot(self, etcd):
        with tempfile.NamedTemporaryFile() as f:
            etcd.snapshot(f)
            f.flush()

            etcdctl('snapshot', 'status', f.name)
