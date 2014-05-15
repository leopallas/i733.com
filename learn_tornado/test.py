#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-30 11:02
# Copyright 2014 LEO

import tornado.httpserver
import tornado.ioloop

def handle_request(request):
   message = "You requested %s\n" % request.uri
   request.write("HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n%s" % (
                 len(message), message))
   request.finish()

# http_server = tornado.httpserver.HTTPServer(handle_request)
# http_server.listen(8888)
# tornado.ioloop.IOLoop.instance().start()


# server = tornado.httpserver.HTTPServer(handle_request)    # 不能传递IOLoop
# server.bind(8888)
# server.start(0)  # 创建多进程
# tornado.ioloop.IOLoop.instance().start()

sockets = tornado.netutil.bind_sockets(8888)
tornado.process.fork_processes(0)   # 创建多进程
server = tornado.httpserver.HTTPServer(handle_request)    # 可以传递IOLoop
server.add_sockets(sockets)
tornado.ioloop.IOLoop.instance().start()

