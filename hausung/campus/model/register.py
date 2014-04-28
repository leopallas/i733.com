#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-26 17:07
# Copyright 2014 LEO

from hausung.campus import util
from datetime import datetime


class RegisterModel():
    def __init__(self, db, db_auth):
        self._db = db
        self._db_auth = db_auth

    def get_register_by_phone(self, phone):
        register = self._db_auth.get('SELECT REG_HP, REG_AUTH_CODE, REG_DT, REG_IND FROM register where REG_HP = %s',
                                     phone)
        return register

    def update_auth_code(self, phone, auth_code):
        self._db_auth.execute('UPDATE register set REG_AUTH_CODE = %s, REG_DT = %s where REG_HP = %s', auth_code,
                              datetime.now(), phone)

    def insert_register(self, phone, auth_code):
        self._db_auth.execute('INSERT INTO register(REG_HP, REG_AUTH_CODE, REG_DT, REG_IND) VALUES (%s, %s, %s, %s)',
                              phone, auth_code, datetime.now(), 1)

    def update_register_ind(self, phone):
        self._db_auth.execute('UPDATE register set REG_IND = 2 where REG_HP = %s', phone)

    def insert_user(self, usr_id, phone, pwd, now):
        self._db_auth.execute('INSERT INTO user(USR_ID, USR_NAME, USR_PWD, USR_TYPE, USR_PHONE, CREATE_DT, UPDATE_DT) '
                              'VALUES (%s, %s, %s, %s, %s, %s, %s)', usr_id, phone, util.sha1(pwd), 1, phone, now, now)

    def get_user(self, username):
        user = self._db_auth.get('SELECT * FROM user where USR_NAME = %s', username)
        return user

    def get_default_img_id(self, type):
        return self._db.get('SELECT ATT_ID as id FROM attachment WHERE ATT_REF_TYPE=%s', type)

    def update_register_user_extend(self, nickname, usr_id):
        img = self.get_default_img_id(10)
        self._db.execute('UPDATE user_extend set USR_NICKNAME=%s, USR_AVATAR=%s, OPEN_SHOP_IND=%s where USR_ID=%s',
                         nickname, img['id'], 1, usr_id)

    def change_auth_key(self, usrid):
        self._db.execute('DELETE FROM auth_key WHERE USR_ID=%s', usrid)
        auth_key = util.gen_auth_key()
        self._db.execute('INSERT INTO auth_key(SECRET_TOKEN, SIGNATURE_KEY, USR_ID) VALUES (%s, %s, %s)', auth_key[0],
                         auth_key[1], usrid)
        return auth_key

    def update_login_user_extend(self, usrid, sn, device_os):
        self._db.execute('UPDATE user_extend SET USR_DEVICE_SER_NO=%s, USR_DEVICE_TYPE=%s', sn, device_os)
        user_extend = self._db.get('SELECT * FROM user_extend WHERE USR_ID=%s', usrid)
        return user_extend

    def get_servers(self):
        return self._db.query('''
                            SELECT ADDRESS as address,
                            PORT as port,
                            TYPE as type,
                            WEB_CONTEXT as webContext,
                            HTTPS as https
                            FROM server
                            ''')


class CommonModel:
    def __init__(self, db):
        self._db = db

    def bundle_community(self, com_id, usr_id):
        self._db.execute('UPDATE user_extend SET COM_ID=%s WHERE USR_ID=%s', com_id, usr_id)

    def get_districts(self):
        self._db.query('''
                SELECT a.ARE_ID, CONCAT('成都市, ', a.ARE_NAME) as ARE_NAME, c.COM_ID, c.COM_NAME
                FROM AREA a
                INNER JOIN (community c)
                ON (c.ARE_ID = a.ARE_ID and c.COM_STATUS = 2)
                WHERE a.ARE_PARENT_ID = '3001'
                AND a.ARE_STATUS = 2''')