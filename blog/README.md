#参照wordpress写的python版的个人博客, 也是用来学习python的个人作品.

开发环境:
-Ubuntu 12.04
-Python 2.7.5
-MySql 5.5.37

========
Python modules:
-tornado 3.2 (http://www.tornadoweb.org)

-SQLAlchemy 0.9.4 (http://www.sqlalchemy.org/)

-WTForms 2.0 (http://wtforms.simplecodes.com/)

-PIL 1.1.7 (http://www.pythonware.com/products/pil/)

UI:

-CKEditor 4.4.1 (http://ckeditor.com/)

-bootstrap 2.3.2 or 3.0.3(http://twitter.github.io/bootstrap/index.html)

-SyntaxHighlighter 3.0.83 (http://alexgorbatchev.com/SyntaxHighlighter/download/)

-Jquery 1.11.1 (http://jquery.com/)

-JqueryUI 1.10.3 (http://jqueryui.com/)

-jquery validation 1.12.0

-jquery tablesorter 2.17.1

-jquery splitter 1.6

-jquery form plugin 3.50


期间遇到的问题:

(1)UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

解决：3种方法
  a、把ascii改为utf-8，还有就是最好文件目录中不要出现中文；
  b、在python的安装目录下的Lib目录，找到site.py,修改def setencoding()方法
def setencoding():
   encoding = "ascii" # Default value set by _PyUnicode_Init()
   ....
    if 0:
        # Enable to support locale aware default string encodings.
把if 0改为if 1.

  c、在代码第一行指定编码
    #-*-coding:utf-8-*-
    或
    #coding=utf8
