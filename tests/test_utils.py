class TestUtils(object):
    def test_prefix_range_end(self):
        assert pyetcd.utils.prefix_range_end(b'foo') == b'fop'
        assert pyetcd.utils.prefix_range_end(b'ab\xff') == b'ac\xff'
        assert (pyetcd.utils.prefix_range_end(b'a\xff\xff\xff\xff\xff')
                == b'b\xff\xff\xff\xff\xff')

    def test_to_bytes(self):
        assert isinstance(pyetcd.utils.to_bytes(b'doot'), bytes) is True
        assert isinstance(pyetcd.utils.to_bytes('doot'), bytes) is True
        assert pyetcd.utils.to_bytes(b'doot') == b'doot'
        assert pyetcd.utils.to_bytes('doot') == b'doot'
