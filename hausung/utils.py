#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-10 09:29
# Copyright 2014 LEO

import hashlib
import random
import string


def sha1(data):
    if data is None:
        return ''
    hash_sha1 = hashlib.sha1(data)
    return hash_sha1.hexdigest()


def md5(data):
    if data is None:
        return ''
    hash_sha1 = hashlib.md5(data)
    return hash_sha1.hexdigest()


#处理大文件, 用MD5来检测两个文件是否相同
def get_file_md5(f):
    m = hashlib.md5()

    while True:
        data = f.read(10240)
        if not data:
            break

        m.update(data)
    return m.hexdigest()


def gen_auth_code(length=6):
    """
    简短地生成随机密码，包括大小写字母、数字，可以指定密码长度
    生成随机验证码
    python3中为string.ascii_letters,而python2下则可以使用string.letters和string.ascii_letters
    """
    # chars = string.ascii_letters + string.digits
    chars = string.digits
    return ''.join([random.choice(chars) for i in range(length)])#得出的结果中字符会有重复的
    #return ''.join(random.sample(chars, 15))#得出的结果中字符不会有重复的


def set_status(tuple):
    print tuple[0], tuple[1]


def main():
    error = (1000, "23423")

    set_status(error)
    #生成10个随机密码
    for i in range(10):
        #密码的长度为15
        print gen_auth_code()


if __name__ == "__main__":
    main()

# with open('/home/xw/Documents/test_data/default_avatar.jpg', 'r') as f:
#     file_md5 = get_file_md5(f)
#     print file_md5