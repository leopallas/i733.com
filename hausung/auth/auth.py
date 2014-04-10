#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-05 12:06
# Copyright 2014 LEO

import time

import tornado.ioloop
import tornado.escape
import tornado.web
import tornado.httpserver
import tornado.log
from tornado.options import define, options

import pymongo
# from pymongo import MongoClient
from hausung import utils


define("port", default=8888, help="run on the given port", type=int)
define("mongodb_host", default="127.0.0.1", help="mongodb  host")
define("mongodb_port", default=27017, help="mongodb port host")
#
# MONGODB_DB_URL = 'mongodb://localhost:27017/'
# MONGODB_DB_NAME = 'lifestyle'
# client = MongoClient(MONGODB_DB_URL)
# db = client[MONGODB_DB_NAME]

error = {10000: "u", 10001: "mm"}


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/get-auth-code", GetAuthCodeHandler),
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
        # 获得所以输入参数,并存在data中
        args = self.request.arguments
        for a in args:
            data[a] = self.get_argument(a)
        # 获取file类型参数
        data["files"] = self.request.files
        # 获取headers
        data["headers"] = self.request.headers
        if self.request.method in ('POST', 'DELETE', 'PATCH', 'PUT', 'OPTIONS'):
            if self.request.headers['Content-Type'] == 'application/json':
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
        return data


class GetAuthCodeHandler(BaseHandler):
    def get(self):
        data = self.get_data
        if self.get_status() != 200:
            return
        phone = data['phone']
        coll = self.db.register
        register_doc = coll.find_one({'phone': phone})
        if register_doc is not None:
            if register_doc['registerInd']:
                self.set_status(10001, 'phone is already register')
                return
            else:
                print register_doc['registerInd']
                coll.update({'phone': phone}, {"$set": {'authCode': utils.gen_auth_code()}})
        else:
            register_doc = {'phone': phone, 'authCode': utils.gen_auth_code(), 'createDt': time.time(),
                            'registerInd': False}
            coll.insert(register_doc)
            del register_doc['_id']
            self.write(register_doc)


class RegisterHandler(BaseHandler):
    def post(self):
        data = self.get_data
        if self.get_status() != 200:
            return
        register = data['json']
        phone = register['phone']
        coll = self.db.register
        register_doc = coll.find_one({'phone': phone})
        if register_doc is None:
            self.set_status(10002, 'Phone is not pair with auth code')
            return
        else:
            if register_doc['authCode'] != register['authCode']:
                self.set_status(10003, 'Auth Code is not correct')
                return
            if (time.time() - register_doc['createDt']) > 1200:
                self.set_status(10004, 'Auth Code is already expired')
                return
            # update register, let register indicator change to yes
            coll.update({'phone': register['phone']}, {"$set": {'registerInd': True}})
            # insert account info
            nickname = phone.encode("utf-8")
            nickname = nickname[0: 3] + '****' + nickname[7: 11]
            now = time.time()
            account_doc = {'username': phone,
                           'nickname': nickname,
                           'password': utils.sha1(register['password']),
                           'createDt': now,
                           'updateDt': now}
            self.db.account.insert(account_doc)
            del account_doc["_id"]
            # json_string = json_util.dumps(account_doc)
            self.write(account_doc)


class LoginHandler(BaseHandler):
    def post(self):
        data = self.get_data
        if self.get_status() != 200:
            return
        account = data['json']
        if account['username'] or account['password']:
            self.set_status(10005, 'username or password is not empty')
            return
        coll = self.db.account
        account_doc = coll.find_one({'username': account['username']})
        if account_doc:
            self.set_status(10005, 'user is not register')
            return
        if account_doc['password'] != utils.sha1(account['password']):
            self.set_status(10006, 'password is wrong')

        del account_doc["_id"]
        self.write(account_doc)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()