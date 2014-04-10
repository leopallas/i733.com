#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-10 15:39
# Copyright 2014 LEO
import time

from hausung import utils
from basic import BaseHandler
from constants import PHONE_ALREADY_REGISTER, PHONE_NOT_PAIR_AUTH_CODE, AUTH_CODE_NOT_CORRECT, AUTH_CODE_EXPIRED, \
    USERNAME_OR_PASSWORD_EMPTY, USER_ALREADY_REGISTER, USER_PASSWORD_ERROR


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
                self.response_status(PHONE_ALREADY_REGISTER)
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
            self.response_status(PHONE_NOT_PAIR_AUTH_CODE)
            return
        else:
            if register_doc['authCode'] != register['authCode']:
                self.response_status(AUTH_CODE_NOT_CORRECT)
                return
            if (time.time() - register_doc['createDt']) > 1200:
                self.response_status(AUTH_CODE_EXPIRED)
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
            self.response_status(USERNAME_OR_PASSWORD_EMPTY)
            return
        coll = self.db.account
        account_doc = coll.find_one({'username': account['username']})
        if account_doc:
            self.response_status(USER_ALREADY_REGISTER)
            return
        if account_doc['password'] != utils.sha1(account['password']):
            self.response_status(USER_PASSWORD_ERROR)

        del account_doc["_id"]
        self.write(account_doc)