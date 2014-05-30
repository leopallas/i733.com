#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-28 15:57
# Copyright 2014 LEO
from campus.handler.basic import AuthBaseHandler
# from errorcodes import URL_PARAMETERS_NOT_CORRECT
from tornado.escape import json_encode


class BundleCommunityHandler(AuthBaseHandler):
    def post(self):
        com_id = self.get_argument('comId')
        self.model_comm.bundle_community(com_id, self.get_usr_id)


class GetDistrictsHandler(AuthBaseHandler):
    def post(self):
        self.get()

    def get(self):
        records = self.model_comm.get_districts()
        community_list = [{'comId': r['COM_ID'], 'comName': r['COM_NAME']} for r in records]
        j = json_encode([{'districtName': records[0]['ARE_NAME'], 'communities': community_list}])
        self.write(j)