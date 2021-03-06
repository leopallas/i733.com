#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-10 16:44
# Copyright 2014 LEO

ERR_JSON = (10000, 'decode json error')
PHONE_ALREADY_REGISTER = (10001, 'phone is already register')
PHONE_NOT_PAIR_AUTH_CODE = (10002, 'Phone is not pair with auth code')
AUTH_CODE_NOT_CORRECT = (10003, 'Auth Code is not correct')
AUTH_CODE_EXPIRED = (10004, 'Auth Code is already expired')
USERNAME_OR_PASSWORD_EMPTY = (10005, 'username or password is not empty')
USER_ALREADY_REGISTER = (10006, 'user is not register')
USER_PASSWORD_ERROR = (10007, 'password is wrong')

URL_PARAMETERS_NOT_CORRECT = (10008, 'parameters of url not correct')

errorcodes = {
    9000: 'Content-Type is not application/json',

    10000: 'Decode json error',
    10001: 'Phone No. is already register',
    10002: 'Phone No. is not pair with auth code',
    10003: 'Auth Code is not correct',
    10004: 'Auth Code is already expired',
    10005: 'Username or password is not empty',
    10006: 'User is not register',
    10007: 'Password is wrong',
    10008: 'Parameters of url not correct',
    10009: 'Token is not correct'
}

responses = {
    100: 'Continue',
    101: 'Switching Protocols',

    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    203: 'Non-Authoritative Information',
    204: 'No Content',
    205: 'Reset Content',
    206: 'Partial Content',

    300: 'Multiple Choices',
    301: 'Moved Permanently',
    302: 'Found',
    303: 'See Other',
    304: 'Not Modified',
    305: 'Use Proxy',
    306: '(Unused)',
    307: 'Temporary Redirect',

    400: 'Bad Request',
    401: 'Unauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    406: 'Not Acceptable',
    407: 'Proxy Authentication Required',
    408: 'Request Timeout',
    409: 'Conflict',
    410: 'Gone',
    411: 'Length Required',
    412: 'Precondition Failed',
    413: 'Request Entity Too Large',
    414: 'Request-URI Too Long',
    415: 'Unsupported Media Type',
    416: 'Requested Range Not Satisfiable',
    417: 'Expectation Failed',

    500: 'Internal Server Error',
    501: 'Not Implemented',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'HTTP Version Not Supported',

    9000: 'Content-Type is not application/json',
    10000: 'Decode json error',
    10001: 'Phone No. is already register',
    10002: 'Phone No. is not pair with auth code',
    10003: 'Auth Code is not correct',
    10004: 'Auth Code is already expired',
    10005: 'Username or password is not empty',
    10006: 'User is not register',
    10007: 'Password is wrong',
    10008: 'Parameters of url not correct',
    10009: 'Token is not correct'
}