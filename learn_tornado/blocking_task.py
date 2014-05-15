#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-15 15:32
# Copyright 2014 LEO
import time

import tornado.ioloop
import tornado.web
import tornado.httpserver

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world %s" % time.time())


class SleepHandler(tornado.web.RequestHandler):
    def get(self, n):
        time.sleep(float(n))
        self.write("Awake! %s" % time.time())


if __name__ == "__main__":
    tornado.options.parse_command_line()
    application = tornado.web.Application(handlers=[
                                          (r"/", MainHandler),
                                          (r"/sleep/(\d+)", SleepHandler),
                                          ], debug=True)

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()