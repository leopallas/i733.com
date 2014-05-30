#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-19 16:27
# Copyright 2014 LEO

# '''示例1: 最简单的函数,表示调用了两次'''
#
# def myfunc():
#     print("myfunc() called.")
#
# myfunc()

# '''示例2: 替换函数(装饰)
# 装饰函数的参数是被装饰的函数对象，返回原函数对象
# 装饰的实质语句: myfunc = deco(myfunc)'''
#
# def deco(func):
#     print("before myfunc() called.")
#     func()
#     print("  after myfunc() called.")
#     return func
#
# def myfunc():
#     print(" myfunc() called.")
#
# myfunc = deco(myfunc)

# '''示例3: 使用语法糖@来装饰函数，相当于“myfunc = deco(myfunc)”
# 但发现新函数只在第一次被调用，且原函数多调用了一次'''
# def deco(func):
#     print("before myfunc() called.")
#     func()
#     print("  after myfunc() called.")
#     return func
#
# @deco
# def myfunc():
#     print(" myfunc() called.")
#
# myfunc()
# myfunc()

# '''示例4: 使用内嵌包装函数来确保每次新函数都被调用，
# 内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''
# def deco(func):
#     def _deco():
#         print("before myfunc() called.")
#         ret = func()
#         print("  after myfunc() called.")
#         # 不需要返回func，实际上应返回原函数的返回值
#         return ret
#     return _deco
#
# @deco
# def myfunc():
#     print(" myfunc() called.")
#     return 'ok'
#
# myfunc()
# myfunc()

# '''示例5: 对带参数的函数进行装饰，
# 内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''
# def deco(func):
#     def _deco(a, b):
#         print("before myfunc() called.")
#         ret = func(a, b)
#         print(" after myfunc() called. result: %s" % ret)
#         return ret
#     return _deco
#
# @deco
# def myfunc(a, b):
#     print(" myfunc(%s,%s) called." % (a, b))
#     return a + b
#
# myfunc(1, 2)
# myfunc(3, 4)

# '''示例6: 对参数数量不确定的函数进行装饰，
# 参数用(*args, **kwargs)，自动适应变参和命名参数'''
# def deco(func):
#     def _deco(*args, **kwargs):
#         print("before %s called." % func.__name__)
#         ret = func(*args, **kwargs)
#         print("  after %s called. result: %s" % (func.__name__, ret))
#         return ret
#     return _deco
#
# @deco
# def myfunc(a, b):
#     print(" myfunc(%s,%s) called." % (a, b))
#     return a+b
#
# @deco
# def myfunc2(a, b, c):
#     print(" myfunc2(%s,%s,%s) called." % (a, b, c))
#     return a+b+c
#
# myfunc(1, 2)
# myfunc(3, 4)
# myfunc2(1, 2, 3)
# myfunc2(3, 4, 5)



# """示例7: 在示例4的基础上，让装饰器带参数，和上一示例相比在外层多了一层包装。装饰函数名实际上应更有意义些"""
# def deco(arg):
#     def _deco(func):
#         def __deco():
#             print("before %s called [%s]." % (func.__name__, arg))
#             func()
#             print("  after %s called [%s]." % (func.__name__, arg))
#         return __deco
#     return _deco
#
# @deco("mymodule")
# def myfunc():
#     print(" myfunc() called.")
#
# @deco("module2")
# def myfunc2():
#     print(" myfunc2() called.")
#
# myfunc()
# myfunc2()


# """示例8: 装饰器带类参数"""
# class locker:
#     def __init__(self):
#         print("locker.__init__() should be not called.")
#
#     @staticmethod
#     def acquire():
#         print("locker.acquire() called.（这是静态方法）")
#
#     @staticmethod
#     def release():
#         print("  locker.release() called.（不需要对象实例）")
#
# def deco(cls):
#     '''cls 必须实现acquire和release静态方法'''
#     def _deco(func):
#         def __deco():
#             print("before %s called [%s]." % (func.__name__, cls))
#             cls.acquire()
#             try:
#                 return func()
#             finally:
#                 cls.release()
#         return __deco
#     return _deco
#
# @deco(locker)
# def myfunc():
#     print(" myfunc() called.")
#
# myfunc()
# myfunc()

# # -*- coding:gbk -*-
# """装饰器带类参数，并分拆公共类到其他py文件中，同时演示了对一个函数应用多个装饰器"""
#
#
# class mylocker:
#     def __init__(self):
#         print("mylocker.__init__() called.")
#
#     @staticmethod
#     def acquire():
#         print("mylocker.acquire() called.")
#
#     @staticmethod
#     def unlock():
#         print("  mylocker.unlock() called.")
#
#
# class lockerex(mylocker):
#     @staticmethod
#     def acquire():
#         print("lockerex.acquire() called.")
#
#     @staticmethod
#     def unlock():
#         print("  lockerex.unlock() called.")
#
#
# def lockhelper(cls):
#     """cls 必须实现acquire和release静态方法"""
#
#     def _deco(func):
#         def __deco(*args, **kwargs):
#             print("before %s called." % func.__name__)
#             cls.acquire()
#             try:
#                 return func(*args, **kwargs)
#             finally:
#                 cls.unlock()
#
#         return __deco
#
#     return _deco
#
# # -*- coding:gbk -*-
# '''示例9: 装饰器带类参数，并分拆公共类到其他py文件中
# 同时演示了对一个函数应用多个装饰器'''
#
# # from mylocker import *
#
# class example:
#     @lockhelper(mylocker)
#     def myfunc(self):
#         print(" myfunc() called.")
#
#     @lockhelper(mylocker)
#     @lockhelper(lockerex)
#     def myfunc2(self, a, b):
#         print(" myfunc2() called.")
#         return a + b

class route2app(object):
    _routes = []

    def __init__(self, uri, name=None):
        self._uri = uri
        self.name = name

    def __call__(self, _handler):
        """gets called when we class decorate"""
        name = self.name or _handler.__name__
        if not self._uri:
            pattern = r'(?P<relpath>/.*)?'
        else:
            pattern = self._uri + r'(?P<relpath>/.*)?'
        self._routes.append(_handler.__name__)
        return _handler

    @classmethod
    def get_routes(klass):
        return klass._routes

from datetime import datetime

@route2app(r'/users')
class BaseHandler(object):
    def __init__(self, *args, **kwargs):
        self.t1 = datetime.datetime.now()
        self.t2 = None

    def on_finish(self):
        self.t2 = datetime.datetime.now()

@route2app(r'/apps')
class ABaseHandler(object):
    def __init__(self, *args, **kwargs):
        self.t1 = datetime.datetime.now()
        self.t2 = None

    def on_finish(self):
        self.t2 = datetime.datetime.now()

# if __name__=="__main__":
    # print route2app.get_routes()
    # a.myfunc()
    # print(a.myfunc())
    # print(a.myfunc2(1, 2))
    # print(a.myfunc2(3, 4))

# from UserDict import UserDict
# class FileInfo(dict):
#     def __init__(self, filename=None):
#         self['name'] = filename


