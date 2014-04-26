#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-26 13:41
# Copyright 2014 LEO

from datetime import datetime
import time


#把datetime转成字符串
def datetime_toString(dt):
    return dt.strftime("%Y-%m-%d-%H")


#把字符串转成datetime
def string_toDatetime(string):
    return datetime.strptime(string, "%Y-%m-%d-%H")


#把字符串转成时间戳形式
def string_toTimestamp(strTime):
    return time.mktime(string_toDatetime(strTime).timetuple())


#把时间戳转成字符串形式
def timestamp_toString(stamp):
    return time.strftime("%Y-%m-%d-%H", time.localtime(stamp))


#把datetime类型转外时间戳形式
def datetime_toTimestamp(dt):
    return time.mktime(dt.timetuple())


def main():
    print datetime_toString(datetime.now())
    print datetime_toTimestamp(datetime.now())


if __name__ == "__main__":
    main()