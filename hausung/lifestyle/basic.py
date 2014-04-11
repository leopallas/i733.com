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

from constants import ERR_JSON, URL_PARAMETERS_NOT_CORRECT


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        #set response header name and value.
        self.set_header('Content-Type', 'application/json')

    @property
    def db(self):
        return self.application.db

    @property
    def validate_token(self):
        args = self.request.arguments


    def initialize(self):
        self.supported_path = ['path_a', 'path_b', 'path_c']

    def prepare(self):
        action = self.request.path.split('/')[-1]
        if action not in self.supported_path:
            self.send_error(400)

    @property
    def get_data(self):
        data = {}
        # 获得所以输入参数,并存在data中
        args = self.request.arguments
        for a in args:
            data[a] = self.get_argument(a)

        if data['tm'] or data['nonce'] or data['au'] or data['tkn']:
            self.response_status(URL_PARAMETERS_NOT_CORRECT)

        method = self.request.method
        protocol = self.request.protocol
        uri = self.request.uri
        self.request.url

        action = self.request.path.split('/')[-1]
        query_string = self.get_query_argument
        query_strings = self.get_query_arguments

        url = '%s+%s+%s+%s' % (self.request.method, self.request.protocol, self.request.uri, self.get_query_argument)



        # String FILE           = "file";
        # String JSON_DATA      = "json-data";

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

    # @property
    # def response_status(self, status_code=500):
    #     reason = constants.responses.get(status_code, 'Unknown')
    #     self.status_code(status_code, reason)