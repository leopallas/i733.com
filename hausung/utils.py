#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-10 09:29
# Copyright 2014 LEO

import hashlib
import string
import random


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

import hmac
import uuid
import base64
from Crypto.Cipher import DES
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto import Random


def gen_auth_key(u=None):
    if u is None:
        u = uuid.uuid1()

    u = str(u)
    s = hashlib.sha1()
    s.update(u)
    secret_token = base64.b64encode(s.digest())

    obj = DES.new(Random.new().read(8), DES.MODE_ECB)
    signature_key = base64.b64encode(obj.encrypt(''.join(random.choice(u) for i in range(8))))
    # signature_key = base64.b64encode(obj.encrypt(base64.b64encode(os.urandom(12))))
    return secret_token, signature_key


def signature(key, text):
    h = hmac.new(key, text, hashlib.sha1)
    sig = base64.b64encode(h.digest()).strip()
    return sig

import os


def main():

    # key = ElGamal.generate(100, Random.new().read)
    # print key
    u = '2d157330-35cc-426c-b2c5-64f410be1bdf'
    key = gen_auth_key()
    print key
    sign = signature(key[1], 'command=deployVirtualMachine&serviceOfferingId=1&diskOfferingId=1&templateId=2')
    from urllib import quote
    print quote(sign)
    print quote(key[0])

    # des.setKey(os.urandom(24))
    # print des.getKey()

    print len(base64.b64encode(os.urandom(12)))
    # key = u
    # iv = Random.new.read(DES.block_size)
    # ciper = DES.new(key, DES.MODE_CBC, iv)


    obj = DES.new(Random.new().read(8), DES.MODE_ECB)
    print '******************************'
    u = ''.join(u.split('-'))
    print u
    print len(u)
    print u[0:8]
    xx = obj.encrypt(u[0:8])
    print xx
    print base64.b64encode(xx)
    print '******************************'
    # >>> from Crypto.Cipher import DES3
    # >>> from Crypto import Random
    # >>>
    # >>> key = b'Sixteen byte key'
    # >>> iv = Random.new().read(DES3.block_size)
    # >>> cipher = DES3.new(key, DES3.MODE_OFB, iv)
    # >>> plaintext = b'sona si latine loqueris '
    # >>> msg = iv + cipher.encrypt(plaintext)
    # iv = Random.new().read
    # print iv
    # print DES.new(u, DES.MODE_CBC, iv)
    print base64.b64encode(hashlib.sha1(str(random.getrandbits(256))).digest())


    rng = Random.new().read
    RSAkey = RSA.generate(1024, rng)
    hash = MD5.new(u).digest()
    sign = RSAkey.sign(hash, rng)
    print sign
    print '---------------------'
    print RSAkey.publickey()
    print RSAkey.key
    print '---------------------'
    print RSAkey.verify(hash, sign)
    print RSAkey.verify(hash[:-1], sign)

    # rng = Random.new().read
    # RSAkey = DSA.generate(1024, rng)
    # print base64.b64encode(RSAkey)
    # >>> import hashlib
    # >>> m = hashlib.md5()
    # >>> m.update("Nobody inspects")
    # >>> m.update(" the spammish repetition")
    # >>> m.digest()

    # set_status(error)
    # #生成10个随机密码
    # for i in range(10):
    #     #密码的长度为15
    #     print gen_auth_code()
    sig=base64.encodestring(hmac.new('oV9j0cxQ254=','command=deployVirtualMachine&serviceOfferingId=1&diskOfferingId=1&templateId=2',hashlib.sha1).digest()).strip()
    print sig
# uuid == 2d157330-35cc-426c-b2c5-64f410be1bdf
# /SxRgLw+kW4= :::::: 1qoUzAumPU3jXpg9OAr129p8iJY=
# 4yZ/+66AI0A= :::::: 1qoUzAumPU3jXpg9OAr129p8iJY=

if __name__ == "__main__":
    main()

# with open('/home/xw/Documents/test_data/default_avatar.jpg', 'r') as f:
#     file_md5 = get_file_md5(f)
#     print file_md5