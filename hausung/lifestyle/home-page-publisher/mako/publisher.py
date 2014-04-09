__author__ = 'xw'

import os
import sys
import ConfigParser
from common import mysql
from datetime import datetime
from mako.template import Template
from mako.lookup import TemplateLookup



#获取当前脚本执行的目录
root_dir = os.path.abspath(os.path.dirname(__file__))

#配置文件路径
config_file = os.path.join(root_dir, '../config.ini')
if not os.path.isfile(config_file):
    #文件不存在
    print "\033[31;1m[Error]===> 文件不存在\033[0m"
    sys.exit(0)

#读取配置文件
cf = ConfigParser.ConfigParser()
cf.read('config.ini')
#read server
domain_img = cf.get("Domain", "domain_img")
domain_i = cf.get("Domain", "domain_i")
domain_fang = cf.get("Domain", "domain_fang")
domain_www = cf.get("Domain", "domain_www")

sql_search_coupon = cf.get("SQL", "couponSql")
sql_search_house = cf.get("SQL", "houseSql")
sql_search_shop = cf.get("SQL", "shopSql")
sql_search_secondhand = cf.get("SQL", "secondhandSql")

db_conn = mysql.Mysql(host=cf.get("Database", "host"), port=cf.getint("Database", "port"),
                      user=cf.get("Database", "user"), pwd=cf.get("Database", "pwd"),
                      db=cf.get("Database", "db"), charset=cf.get("Database", "charset"))

no_img_uri = cf.get("URI", "defaultNoImgUri")

coupons = db_conn.getAll(sql_search_coupon)
houses =  db_conn.getAll(sql_search_house)

mylookup = TemplateLookup(directories=['template'],
                          input_encoding='utf-8',
                          output_encoding='utf-8',
                          default_filters=['decode.utf8'],
                          module_directory='/tmp/mako_modules')

mytemplate = mylookup.get_template("base.html")
print mytemplate.render_unicode(coupons=coupons, houses=houses)