#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-26 17:07
# Copyright 2014 LEO

from hausung.campus import util


class RegisterModel():
    def __init__(self, db, db_auth):
        self._db = db
        self._db_auth = db_auth

    def get_register_by_auth_code(self, phone):
        register = self._db_auth.get('SELECT REG_HP, REG_AUTH_CODE, REG_DT, REG_IND FROM register where REG_HP = %s', phone)
        return register

    def get_user(self, username):
        user = self._db_auth.get('SELECT * FROM user where USR_NAME = %s', username)
        return user

    def change_auth_key(self, usrid):
        self._db.execute('DELETE FROM auth_key WHERE USR_ID=%s', usrid)
        authkey = util.gen_auth_key()
        self._db.execute('INSERT INTO auth_key(SECRET_TOKEN, SIGNATURE_KEY, USR_ID) VALUES (%s, %s, %s)', authkey[0],
                        authkey[1], usrid)
        return authkey

    def update_login_user_extend(self, usrid, sn, devicetype):
        self._db.execute('UPDATE user_extend SET USR_DEVICE_SER_NO=%s, USR_DEVICE_TYPE=%s', sn, devicetype)
        user_extend = self._db.get('SELECT * FROM user_extend WHERE USR_ID=%s', usrid)
        return user_extend

    def get_servers(self):
        return self._db.query('SELECT ADDRESS as address, PORT as port, TYPE as type,  WEB_CONTEXT as webContext, HTTPS as https FROM server')


class CommonModel:
    def __init__(self, db):
        self._db = db

    def bundle_community(self, comid, usrid):
        self._db.execute('UPDATE user_extend SET COM_ID=%s WHERE USR_ID=%s', comid, usrid)