#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-26 10:14
# Copyright 2014 LEO

sql = [
    ("getSignature", "SELECT SIGNATURE_KEY FROM auth_key where SECRET_TOKEN = %s"),
    ("", ""),
]