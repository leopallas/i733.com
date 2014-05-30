#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-19 14:58
# Copyright 2014 LEO
"""
在python中如何实现呢，其实python 本身也带了日志操作的库。可以直接使用。这里我把在项目中用到的整理了一下，分享在下面,这个实现的方法，主要有两点
1. 写日志的类
2.日志配置文件(handler,logger,以及日志保存的路径等)
"""

import logging.config
import os


class INetLogger:
    log_instance = None

    @staticmethod
    def InitLogConf():
        currentDir = os.path.dirname(__file__)
        INetLogger.log_instance = logging.config.fileConfig(currentDir + os.path.sep + "logger.ini")

    @staticmethod
    def GetLogger(name=""):
        if INetLogger.log_instance == None:
            INetLogger.InitLogConf()
        INetLogger.log_instance = logging.getLogger(name)
        return INetLogger.log_instance


if __name__ == "__main__":
    logger = INetLogger.GetLogger()
    logger.debug("debug message")
    logger.info("info message")
    logger.warn("warn message")
    logger.error("error message")
    logger.critical("critical message")
    logHello = INetLogger.GetLogger("root")
    logHello.info("Hello world!")