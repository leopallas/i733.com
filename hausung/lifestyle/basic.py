#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-10 16:03
# Copyright 2014 LEO

import tornado.ioloop
import tornado.escape
import tornado.web
import tornado.httpserver
import tornado.log

from constants import ERR_JSON


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.set_header('Content-Type', 'application/json')

    @property
    def db(self):
        return self.application.db

    @property
    def validate_token(self):
        args = self.request.arguments

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
                    self.response_status(ERR_JSON)
        return data

    @property
    def response_status(self, code=(500, 'Server Error!')):
        self.set_status(code[0], code[1])