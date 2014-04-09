#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import ConfigParser
from common import mysql
from datetime import datetime

cf = ConfigParser.ConfigParser()
cf.read('config.ini')

db_conn = mysql.Mysql(host=cf.get("Database", "host"), port=cf.getint("Database", "port"),
                      user=cf.get("Database", "user"), pwd=cf.get("Database", "pwd"),
                      db=cf.get("Database", "db"), charset=cf.get("Database", "charset"))

from mako.template import Template

# mytemplate = Template("hello world!")
# print mytemplate.render()

# mytemplate = Template("hello, ${name}!")
# print mytemplate.render(name="jack")
#
#
from mako.runtime import Context
from StringIO import StringIO
# mytemplate = Template("hello, ${name}!")
# buf = StringIO()
# ctx = Context(buf, name="jack")
# mytemplate.render_context(ctx)
# print buf.getvalue()
#
#
#
mytemplate = Template(filename='templates/test.html', module_directory='tmp')
print mytemplate.render()
#
#
from mako.lookup import TemplateLookup
#
# mylookup = TemplateLookup(directories=['/docs'])
# mytemplate = Template("""<%include file="header.txt"/> hello world!""", lookup=mylookup)
#
#
coupons = db_conn.getAll("select * from facility")
print coupons

mylookup = TemplateLookup(directories=['templates'],
                          input_encoding='utf-8',
                          output_encoding='utf-8',
                          default_filters=['decode.utf8'],
                          module_directory='/tmp/mako_modules')

print "look up"
mytemplate = mylookup.get_template("base.html")

print mytemplate.render_unicode(coupons=coupons)


#
#
# from mako import exceptions
# try:
#     template = mylookup.get_template('sdfasdfas')
#     print template.render()
# except:
#     print exceptions.text_error_template().render()
#     print exceptions.html_error_template().render()
#
#
# import tempfile
# import os
# import shutil
#
#
# def module_writer(source, outputpath):
#     (dest, name) = \
#         tempfile.mkstemp(
#             dir=os.path.dirname(outputpath)
#         )
#
#     os.write(dest, source)
#     os.close(dest)
#     shutil.move(name, outputpath)
#
# #
# # mytemplate = Template(
# #                 filename="base.html",
# #                 module_directory="/path/to/modules",
# #                 module_writer=module_writer
# #             )
#
#
# def serve_template(templatename, **kwargs):
#     mytemplate = mylookup.get_template(templatename)
#     print mytemplate.render(**kwargs)


