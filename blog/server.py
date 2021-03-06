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
from sqlalchemy.orm import scoped_session, sessionmaker
from blog.model.models import engine
from setting import DEBUG, LISTEN_PORT, STATIC_PATH, TEMPLATE_PATH, COOKIE_SECRET, LOGIN_URL, XSRF_COOKIES, BLOG_TITLE, STATIC_URL

from handler.admin import AdminHomeHandler, AdminLoginHandler, AdminLogoutHandler, AdminProfileHandler, \
    AdminSettingHandler, AdminPostListHandler, AdminPostAddHandler, CategoryListHandler
from handler.filemanager import FileListHandler, DirListHandler, GetInfoHandler

define("port", default=LISTEN_PORT, help="run on the given port", type=int)

urls = [
    (r"/admin/login", AdminLoginHandler),
    (r"/admin/logout", AdminLogoutHandler),
    (r"/admin/home", AdminHomeHandler),
    (r"/admin/profile", AdminProfileHandler),
    (r"/admin/setting", AdminSettingHandler),
    (r"/admin/post/list", AdminPostListHandler),
    (r"/admin/post/add", AdminPostAddHandler),
    (r"/filemanager", FileListHandler),
    (r"/filemanager/dirlist/?", DirListHandler),
    (r"/filemanager/?", GetInfoHandler),
    (r"/category/list", CategoryListHandler),

]

settings = dict(
    blog_title=BLOG_TITLE,
    static_path=STATIC_PATH,
    template_path=TEMPLATE_PATH,
    #ui_modules={"Entry": EntryModule},
    cookie_secret=COOKIE_SECRET,
    xsrf_cookies=XSRF_COOKIES,
    gzip=True,
    login_url=LOGIN_URL,
    debug=DEBUG,
)


class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, urls, **settings)
        # Have one global connection to the blog DB across all handlers
        self.db = scoped_session(sessionmaker(bind=engine))


def main():
    tornado.options.parse_command_line()
    print "Starting tornado web server on http://127.0.0.1:%s" % options.port
    print 'Quit the server with CONTROL-C'
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


import tornado.wsgi
class WsgiApplication(tornado.wsgi.WSGIApplication):
    def __init__(self):
        tornado.wsgi.WSGIApplication.__init__(self, urls, **settings)
        # Have one global connection to the blog DB across all handlers
        self.db = scoped_session(sessionmaker(bind=engine))


def wsgi_main():
    import wsgiref.simple_server
    server = wsgiref.simple_server.make_server('', options.port, WsgiApplication())
    server.serve_forever()

if __name__ == "__main__":
    main()