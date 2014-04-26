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
from tornado.log import app_log, gen_log
from tornado.web import MissingArgumentError
from tornado.web import HTTPError

import util
import constants


class AuthBaseHandler(tornado.web.RequestHandler):
    SUPPORTED_METHODS = ("POST", "DELETE", "PATCH", "PUT", "OPTIONS")

    def __init__(self, application, request, **kwargs):
        super(AuthBaseHandler, self).__init__(application, request, **kwargs)
        # self.supported_path = ['register', 'get-auth-code']
        #set response header name and value.
        self.set_header('Content-Type', 'application/json')

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

            # self.response_status(400)
        # 验证签名
        uri = '%s+%s+%s+%s' % (
            self.request.method, self.request.protocol, self.request.path, url_unescape(self.request.query))
        uri = uri.replace('&au=' + data['au'], '')
        uri = uri.replace('&tkn=' + data['tkn'], '')
        sign = util.signature(authkey['SIGNATURE_KEY'], uri)
        if sign != data['au']:
            raise HTTPError(400)


    @property
    def body_json(self):
        if self.request.method in self.SUPPORTED_METHODS:
            content_type = self.request.headers['Content-Type']
            if content_type == 'application/json':
                try:
                    return json_decode(self.request.body)
                except ValueError, e:
                    gen_log.error('decode track data error. e=%s' % e)
                #     error_info = {'my_exc_info': 'decode track data error. e=%s' % e, 'des': '参数有误！',
                # 'reason': ['参数有误！'], 'next_url': '/'}
                #     self.send_error(400, **error_info)
                    raise HTTPError(400)
            else:
                gen_log.error('content-type is not application/json.')
                raise HTTPError(400)

    @property
    def db(self):
        return self.application.db

    @property
    def comm_model(self):
        from model.register import CommonModel
        return CommonModel(self.application.db)

    def response_status(self, code=(500, 'Server Error!')):
        print code
        self.set_status(code[0], code[1])


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.set_header('Content-Type', 'application/json')

    @property
    def db(self):
        return self.application.db

    @property
    def db_auth(self):
        return self.application.db_auth

    @property
    def register_model(self):
        from model.register import RegisterModel
        return RegisterModel(self.application.db, self.application.db_auth)

    def initialize(self):
        pass

    def prepare(self):
        # args = self.request.query_arguments
        # data = {}
        # for a in args:
        #     data[a] = self.get_argument(a)
        # return data
        pass

    @property
    def body_json(self):
        if self.request.method in ('POST', 'DELETE', 'PATCH', 'PUT', 'OPTIONS'):
            content_type = self.request.headers['Content-Type']
            if content_type == 'application/json':
                try:
                    return json_decode(self.request.body)
                except ValueError, e:
                    gen_log.debug('decode track data error. e=%s' % e)
                    raise HTTPError(400)
            else:
                gen_log.debug('content-type is not application/json.')
                raise HTTPError(400)

    def response_status(self, code=(500, 'Server Error!')):
        status_code = code[0]
        reason = code[1]

        self.set_status(status_code, reason=reason)
        # self.set_status(code[0], code[1])
        try:
            self.write_error(status_code)
        except Exception:
            app_log.error("Uncaught exception in write_error", exc_info=True)
        if not self._finished:
            self.finish()

    # def send_error(self, status_code=500, **kwargs):
    #     if self._headers_written:
    #         gen_log.error("Cannot send error response after headers written")
    #         if not self._finished:
    #             self.finish()
    #         return
    #     self.clear()
    #
    #     reason = constants.responses.get(status_code, 'Unknown')
    #     self.set_status(status_code, reason=reason)
    #     try:
    #         self.write_error(status_code, **kwargs)
    #     except Exception:
    #         app_log.error("Uncaught exception in write_error", exc_info=True)
    #     if not self._finished:
    #         self.finish()