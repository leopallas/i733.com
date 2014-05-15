#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-15 17:25
# Copyright 2014 LEO

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen
from tornado.concurrent import run_on_executor
# 这个并发库在python3自带在python2需要安装sudo pip install futures
from concurrent.futures import ThreadPoolExecutor

import time

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world %s" % time.time())


class SleepHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(max_workers=4)

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, n):
        # 假如你执行的异步会返回值被继续调用可以这样(只是为了演示),否则直接yield就行
        res = yield self.sleep(n)
        print res
        self.write("%ss Awake! %s" % (res, time.time()))
        self.finish()

    @run_on_executor
    def sleep(self, n):
        time.sleep(float(n))
        return n


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/", MainHandler),
        (r"/sleep/(\d+)", SleepHandler),
    ], debug=True)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

