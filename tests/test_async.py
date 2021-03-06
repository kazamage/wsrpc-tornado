#!/usr/bin/env python
# encoding: utf-8
from tornado.testing import gen_test
from . import TestBase


class TestAsync(TestBase):
    URI = '/ws/async'

    @gen_test
    def test_sync_init(self):
        self.assertTrue((yield self.call("sync")))

    @gen_test
    def test_sync_echo(self):
        kw = dict(test=True, arg0=1, arg1=2, arg2=3, arg3=4)
        self.assertEqual((yield self.call('sync.simple_method', **kw)), kw)

    @gen_test
    def test_sync_lambda(self):
        kw = dict(test=True, arg0=1, arg1=2, arg2=3, arg3=4)
        result = yield self.call('sync_func', **kw)
        self.assertEqual(result, kw)
