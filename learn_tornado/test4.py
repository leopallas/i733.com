#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-15 16:25
# Copyright 2014 LEO

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.gen
import tornado.httpclient
import tornado.concurrent
import tornado.ioloop

import time
# 一个mongodb出品的支持异步的数据库的python驱动
import motor
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)
# db其实就是test数据库的游标
db = motor.MotorClient().open_sync().test

class SleepHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        # 这一行执行还是阻塞需要时间的，我的tt集合有一些数据并且没有索引
        cursor = db.tt.find().sort([('a', -1)])
        # 这部分会异步非阻塞的执行二不影响其他页面请求
        while (yield cursor.fetch_next):
            message = cursor.next_object()
            self.write('<li>%s</li>' % message['a'])
        self.write('</ul>')
        self.finish()

    def _on_response(self, message, error):
        if error:
            raise tornado.web.HTTPError(500, error)
        elif message:
            for i in message:
                self.write('<li>%s</li>' % i['a'])
        else:
            self.write('</ul>')
            self.finish()


class JustNowHandler(BaseHandler):
    def get(self):
        self.write("i hope just now see you")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
            (r"/sleep", SleepHandler), (r"/justnow", JustNowHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()