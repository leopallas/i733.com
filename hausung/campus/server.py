#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-10 15:24
# Copyright 2014 LEO

import torndb
import tornado.ioloop
import tornado.escape
import tornado.web
import tornado.httpserver
import tornado.log
from tornado.options import define, options

from url import url


define("port", default=8889, help="run on the given port", type=int)

define("mysql_host", default="192.168.1.101:3306", help="lifestyle database host")
define("mysql_database", default="lifestyle_2.0", help="lifestyle database name")
define("mysql_user", default="root", help="lifestyle database user")
define("mysql_password", default="root", help="lifestyle database password")

define("mysql_database_auth", default="auth_2.0", help="authentication database name")
define("mysql_user_auth", default="root", help="authentication database user")
define("mysql_password_auth", default="root", help="authentication database password")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = url
        settings = dict(
            web_title=u"Tornado Web",
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

        # Have one global connection to the blog DB across all handlers
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)

        self.db_auth = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database_auth,
            user=options.mysql_user_auth, password=options.mysql_password_auth)


def main():
    # tornado.options.options['log_file_prefix'].set('/home/xw/my_app.log')
    tornado.options.parse_command_line()
    print "Starting tornado web server on http://127.0.0.1:%s" % options.port
    print 'Quit the server with CONTROL-C'
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()