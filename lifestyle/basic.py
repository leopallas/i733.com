#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-10 16:03
# Copyright 2014 LEO

import tornado.ioloop
from tornado.escape import url_unescape, json_decode
import tornado.web
import tornado.httpserver
from tornado.log import gen_log
from tornado.web import MissingArgumentError
from tornado.web import HTTPError

from hausung import utils
import base64
import hmac
import hashlib


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
        pass

    def prepare(self):
        args = self.request.query_arguments
        if not args.get('tm') or not args.get('nonce') or not args.get('au') or not args.get('tkn'):
            gen_log.debug('Missing parameter tm or nonce or au or tkn')
            raise MissingArgumentError('tm or nonce or au or tkn')

        data = {}
        for a in args:
            data[a] = self.get_argument(a)
        #根据SECRET_TOKEN从数据库中取得签名的Key
        authkey = self.db.get("SELECT SIGNATURE_KEY FROM auth_key where SECRET_TOKEN = %s", data['tkn'])
        if not authkey:
            raise HTTPError(400)

        # 验证签名
        uri = '%s+%s+%s+%s' % (
            self.request.method, self.request.protocol, self.request.path, url_unescape(self.request.query))
        uri = uri.replace('&au=' + data['au'], '')
        uri = uri.replace('&tkn=' + data['tkn'], '')
        sign = utils.signature(authkey['SIGNATURE_KEY'], uri)
        if sign != data['au']:
            raise HTTPError(400)
            # action = self.request.path.split('/')[-1]
            # if action not in self.supported_path:
            #     self.send_response_error(400)


    # def signature(self, key, text):
    #     if isinstance(key, unicode):
    #         key = str(key)
    #
    #     key = base64.b64decode(key)
    #     h = hmac.new(key, text.encode('utf-8'), hashlib.sha1)
    #     my_signature = base64.b64encode(h.digest()).strip()
    #     return my_signature


    @property
    def body_json(self):
        json = {}
        if self.request.method in ('POST', 'DELETE', 'PATCH', 'PUT', 'OPTIONS'):
            content_type = self.request.headers['Content-Type']
            if content_type == 'application/json':
                try:
                    json = json_decode(self.request.body)
                except ValueError, e:
                    # tornado.log.LogFormatter('decode track data error. e=%s' % e)
                    gen_log.debug('decode track data error. e=%s' % e)
                #     error_info = {'my_exc_info': 'decode track data error. e=%s' % e, 'des': '参数有误！',
                # 'reason': ['参数有误！'], 'next_url': '/'}
                #     self.send_error(400, **error_info)
                    raise HTTPError(400)
            else:
                gen_log.debug('content-type is not application/json.')
                raise HTTPError(400)
        return json