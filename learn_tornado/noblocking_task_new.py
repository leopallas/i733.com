#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-15 18:24
# Copyright 2014 LEO
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-15 16:46
# Copyright 2014 LEO

# 这个并发库在python3自带在python2需要安装sudo pip install futures
from concurrent.futures import ThreadPoolExecutor
from functools import partial, wraps
import time

import tornado.ioloop
import tornado.web


EXECUTOR = ThreadPoolExecutor(max_workers=4)


def unblock(f):

    @tornado.web.asynchronous
    @wraps(f)
    def wrapper(*args, **kwargs):
        self = args[0]

        def callback(future):
            self.write(future.result())
            self.finish()

        EXECUTOR.submit(
            partial(f, *args, **kwargs)
        ).add_done_callback(
            lambda future: tornado.ioloop.IOLoop.instance().add_callback(
                partial(callback, future)))

    return wrapper


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world %s" % time.time())


class SleepHandler(tornado.web.RequestHandler):

    @unblock
    def get(self, n):
        time.sleep(float(n))
        return "Awake! %s" % time.time()


class SleepAsyncHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self, n):

        def callback(future):
            self.write(future.result())
            self.finish()

        EXECUTOR.submit(
            partial(self.get_, n)
        ).add_done_callback(
            lambda future: tornado.ioloop.IOLoop.instance().add_callback(
                partial(callback, future)))

    def get_(self, n):
        time.sleep(float(n))
        return "Awake! %s" % time.time()


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/sleep/(\d+)", SleepHandler),
    (r"/sleep_async/(\d+)", SleepAsyncHandler),
], debug=True)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()