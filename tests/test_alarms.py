import pytest
import pyetcd
import grpc
from pyetcd import etcdrpc

class TestAlarms:
    @pytest.fixture
    def etcd(self):
        etcd = pyetcd.client()
        yield etcd
        etcd.disarm_alarm()
        for m in etcd.members:
            if m.active_alarms:
                etcd.disarm_alarm(m.id)

    def test_create_alarm_all_members(self, etcd):
        alarms = etcd.create_alarm()

        assert len(alarms) == 1
        assert alarms[0].member_id == 0
        assert alarms[0].alarm_type == etcdrpc.NOSPACE

    def test_create_alarm_specific_member(self, etcd):
        a_member = next(etcd.members)

        alarms = etcd.create_alarm(member_id=a_member.id)

        assert len(alarms) == 1
        assert alarms[0].member_id == a_member.id
        assert alarms[0].alarm_type == etcdrpc.NOSPACE

    def test_list_alarms(self, etcd):
        a_member = next(etcd.members)
        etcd.create_alarm()
        etcd.create_alarm(member_id=a_member.id)
        possible_member_ids = [0, a_member.id]

        alarms = list(etcd.list_alarms())

        assert len(alarms) == 2
        for alarm in alarms:
            possible_member_ids.remove(alarm.member_id)
            assert alarm.alarm_type == etcdrpc.NOSPACE

        assert possible_member_ids == []

    def test_disarm_alarm(self, etcd):
        etcd.create_alarm()
        assert len(list(etcd.list_alarms())) == 1

        etcd.disarm_alarm()
        assert len(list(etcd.list_alarms())) == 0
