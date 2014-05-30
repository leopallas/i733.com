#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-28 13:43
# Copyright 2014 LEO

"""
限制上传图片的格式，所以要做文件类型检测
"""
def get_image_type(pd, is_path=True):
    '''
    获取图片的类型，支持传入路径和文件内容
    '''
    if is_path:
        f = file(pd, 'rb')
        data = f.read(10).encode('hex')
    else:
        data = pd.encode('hex')

    ftype = None

    if data.startswith('ffd8'):
        ftype = 'jpeg'
    if data.startswith('424d'):
        ftype = 'bmp'
    if data.startswith('474946'):
        ftype = 'gif'
    elif data.startswith('89504e470d0a1a0a'):
        ftype = 'png'

    return ftype