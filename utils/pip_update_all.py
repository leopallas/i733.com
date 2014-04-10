#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:    Leo XU     <leopallas@gmail.com>
# Version:   1.0
# Create On: Sat Apr  5 12:15:37 2014
# Copyright 2014 LEO

import pip
from subprocess import call
 
for dist in pip.get_installed_distributions():
    call("sudo pip install --upgrade " + dist.project_name, shell=True)
