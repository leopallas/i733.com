#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-10 15:22
# Copyright 2014 LEO

from handler.login import GetAuthCodeHandler
from handler.login import RegisterHandler
from handler.login import LoginHandler
from handler.common import BundleCommunityHandler, GetDistrictsHandler

url = [
    (r"/auth-device/get-auth-code", GetAuthCodeHandler),
    (r"/auth-device/register", RegisterHandler),
    (r"/auth-device/login", LoginHandler),
    (r"/device/common/bundle-community", BundleCommunityHandler),
    (r"/device/common/get-districts", GetDistrictsHandler),
]
