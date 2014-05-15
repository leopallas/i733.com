#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-15 16:10
# Copyright 2014 LEO
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.gen
import tornado.httpclient
import tornado.concurrent
import tornado.ioloop
import tornado.log

import time

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class SleepHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time() + 10)
        self.write("when i sleep 10s")


class JustNowHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("i hope just now see you")

# old implement method
# class SleepHandler(tornado.web.RequestHandler):
#     @tornado.web.asynchronous
#     def get(self):
#         tornado.ioloop.IOLoop.instance().add_timeout(time.time() + 5, callback=self.on_response)
#
#     def on_response(self):
#         self.write("when i sleep 5s")
#         self.finish()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    tornado.log.gen_log.info("start server")
    app = tornado.web.Application(handlers=[
            (r"/sleep", SleepHandler), (r"/justnow", JustNowHandler)], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()