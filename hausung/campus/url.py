#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-10 15:22
# Copyright 2014 LEO

from auth import GetAuthCodeHandler
from auth import RegisterHandler
from auth import LoginHandler
from common import BundleCommunityHandler

url = [
    (r"/auth-device/get-auth-code", GetAuthCodeHandler),
    (r"/auth-device/register", RegisterHandler),
    (r"/auth-device/login", LoginHandler),
    (r"/device/common/bundle-community", BundleCommunityHandler),
]
