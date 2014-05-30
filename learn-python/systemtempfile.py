#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-19 11:59
# Copyright 2014 LEO

"""
在开发应用程序的过程中，会有一些临时的信息，或者不太重要的信息，会保存在一个特殊的目录下面，在windows 里面，通常会在
c:\docume~1\admini~1\locals~1\temp 这个地方，而在 centos 中就是 /tmp 目录

在python里面有tempfile这个模块可以调用

这里将这些方法列出来，讲解一下
tempfile.mkstemp([suffix=''[, prefix='tmp'[, dir=None[, text=False]]]])
    mkstemp方法用于创建一个临时文件。该方法仅仅用于创建临时文件， 调用tempfile.mkstemp函数后，返回包含两个元素的元组，
    第一个元素指示操作该临时文件的安全级别，第二个元素指示该临时文件的路径。
    参数 suffix和prefix分别表示临时文件名称的后缀和前缀；dir指定了临时文件所在的目录，
    如果没有指定目录，将根据系统环境变量TMPDIR, TEMP或者TMP的设置来保存临时文件；
    参数text指定了是否以文本的形式来操作文件，默认为False，表示以二进制的形式来操作文件。

tempfile.mkdtemp([suffix=''[, prefix='tmp'[, dir=None]]])
    该函数用于创建一个临时文件夹。参数的意思与tempfile.mkdtemp一样。它返回临时文件夹的绝对路径。

tempfile.mktemp([suffix=''[, prefix='tmp'[, dir=None]]])
    mktemp用于返回一个临时文件的路径，但并不创建该临时文件。

tempfile.tempdir
    该属性用于指定创建的临时文件（夹）所在的默认文件夹。
    如果没有设置该属性或者将其设为None，Python将返回以下环境变量TMPDIR, TEMP, TEMP指定的目录，
    如果没有定义这些环境变量，临时文件将被创建在当前工作目录。

tempfile.gettempdir()
    gettempdir()则用于返回保存临时文件的文件夹路径。

tempfile.TemporaryFile([mode='w+b'[, bufsize=-1[, suffix=''[, prefix='tmp'[, dir=None]]]]])
    该函数返回一个 类文件 对象(file-like)用于临时数据保存（实际上对应磁盘上的一个临时文件）。
    当文件对象被close或者被del的时候，临时文件将从磁盘上删除。
    mode、bufsize参数的单方与open()函数一样；
    suffix和prefix指定了临时文件名的后缀和前缀；
    dir用于设置临时文件默认的保 存路径。
    返回的类文件对象有一个file属性，它指向真正操作的底层的file对象。

tempfile.NamedTemporaryFile([mode='w+b'[, bufsize=-1[, suffix=''[, prefix='tmp'[, dir=None[, delete=True]]]]]])
    tempfile.NamedTemporaryFile函数的行为与tempfile.TemporaryFile类似，只不过它多了一个delete 参数，
    用于指定类文件对象close或者被del之后，是否也一同删除磁盘上的临时文件（当delete = True的时候，行为与TemporaryFile一样）。

tempfile.SpooledTemporaryFile([max_size=0[, mode='w+b'[, bufsize=-1[, suffix=''[, prefix='tmp'[, dir=None]]]]]])
    tempfile.SpooledTemporaryFile函数的行为与tempfile.TemporaryFile类似。
    不同的是向类文件对象写数 据的时候，数据长度只有到达参数max_size指定大小时，或者调用类文件对象的fileno()方法，数据才会真正写入到磁盘的临时文件中
"""

import tempfile
import os

tmpfd, tempfilename = tempfile.mkstemp()
print tmpfd
print tempfilename
os.close(tmpfd)

#删除临时文件
os.unlink(tempfilename)