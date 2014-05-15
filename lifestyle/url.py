#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-10 15:22
# Copyright 2014 LEO

from lifestyle.handlers import GetAuthCodeHandler
from lifestyle.handlers import RegisterHandler

url = [
    (r"/device/barter/get-barter-categories", GetAuthCodeHandler),
    (r"/register", RegisterHandler),
]
