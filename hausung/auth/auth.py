#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo XU     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-05 12:06
# Copyright 2014 LEO
from collections import defaultdict

import os
import tornado.ioloop
import tornado.escape
import tornado.web
import tornado.httpserver
import tornado.log
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

import pymongo
from pymongo import MongoClient
import json
from bson import json_util
from bson.objectid import ObjectId

MONGODB_DB_URL = 'mongodb://localhost:27017/'
MONGODB_DB_NAME = 'lifestyle'

client = MongoClient(MONGODB_DB_URL)
db = client[MONGODB_DB_NAME]


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/register", RegisterHandler),
            # (r"/archive", ArchiveHandler),
            # (r"/feed", FeedHandler),
            # (r"/entry/([^/]+)", EntryHandler),
            # (r"/compose", ComposeHandler),
            # (r"/auth/login", AuthLoginHandler),
            # (r"/auth/logout", AuthLogoutHandler),
        ]
        settings = dict(
            web_title=u"Tornado Weg",
            # template_path=os.path.join(os.path.dirname(__file__), "templates"),
            # static_path=os.path.join(os.path.dirname(__file__), "static"),
            # xsrf_cookies=True,
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        # super(Application, self).__init__(self, handlers,**settings)

        conn = pymongo.Connection("localhost", 27017)
        self.db = conn["lifestyle"]


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.set_header('Content-Type', 'application/json')

    @property
    def db(self):
        return self.application.db

    @property
    def get_data(self):
        data = {}
        content_type = self.request.headers['Content-Type']
        if content_type == 'application/json':
            try:
                data['json'] = tornado.escape.json_decode(self.request.body)
            except ValueError, e:
                tornado.log.LogFormatter('decode track data error. e=%s' % e)
                # r = {}
                # r['status_code'] = 500
                # r['status_desc'] = 'decode json error'
                # self.write(tornado.escape.json_encode(r))
                # self.add_header('status_code', 500)
                # self.add_header('status_desc', 'decode json error')
                self.set_status(10000, 'decode json error')
        else:
            # 获得所以输入参数,并存在data中
            args = self.request.arguments
            for a in args:
                data[a] = self.get_argument(a)
            # 获取file类型参数
            data["files"] = self.request.files
            # 获取headers
            data["headers"] = self.request.headers
        return data


class RegisterHandler(BaseHandler):
    def post(self):
        data = self.get_data
        if self.get_status() != 200:
            return
        account = data['json']

        coll = self.db.accounts
        account_doc = coll.find_one({'username': account['username']})
        if account_doc:
            self.set_status(10001, 'username already exist')
            return
        else:
            username = account['username'].encode("utf-8")

            print type(username)
            account['nickname'] = username[0: 3] + '****' + username[7: 11]
            coll.insert(account)
            del account["_id"]
            # json_string = json_util.dumps(account_doc)
            self.write(account)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()