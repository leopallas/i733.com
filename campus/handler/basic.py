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
from tornado.log import access_log
from tornado.web import MissingArgumentError

import util
from campus.model.register import RegisterModel, CommonModel


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.set_header('Content-Type', 'application/json')
        self._auth_request = False
        self._usr_id = None
        self._json_args = None

    @property
    def db(self):
        return self.application.db

    @property
    def model_register(self):
        return RegisterModel(self.application.db)

    @property
    def model_comm(self):
        return CommonModel(self.application.db)

    @property
    def get_usr_id(self):
        return self._usr_id

    def initialize(self):
        pass

    def on_finish(self):
        pass

    def prepare(self):
        if self._auth_request:
            self._usr_id = self.validation_url_sign()

    def load_json(self):
        """Load JSON from the request body and store them in
        self.request.arguments, like Tornado does by default for POSTed form
        parameters.

        If JSON cannot be decoded, raises an HTTPError with status 400.
        """
        if self.request.headers['Content-Type'] == 'application/json':
            try:
                self._json_args = json_decode(self.request.body)
            except ValueError:
                msg = "Could not decode JSON: %s" % self.request.body
                access_log.error(msg)
                raise tornado.web.HTTPError(400, msg)
        else:
            access_log.error('Content-Type is not application/json.')
            raise tornado.web.HTTPError(400)

    def get_json_argument(self, name, default=None):
        """Find and return the argument with key 'name' from JSON request data.
        Similar to Tornado's get_argument() method.
        """
        if default is None:
            default = self._ARG_DEFAULT
        if not self._json_args:
            self.load_json()
        if name not in self._json_args:
            if default is self._ARG_DEFAULT:
                access_log.debug("Missing argument '%s'" % name)
                raise tornado.web.MissingArgumentError(name)
            access_log.debug("Returning default argument %s, as we couldn't find "
                    "'%s' in %s" % (default, name, self.request.arguments))
            return default
        arg = self._json_args[name]
        access_log.debug("Found '%s': %s in JSON arguments" % (name, arg))
        return arg

    def validation_url_sign(self):
        # args = self.request.query_arguments
        # if not args.get('tm') or not args.get('nonce') or not args.get('au') or not args.get('tkn'):
        #     access_log.error('Missing parameter tm or nonce or au or tkn')
        #     raise MissingArgumentError('tm or nonce or au or tkn')
        # tm = self.get_argument('tm')
        # nonce = self.get_argument('nonce')
        au = self.get_argument('au')
        tkn = self.get_argument('tkn')

        #根据SECRET_TOKEN从数据库中取得签名的Key
        authkey = self.db.get("SELECT SIGNATURE_KEY, USR_ID FROM auth_key where SECRET_TOKEN = %s", tkn)
        if not authkey:
            raise tornado.web.HTTPError(400)
        # 验证签名
        uri = '%s+%s+%s+%s' % (
            self.request.method, self.request.protocol, self.request.path, url_unescape(self.request.query))
        uri = uri.replace('&au=' + au, '')
        uri = uri.replace('&tkn=' + tkn, '')
        sign = util.signature(authkey['SIGNATURE_KEY'], uri)
        if sign != au:
            raise tornado.web.HTTPError(400)
        return authkey['USR_ID']

    def response_status(self, code=(500, 'Server Error!')):
        status_code = code[0]
        reason = code[1]

        self.set_status(status_code, reason=reason)
        # self.set_status(code[0], code[1])
        try:
            self.write_error(status_code)
        except Exception:
            access_log.error("Uncaught exception in write_error", exc_info=True)
        if not self._finished:
            self.finish()

    def response_status(self, code=(500, 'Server Error!')):
        print code
        self.set_status(code[0], code[1])


class AuthBaseHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(AuthBaseHandler, self).__init__(application, request, **kwargs)
        self._auth_request = True
