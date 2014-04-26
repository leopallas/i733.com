#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-26 17:52
# Copyright 2014 LEO
from hausung.campus.basic import AuthBaseHandler
from constants import URL_PARAMETERS_NOT_CORRECT


class BundleCommunityHandler(AuthBaseHandler):
    def post(self):
        args = self.request.query_arguments
        if not args.get('comId'):
            self.response_status(URL_PARAMETERS_NOT_CORRECT)
            return

