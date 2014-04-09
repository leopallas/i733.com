#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'xw'
import os
import sys
import ConfigParser
import time
import sched
from common import mysql
from common.unit import HtmlGenerator

s = sched.scheduler(time.time, time.sleep)


def perform(inc, gen, sqls, out_put_path):
    s.enter(inc, 0, perform, (inc, gen, sqls, out_put_path))
    generateIndexPage(gen, sqls, out_put_path)


def generateIndexPage(gen, sqls, out_put_path):
    couponHTML = gen.couponHTML(sqls[0])
    houseHTML = gen.houseHTML(sqls[1])
    shopHTML = gen.shopHTML(sqls[2])
    secondhandHTML = gen.secondhandHTML(sqls[3])

    page_context = {'couponHTML': couponHTML, 'houseHTML': houseHTML, 'shopHTML': shopHTML, 'secondhandHTML': secondhandHTML,}

    root_dir = os.path.abspath(os.path.dirname(__file__))
    index_html_file = os.path.join(root_dir, 'template/index.html')
    fileHandle = open(index_html_file)
    template = fileHandle.read()
    fileHandle = open(out_put_path, 'w')
    fileHandle.write(template % page_context)
    fileHandle.close()


def init():
    #获取当前脚本执行的目录
    root_dir = os.path.abspath(os.path.dirname(__file__))
    #sys.path.append(root_dir)

    #配置文件路径
    config_file = os.path.join(root_dir, 'config.ini')
    if not os.path.isfile(config_file):
        #文件不存在
        print "\033[31;1m[Error]===> 文件不存在\033[0m"
        sys.exit(0)

    #读取配置文件
    cf = ConfigParser.ConfigParser()
    cf.read(config_file)
    #read server
    domain_img = cf.get("Domain", "domain_img")

    sql_search_coupon = cf.get("SQL", "couponSql")
    sql_search_house = cf.get("SQL", "houseSql")
    sql_search_shop = cf.get("SQL", "shopSql")
    sql_search_secondhand = cf.get("SQL", "secondhandSql")
    sqls = (sql_search_coupon, sql_search_house, sql_search_shop, sql_search_secondhand)

    db_conn = mysql.Mysql(host=cf.get("Database", "host"), port=cf.getint("Database", "port"),
                          user=cf.get("Database", "user"), pwd=cf.get("Database", "pwd"),
                          db=cf.get("Database", "db"), charset=cf.get("Database", "charset"))

    no_img_uri = cf.get("URI", "defaultNoImgUri")
    gen = HtmlGenerator(root_dir, domain_img, db_conn, no_img_uri)
    out_put_path = cf.get("FILE", "outPutPath")
    return gen, sqls, out_put_path


def main(inc=5 * 60, round=False):
    """
    :param inc:  间隔时间，默认5分钟
    :param round: 是否循环执行, 默认不循环执行
    """
    parm = init()
    if not round:
        generateIndexPage(parm[0], parm[1], parm[2])
    else:
        s.enter(0, 0, perform, (inc, parm[0], parm[1], parm[2]))
        s.run()

if __name__ == '__main__':
    main()

    # round = raw_input('是否开始执行自动生成首页程序 (yes or no) : ')
    # if round is None or round.strip() == '' or round.upper() == 'NO':
    #     main()
    # elif round.upper() == 'YES':
    #     try:
    #         interval_time = int(raw_input('输入生成的时间间隔(秒) : '))
    #         print interval_time
    #     except ValueError:
    #         print "请输入有效的时间间隔"
    #
    #     main(inc=interval_time, round=True)
    # else:
    #     print "输入参数错误"