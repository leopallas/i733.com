#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo XU     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-06 00:35
# Copyright 2014 LEO

import socket
import sys
"""
family参数代表地址家族，可为AF_INET或AF_UNIX。AF_INET家族包括Internet地址，AF_UNIX家族用于同一台机器上的进程间通信。
type参数代表套接字类型，可为SOCK_STREAM(流套接字)和SOCK_DGRAM(数据报套接字)。
SOCK_DGRAM 用于 UDP 通讯协议，UDP 通讯是非连接
"""
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #创建一个socket实例
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()
print 'Socket Created'

host = 'www.oschina.net'
port = 80

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
print 'Ip address of ' + host + ' is ' + remote_ip
s.connect((remote_ip, port))
print 'Socket Connected to ' + host + ' on ip ' + remote_ip

#Send some data to remote server
message = "GET / HTTP/1.1\r\nHost: www.oschina.net\r\n\r\n" #发送字符串数据 "GET / HTTP/1.1\r\n\r\n" ，这是一个 HTTP 协议的命令，用来获取网站首页的内容
try:
    #Set the whole string
    s.sendall(message)
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()
print 'Message send successfully'

#Now receive data
reply = s.recv(4096)
print reply
s.close()