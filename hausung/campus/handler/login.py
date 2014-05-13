#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-10 15:39
# Copyright 2014 LEO
import time
from datetime import datetime, timedelta

from tornado.escape import json_encode
from bson.objectid import ObjectId

from hausung.campus import util
from basic import BaseHandler
from errorcodes import PHONE_ALREADY_REGISTER, PHONE_NOT_PAIR_AUTH_CODE, AUTH_CODE_NOT_CORRECT, AUTH_CODE_EXPIRED, \
    USERNAME_EMPTY, PASSWORD_ERROR


class GetAuthCodeHandler(BaseHandler):
    def get(self):
        phone = self.get_argument('phone')

        register = self.model_register.get_register_by_phone(phone)
        auth_code = util.gen_auth_code()
        if register is not None:
            if register['REG_IND'] == 2:
                self.response_status(PHONE_ALREADY_REGISTER)
                return
            else:
                self.model_register.update_auth_code(phone, auth_code)
        else:
            self.model_register.insert_register(phone, auth_code)
        #TODO... send sms to phone with auth code


class RegisterHandler(BaseHandler):
    def post(self):
        phone = self.get_json_argument('phone')
        auth_code = self.get_json_argument('authCode')
        pwd = self.get_json_argument('pwd')

        register = self.model_register.get_register_by_phone(phone)
        if register is None:
            self.response_status(PHONE_NOT_PAIR_AUTH_CODE)
            return
        else:
            if register['REG_AUTH_CODE'] != auth_code:
                self.response_status(AUTH_CODE_NOT_CORRECT)
                return

            now = datetime.now()
            # auth code of fetch time must be not greater than 2 minutes
            reg_dt = register['REG_DT'] + timedelta(minutes=2)
            if now > reg_dt:
                self.response_status(AUTH_CODE_EXPIRED)
                return
            # update register, let register indicator change to yes
            self.model_register.update_register_ind(phone)

            usr_id = ObjectId()
            self.model_register.insert_user(usr_id, phone, pwd, now)

            # 更新到lifestyle
            nickname = phone.encode("utf-8")
            nickname = nickname[0: 3] + '****' + nickname[7: 11]
            self.model_register.update_register_user_extend(nickname, usr_id)


class LoginHandler(BaseHandler):
    def post(self):
        account = self.get_json_argument('user')
        pwd = self.get_json_argument('pwd')
        sn = self.get_json_argument('sn')
        type = self.get_json_argument('type')
        # n = self.request.arguments

        user = self.model_register.get_user(account)
        if not user:
            # self.send_error(USER_NAME_INVALID)
            self.response_status(USERNAME_EMPTY)
            return
        if user['USR_PWD'] != util.sha1(pwd):
            # self.send_error(PASSWORD_ERROR)
            self.response_status(PASSWORD_ERROR)

        if type == u'Android':
            device_type = 2
        elif type == u'iOS':
            device_type = 3

        usr_id = user['USR_ID']
        # 更换authKey
        authkey = self.model_register.change_auth_key(usr_id)
        # 更新登录信息user_extend
        user_extend = self.model_register.update_login_user_extend(usr_id, sn, device_type)
        servers = self.model_register.get_servers()
        for server in servers:
            if server['https'] == 1:
                server['https'] = True
            else:
                server['https'] = False

        result = {
            "usrId": user_extend['USR_ID'],
            "nickname": user_extend['USR_NICKNAME'],
            "usrType": user['USR_TYPE'],
            "servers": servers,
            "avatar": "http://192.168.1.160:18080/img/82/24/09/533e0975559a03d62fd742cc/533e0975559a03d62fd742cc.jpg",
            "openShopInd": user_extend['OPEN_SHOP_IND'],
            "token": authkey[0],
            "key": authkey[1],
            "sdt": int(time.time())
        }
        if user_extend['COM_ID']:
            result['comId'] = user_extend['COM_ID']
        self.write(json_encode(result))


