#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-10 09:29
# Copyright 2014 LEO

#-------------------------------------------- HASH -----------------------------------------
import hashlib
import string
import random
import hmac
import uuid
import base64


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

#-------------------------------------------- 签名与加密 -----------------------------------------
from Crypto.Cipher import DES
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto import Random


def gen_auth_code(length=6):
    """
    简短地生成随机密码，包括大小写字母、数字，可以指定密码长度
    生成随机验证码
    python3中为string.ascii_letters,而python2下则可以使用string.letters和string.ascii_letters
    """
    # chars = string.ascii_letters + string.digits
    chars = string.digits
    return ''.join([random.choice(chars) for i in range(length)])  #得出的结果中字符会有重复的
    #return ''.join(random.sample(chars, 15))#得出的结果中字符不会有重复的


def gen_auth_key(u=None):
    """
    生成私密令牌与签名Key
    """
    if u is None:
        u = uuid.uuid1()
    #秘密令牌
    u = str(u)
    s = hashlib.sha1()
    s.update(u)
    secret_token = base64.b64encode(s.digest())
    #签名Key
    obj = DES.new(Random.new().read(8), DES.MODE_ECB)
    signature_key = base64.b64encode(obj.encrypt(''.join(random.choice(u) for i in range(8))))
    return secret_token, signature_key


def signature(key, text):
    """
    用传入的key对文本进行签名
    """
    if isinstance(key, unicode):
        key = str(key)

    key = base64.b64decode(key)
    h = hmac.new(key, text.encode('utf-8'), hashlib.sha1)
    my_signature = base64.b64encode(h.digest()).strip()
    return my_signature


# --------------------------------------------- 日期相关方法 --------------------------------------------
import datetime
import time


def datetime_toString(dt):
    """把datetime转成字符串"""
    return dt.strftime("%Y-%m-%d")


def string_toDatetime(string):
    """把字符串转成datetime"""
    return datetime.datetime.strptime(string, "%Y-%m-%d")


def string_toTimestamp(strTime):
    """把字符串转成时间戳形式"""
    return time.mktime(string_toDatetime(strTime).timetuple())


def timestamp_toString(stamp):
    """把时间戳转成字符串形式"""
    return time.strftime("%Y-%m-%d-%H", time.localtime(stamp))


def datetime_toTimestamp(dateTime):
    """把datetime类型转外时间戳形式"""
    return time.mktime(dateTime.timetuple())


def substract_DateTime(dateStr1, dateStr2):
    """ 返回两个日期之间的差 """
    d1 = string_toDatetime(dateStr1)
    d2 = string_toDatetime(dateStr2)
    return d2 - d1


def substract_TimeStamp(dateStr1, dateStr2):
    """ 两个日期的 timestamp 差值 """
    ts1 = string_toTimestamp(dateStr1)
    ts2 = string_toTimestamp(dateStr2)
    return ts1 - ts2


def compare_dateTime(dateStr1, dateStr2):
    """两个日期的比较, 当然也可以用timestamep方法比较,都可以实现."""
    date1 = string_toDatetime(dateStr1)
    date2 = string_toDatetime(dateStr2)
    return date1.date() > date2.date()


def dateTime_add(dateStr, days=0, hours=0, minutes=0):
    """ 指定日期加上 一个时间段，天，小时，或分钟之后的日期 """
    date1 = string_toDatetime(dateStr)
    return date1 + datetime.timedelta(days=days, hours=hours, minutes=minutes)


def increment_month(when):
    """ 根据当前日期，对年月进行加减的方法 """
    import calendar

    days = calendar.monthrange(when.year, when.month)[1]
    return when + datetime.timedelta(days=days)


def get_datetime_from_date_now(datenow, now=datetime.datetime.now()):
    """通过date对象和time对象构造出一个新的datetime"""
    return datetime.datetime.combine(datenow, datetime.time(now.hour, now.minute, now.second))


def main():
    print get_datetime_from_date_now('2014-03-04')

    import base64
    import uuid

    print base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)

    print substract_DateTime('2012-12-12', '2012-01-01')
    #-346 days, 0:00:00
    print substract_DateTime('2012-12-12', '2012-01-01').days
    #-346
    print substract_TimeStamp('2012-12-12', '2012-01-01')
    #29894400.0
    print substract_TimeStamp('2012-12-12', '2012-01-01') / (24 * 60 * 60), '天'
    #346.0 天
    print compare_dateTime('2012-12-12', '2012-01-01')
    #True
    print dateTime_add('2012-12-12', days=10, hours=5, minutes=10)
    #2012-12-22 05:10:00

    now = datetime.datetime.now()
    print 'It is now %s' % now
    print 'In a month, it will be %s' % increment_month(now)

    print 'zvCVb5B01qgCo2OxgZBQGie7yAY='
    # uri = 'GET+http+/device/barter/get-barter-categories+tm=1397705800365&nonce=-131075622'
    uri = 'GET+http+/device/barter/get-barter-categories+tm=1397705800365&nonce=-131075622'

    key = {'SIGNATURE_KEY': u'iu+SAZ2wj0A='}
    print signature(key['SIGNATURE_KEY'], uri)

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

    import os

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
    sig = base64.encodestring(
        hmac.new('oV9j0cxQ254=', 'command=deployVirtualMachine&serviceOfferingId=1&diskOfferingId=1&templateId=2',
                 hashlib.sha1).digest()).strip()
    print sig


if __name__ == "__main__":
    main()

    # with open('/home/xw/Documents/test_data/default_avatar.jpg', 'r') as f:
    #     file_md5 = get_file_md5(f)
    #     print file_md5