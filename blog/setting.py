#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-30 11:31
# Copyright 2014 LEO


import os.path

DEBUG = True
LISTEN_PORT = 8080

# Database Setting
if DEBUG:
    DB_CONNECT_STRING = 'mysql://root:root@localhost:3306/blog2?charset=utf8'
else:
    #import sae.const
    #sae.const.MYSQL_DB      # 数据库名
    #sae.const.MYSQL_USER    # 用户名
    #sae.const.MYSQL_PASS    # 密码
    #sae.const.MYSQL_HOST    # 主库域名（可读写）
    #sae.const.MYSQL_PORT    # 端口，类型为，请根据框架要求自行转换为int
    #sae.const.MYSQL_HOST_S  # 从库域名（只读）
    #DB_CONNECT_STRING = 'mysql://'+sae.const.MYSQL_USER+':'+sae.const.MYSQL_PASS+'@'+sae.const.MYSQL_HOST+':'+sae.const.MYSQL_PORT+'/'+sae.const.MYSQL_DB+'?charset=utf8'
    DB_CONNECT_STRING = 'mysql://root:root@localhost:3306/blog2?charset=utf8'
DB_ECHO = True
DB_ENCODING = 'utf-8'
POOL_RECYCLE = 5

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(CURRENT_PATH)
ROOT_PATH = os.path.dirname(PROJECT_PATH)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# 使用SAE Storage服务保存上传的附件，需在SAE管理面板创建
STORAGE_DOMAIN_NAME = 'upload'

BASE_PATH = os.path.dirname(__file__)
# the address path which the file will be uploaded in
FILE_MANAGER_PATH = os.path.join(BASE_PATH, u"static/upload/")

# the app will use this template
CURRENT_TEMPLATE_NAME = "default"

ALLOWED_HOSTS = []
LANGUAGE_CODE = 'en-us'

# Tornado Application Parameter Setting
BLOG_TITLE = u"Leo's Blog"
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_PATH = os.path.join(CURRENT_PATH, 'static')
TEMPLATE_PATH = os.path.join(CURRENT_PATH, 'templates')
COOKIE_SECRET = "88oETzKXQAGaYdkL6gEmGeJJFYYh7EQnp3XdTP1o/Vo="
XSRF_COOKIES = True
LOGIN_URL = "/admin/login"