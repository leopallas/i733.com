#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-19 12:02
# Copyright 2014 LEO

#coding:utf-8
import time


def timeit(func):
    """
    对普通方法的装饰。比如，要计算一个一个方法执行的时间.
    """
    def wrapper(*args, **kv):
        start = time.clock()
        print '开始执行'
        func(*args, **kv)
        end = time.clock()
        print '花费时间:', end - start

    return wrapper


@timeit
def foo():
    print 'in foo()'


class MySpendTime(object):
    """
    对在 class 类中的方法的装饰，不需要给参数的情况
    """
    def __init__(self):
        pass

    @timeit
    def foo(self):
        print 'in foo()'


def UpdateUI(msg, step):
    """
    对在 class 类中的方法的装饰，需要给参数的情况
    """
    print u"内容:", msg
    print u"步骤:到第%s步了" % step

    def dec(func):
        def wapper(self, *args, **kwargs):
            func(self, *args, **kwargs)

        return wapper

    return dec


class Command(object):
    def Excute(self):
        self.Work1st()
        self.Work2nd()
        self.Work3rd()

    @UpdateUI("开始第一步", "1")
    def Work1st(self):
        print "Work1st"

    @UpdateUI("开始第二步", 2)
    def Work2nd(self):
        print "Work2nd"

    @UpdateUI("开始第三步", 3)
    def Work3rd(self):
        print "Work3rd"


if __name__ == '__main__':
    foo()

    spendtime = MySpendTime()
    spendtime.foo()

    command = Command()
    command.Excute()
