#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-19 11
"""
python 可以很方便的对文件进行打开，读写操作，删除操作，也可以很方便的对文件夹进行遍历操作。总体说来，有如下几个方面：
1. python 遍历文件目录，当然可以递归
2. python 删除文件
3. python 对文件进行重命名操作
4. python 创建文件夹 （多个层级创建）
5. python 删除文件夹  （多个层级删除）
6. python 移动文件
7. python 查找文件
8. 得到文件夹的大小

我在用python 做一个网盘服务端的时候用到的一些方法，记录下来，以供以后参考
"""

import json
import os
import time
import glob
import shutil

DATETIMEFORMATER = '%Y-%m-%d %X'

#only for windows
RECYCLED_FOLDER_NAME = 'Recycled'


def dateformat(datetime):
    '''return GMT TIME,need to change to LOCAL TIME'''
    return time.strftime(DATETIMEFORMATER, time.gmtime(datetime))


def filesizeformat(size):
    ''' Convert file size to string '''
    KBSIZE = 1024.00
    strSize = '0 Byte'
    if (size < KBSIZE):
        strSize = '%.2f Byte' % (size)
    elif (size >= KBSIZE and size < KBSIZE ** 2):
        strSize = '%.2f K' % (size / KBSIZE)
    elif (size >= KBSIZE ** 2 and size < KBSIZE ** 3):
        strSize = '%.2f M' % (size / KBSIZE / KBSIZE)
    elif (size >= KBSIZE ** 3):
        strSize = '%.2f G' % (size / KBSIZE / KBSIZE / KBSIZE)

    return strSize


def listdir(path):
    if os.path.isfile(path):
        return '[]'
    allFiles = os.listdir(path)
    retlist = []
    for cfile in allFiles:
        fileinfo = {}
        filepath = (path + os.path.sep + cfile).replace("\\", "/")

        if cfile == RECYCLED_FOLDER_NAME:
            continue

        if os.path.isdir(filepath):
            fileinfo['isfile'] = '0'
            fileinfo['size'] = getfoldersize(filepath)
        else:
            fileinfo['isfile'] = '1'
            fileinfo['size'] = os.path.getsize(filepath)

        fileinfo['name'] = cfile
        fileinfo['lastvisittime'] = dateformat(os.path.getatime(filepath))
        fileinfo['createtime'] = dateformat(os.path.getctime(filepath))
        fileinfo['lastmodifytime'] = dateformat(os.path.getmtime(filepath))

        retlist.append(fileinfo)
    retStr = json.dumps(retlist, encoding='utf-8')
    return retStr


def deletefile(path):
    if os.path.exists(path):
        os.remove(path)


def rename(old, new):
    if os.path.exists(old):
        os.rename(old, new)


def checkoutfile(path):
    pass


def checkinfile(path):
    pass


def lockfile(path):
    pass


def unlockfile(path):
    pass


def createfolder(path):
    if not os.path.exists(path):
        os.mkdir(path)


def createfolders(path):
    if not os.path.exists(path):
        os.makedirs(path);


def deletefolder(path):
    if os.path.isdir(path):
        os.rmdir(path)


def retreeExceptionHandler(fun, path, excinfo):
    pass


def deletefolders(path):
    #    if  os.path.isdir(path):
    #        os.removedirs(path)
    shutil.rmtree(path, ignore_errors=False, onerror=retreeExceptionHandler)


def movefile(old, new):
    shutil.move(old, new)


def getfoldersize(path):
    size = 0
    for root, dirs, files in os.walk(path):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size


def searchfile(path, ext):
    returnList = glob.glob1(path, ext)
    return returnList


if __name__ == '__main__':
    listdir('c:/vDriver')
    #searchfile('c:/vDriver','*.log')