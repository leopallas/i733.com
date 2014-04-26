#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-10 15:39
# Copyright 2014 LEO
import time
from datetime import datetime, timedelta

from tornado.web import MissingArgumentError
import util
from basic import BaseHandler
from bson.objectid import ObjectId
from constants import PHONE_ALREADY_REGISTER, PHONE_NOT_PAIR_AUTH_CODE, AUTH_CODE_NOT_CORRECT, AUTH_CODE_EXPIRED, \
    USERNAME_OR_PASSWORD_EMPTY, USER_ALREADY_REGISTER, USER_PASSWORD_ERROR, USERNAME_EMPTY


class GetAuthCodeHandler(BaseHandler):
    def get(self):
        now = datetime.now()
        phone = self.get_argument('phone')
        if not phone:
            raise MissingArgumentError('phone is missing')

        register = self.db_auth.get('SELECT REG_HP, REG_AUTH_CODE, REG_DT, REG_IND FROM register where REG_HP = %s',
                                    phone)
        authcode = util.gen_auth_code()
        if register is not None:
            if register['REG_IND'] == 2:
                self.response_status(PHONE_ALREADY_REGISTER)
                return
            else:
                print register['REG_IND']
                self.db_auth.execute('UPDATE register set REG_AUTH_CODE = %s, REG_DT = %s where REG_HP = %s', authcode,
                                     now, phone)
        else:
            self.db_auth.execute('INSERT INTO register(REG_HP, REG_AUTH_CODE, REG_DT, REG_IND) VALUES (%s, %s, %s, %s)',
                                 phone, authcode, now, 1)
        self.write(authcode)


class RegisterHandler(BaseHandler):
    def post(self):
        data = self.body_json

        phone = data['phone']

        register = self.db_auth.get('SELECT * FROM register WHERE REG_HP = %s', phone)
        now = datetime.now()
        if register is None:
            self.response_status(PHONE_NOT_PAIR_AUTH_CODE)
            return
        else:
            if register['REG_AUTH_CODE'] != data['authCode']:
                self.response_status(AUTH_CODE_NOT_CORRECT)
                return

            regdt = register['REG_DT'] + timedelta(seconds=120)
            if now > regdt:
                self.response_status(AUTH_CODE_EXPIRED)
                return
            # update register, let register indicator change to yes
            self.db_auth.execute('UPDATE register set REG_IND = 2 where REG_HP = %s', phone)

            usrid = ObjectId()
            self.db_auth.execute(
                'INSERT INTO user(USR_ID, USR_NAME, USR_PWD, USR_TYPE, USR_PHONE, CREATE_DT, UPDATE_DT) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                usrid, phone, util.sha1(data['pwd']), 1, phone, now, now)

            # 更新到lifestyle
            nickname = phone.encode("utf-8")
            nickname = nickname[0: 3] + '****' + nickname[7: 11]
            attachment = self.db.get('SELECT ATT_ID FROM attachment WHERE ATT_REF_TYPE=%s', 10)
            self.db.execute('UPDATE user_extend set USR_NICKNAME=%s, USR_AVATAR=%s, OPEN_SHOP_IND=%s where USR_ID=%s',
                            nickname, attachment['ATT_ID'], 1, usrid)


class LoginHandler(BaseHandler):
    def post(self):
        account = self.body_json

        if not account.get('user') or not account.get('pwd') or not account.get('sn') or not account.get('type'):
            self.response_status(USERNAME_OR_PASSWORD_EMPTY)
            return

        user = self.register_model.get_user(account['user'])
        # user = self.db_auth.get('SELECT * FROM user where USR_NAME = %s', account['user'])
        if not user:
            self.response_status(USERNAME_EMPTY)
            return
        if user['USR_PWD'] != util.sha1(account['pwd']):
            self.response_status(USER_PASSWORD_ERROR)

        if account['type'] == u'Android':
            devicetype = 2
        elif account['type'] == u'iOS':
            devicetype = 3

        usrid = user['USR_ID']
        # 更换authKey
        authkey = self.register_model.change_auth_key(usrid)
        # 更新登录信息user_extend
        user_extend = self.register_model.update_login_user_extend(usrid, account['sn'], devicetype)
        servers = self.register_model.get_servers()
        for server in servers:
            if server['https'] == 1:
                server['https'] = True
            else:
                server['https'] = False

        loginresult = {
            "usrId": user_extend['USR_ID'],
            "nickname": user_extend['USR_NICKNAME'],
            "usrType": user['USR_TYPE'],
            "servers": servers,
            "avatar": "http://192.168.1.160:18080/img/82/24/09/533e0975559a03d62fd742cc/533e0975559a03d62fd742cc.jpg",
            "openShopInd": user_extend['OPEN_SHOP_IND'],
            "token": authkey[0],
            "key": authkey[1],
            "sdt": 1398494454857
        }

        if user_extend['COM_ID']:
            loginresult['comId'] = user_extend['COM_ID']

        print loginresult
        self.write(loginresult)


