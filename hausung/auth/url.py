#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-10 15:22
# Copyright 2014 LEO

from handlers import GetAuthCodeHandler
from handlers import RegisterHandler

url = [
    (r"/get-auth-code", GetAuthCodeHandler),
    (r"/register", RegisterHandler),
]