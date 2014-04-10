#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-10 15:24
# Copyright 2014 LEO

import tornado.ioloop
import tornado.escape
import tornado.web
import tornado.httpserver
import tornado.log
from tornado.options import define, options
import pymongo

from url import url


define("port", default=8889, help="run on the given port", type=int)
define("mongodb_host", default="127.0.0.1", help="mongodb  host")
define("mongodb_port", default=27017, help="mongodb port host")
define("mongodb_database", default="lifestyle", help="mongodb database name")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = url
        settings = dict(
            web_title=u"Tornado Web",
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        conn = pymongo.Connection(options.mongodb_host, options.mongodb_port)
        self.db = conn[options.mongodb_database]


def main():
    tornado.options.parse_command_line()
    print "Starting tornado web server on http://127.0.0.1:%s" % options.port
    print 'Quit the server with CONTROL-C'
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()