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

import constants
from constants import ERR_JSON, URL_PARAMETERS_NOT_CORRECT

from urllib import quote


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        #set response header name and value.
        self.supported_path = ['register', 'get-auth-code']
        self.set_header('Content-Type', 'application/json')

    @property
    def db(self):
        return self.application.db

    def initialize(self):
        data = {}
        args = self.request.query_arguments
        for a in args:
            data[a] = self.get_argument(a)
        if data['tm'] is None or data['nonce'] is None or data['au'] is None or data['tkn'] is None:
            self.send_error(10008)
        uri = '%s+%s+%s+%s' % (self.request.method, self.request.protocol, self.request.path, self.request.query)
        uri = uri.replace('&au=' + quote(data['au']), '')
        uri = uri.replace('&tkn=' + quote(data['tkn']), '')
        print uri

    def prepare(self):
        action = self.request.path.split('/')[-1]
        if action not in self.supported_path:
            self.send_response_error(400)

    @property
    def body_json(self):
        json = {}
        if self.request.method in ('POST', 'DELETE', 'PATCH', 'PUT', 'OPTIONS'):
            content_type = self.request.headers['Content-Type']
            if content_type == 'application/json':
                try:
                    json = tornado.escape.json_decode(self.request.body)
                except ValueError, e:
                    tornado.log.LogFormatter('decode track data error. e=%s' % e)
                    # self.send_response_error(10000)
                    self.send_response_error(10000)
            else:
                self.send_response_error(9000)
            # elif content_type in ('application/x-www-form-urlencoded', 'multipart/form-data'):
            #     args3 = self.request.body_arguments
            #     for a in args3:
            #         data[a] = self.get_argument(a)

        return json

    # @property
    def send_response_error(self, code):
        reason = constants.errorcodes.get(code, 'Unknown')
        self.set_status(code, reason)
    
    # @property
    def response_status(self, code=(500, 'Server Error!')):
        self.set_status(code[0], code[1])

    # @property
    # def response_status(self, status_code=500):
    #     reason = constants.responses.get(status_code, 'Unknown')
    #     self.status_code(status_code, reason)