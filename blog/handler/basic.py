#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-04-10 16:03
# Copyright 2014 LEO

import tornado.ioloop
from tornado.escape import url_unescape, json_decode
import tornado.web
import tornado.httpserver
from tornado.log import access_log
from tornado.web import MissingArgumentError

from sqlalchemy import func, distinct
from blog.model.models import StatTrace, User, Option
from blog import util

import os
import re
import urlparse
from datetime import datetime

spider_list = []
browser_list = []
os_list = []
se_list = []
lang_map = {}


def init_stat_def():
    browserpath = os.path.join(os.path.dirname(__file__), 'def\\browser.dat').replace('\\', '/')
    feedpath = os.path.join(os.path.dirname(__file__), 'def\\feed.dat').replace('\\', '/')
    languagespath = os.path.join(os.path.dirname(__file__), 'def\\languages.dat').replace('\\', '/')
    ospath = os.path.join(os.path.dirname(__file__), 'def\\os.dat').replace('\\', '/')
    sepath = os.path.join(os.path.dirname(__file__), 'def\\searchengine.dat').replace('\\', '/')
    spiderpath = os.path.join(os.path.dirname(__file__), 'def\\spider.dat').replace('\\', '/')
    f = open(browserpath, 'r')
    try:
        global browser_list
        browser_list = f.readlines()
    finally:
        f.close()

    f = open(spiderpath, 'r')
    try:
        global spider_list
        spider_list = f.readlines()[:]
    finally:
        f.close()

    f = open(ospath, 'r')
    try:
        global os_list
        os_list = f.readlines()[:]
    finally:
        f.close()

    f = open(sepath, 'r')
    try:
        global se_list
        se_list = f.readlines()[:]
    finally:
        f.close()

    f = open(languagespath, 'r')
    try:
        global lang_map
        for line in f.readlines():
            value = line.split('|')
            if len(value[0]) == 0 or len(value[1]) == 0:
                continue
            lang_map[value[1]] = value[0]
    finally:
        f.close()


init_stat_def()


def is_skip_uri(uri):
    """
    check if it needs to skip these urls:
        static file
        admin request
        ajax
    """
    if re.search(r'.ico$', uri):
        return True
    if re.search(r'favicon.ico', uri):
        return True
    if re.search(r'.css$', uri):
        return True
    if re.search(r'.js$', uri):
        return True

    if uri.find("/admin/") != -1:
        return True
    if uri.find("/comment/add") != -1:
        return True
    if uri.find("/comment/list") != -1:
        return True
    if uri.find("/tag/list") != -1:
        return True
    if uri.find("/category/list") != -1:
        return True
    return False


def get_url(uri):
    # home page with page id
    if uri[0:2] == '/?':
        return ''
    # home
    if uri == '/':
        return ''
    return uri


def get_spider(agent):
    agent = agent.replace(' ', '')
    for item in spider_list:
        value = item.split('|')
        if len(value[0]) == 0 or len(value[1]) == 0:
            continue
        if agent.find(value[1]) != -1:
            return value[0]
    return ""


def get_browser(agent):
    agent = agent.replace(' ', '')
    for item in browser_list:
        value = item.split('|')
        if len(value[0]) == 0 or len(value[1]) == 0:
            continue
        if agent.find(value[1]) != -1:
            return value[0]
    return ""


def get_os(agent):
    agent = agent.replace(' ', '')
    for item in os_list:
        value = item.split('|')
        if len(value[0]) == 0 or len(value[1]) == 0:
            continue
        if agent.find(value[1]) != -1:
            return value[0]
    return ""


def get_se(referrer):
    for item in se_list:
        value = item.split('|')
        if len(value[0]) == 0 or len(value[1]) == 0:
            continue
        if referrer.find(value[1]) == -1:
            continue
        result = urlparse.urlparse(referrer)
        parametermap = urlparse.parse_qs(result.query, True)
        for k in parametermap.keys():
            if k == value[2]:
                return value[0]
    return ""


def is_feed(uri):
    return False


def is_post(uri):
    if uri.find("/post/id/") != -1:
        return True
    return False


def get_nation(accept_language):
    try:
        if accept_language:
            return accept_language[0:2]
    except:
        pass
    return ""


def get_stat_info(db):
    '''
    since: the start time of visiting
    totalvisitors: the visitor count of site except spider and feed
    totalpageviews: the view count of site except spider and feed
    todayvisitors: today, the visitor count of site except spider and feed
    todaypageviews: today, the view count of site except spider and feed
    '''
    stat = {}

    #st = db.query(StatTrace).filter(StatTrace.ip != '').order_by(StatTrace.date.desc()).first()
    #stat['since'] = st.date
    stat['totalvisitors'] = db.query(func.count(distinct(StatTrace.ip))).filter_by(spider='', feed='').scalar()
    #stat['totalpageviews'] = db.query(func.count('*')).select_from(StatTrace).filter_by(spider='', feed='').scalar()
    # comment the today stat
    #stat['todayvisitors'] = db.query(func.count(distinct(StatTrace.ip))).filter_by(spider='', feed='', date=datetime.date.today()).scalar()
    #stat['todaypageviews'] = db.query(func.count(StatTrace.ip)).filter_by(spider='', feed='', date=datetime.date.today()).scalar()

    return stat


def get_post_stat_info(db, url):
    '''
    thistotalvisitors: the totalvisitors of the current post url
    thistodayvisitors: the todayvisitors of the current post url
    thistotalpageviews: the totalpageviews of the current post url
    thistodaypageviews: the todaypageviews of the current post url
    '''
    stat = {}
    # comment the today stat
    stat['thistotalvisitors'] = db.query(func.count(distinct(StatTrace.ip))).filter_by(spider='', feed='',
                                                                                       urlrequested=url).scalar()
    #stat['thistodayvisitors'] = db.query(func.count(distinct(StatTrace.ip))).filter_by(spider='', feed='', urlrequested=url, date=datetime.date.today()).scalar()

    #stat['thistotalpageviews'] = db.query(func.count('*')).select_from(StatTrace).filter_by(spider='', feed='', urlrequested=url).scalar()
    #stat['thistodaypageviews'] = db.query(func.count(StatTrace.ip)).filter_by(spider='', feed='', urlrequested=url, date=datetime.date.today()).scalar()
    return stat


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.set_header('Content-Type', 'application/json')
        self._auth_request = False
        self._usr_id = None
        self._json_args = None
        self._option_dict = None

    @property
    def db(self):
        return self.application.db

    @property
    def get_usr_id(self):
        return self._usr_id

    def initialize(self):
        pass

    def on_finish(self):
        self.db.close()

    def prepare(self):
        self.request_stat_trace()
        if self._auth_request:
            self._usr_id = self.validation_url_sign()

    def get_current_user(self):
        username = self.get_secure_cookie("blogadmin_user")
        if not username:
            return None
        return self.db.query(User).filter_by(login=username).first()

    @property
    def options(self):
        if self._option_dict is None:
            option_list = self.db.query(Option).all()
            self._option_dict = {option.name: option.value for option in option_list}
        return self._option_dict

    def update_options(self):
        option_list = self.db.query(Option).all()
        self._option_dict = {option.name: option.value for option in option_list}

    def request_stat_trace(self):
        request_uri = self.request.uri
        if is_skip_uri(request_uri):
            return None
        request_uri = get_url(request_uri)
        date = datetime.date.today()
        dt = datetime.datetime.now()
        time = datetime.time(dt.hour, dt.minute, dt.second)
        ip = self.request.remote_ip
        referrer = ''
        try:
            referrer = self.request.headers['Referer']
        except:
            pass
        agent = ''
        try:
            agent = self.request.headers['User-Agent']
        except:
            pass
        spider = get_spider(agent) if len(agent) != 0 else ''
        os = get_os(agent) if len(agent) != 0 else ''
        browser = get_browser(agent) if len(agent) != 0 else ''
        search_engine = get_se(referrer) if len(referrer) != 0 else ''
        nation = get_nation(self.request.headers['Accept-Language'])
        feed = request_uri if is_feed(request_uri) else ''
        real_post = 1 if is_post(request_uri) else 0

        st = StatTrace(date=date,
                       time=time,
                       ip=ip,
                       request_uri=request_uri,
                       agent=agent,
                       referrer=referrer,
                       os=os,
                       browser=browser,
                       search_engine=search_engine,
                       spider=spider,
                       feed=feed,
                       nation=nation,
                       real_post=real_post)
        self.db.add(st)
        self.db.commit()

    def load_json(self):
        """Load JSON from the request body and store them in
        self.request.arguments, like Tornado does by default for POSTed form
        parameters.

        If JSON cannot be decoded, raises an HTTPError with status 400.
        """
        json_headers = (
            "text/json",
            # "text/javascript",
            "application/json",  # default
            # "application/javascript",
        )
        if self.request.headers['Content-Type'] in json_headers:
            try:
                self._json_args = json_decode(self.request.body)
            except ValueError:
                msg = "Could not decode JSON: %s" % self.request.body
                access_log.error(msg)
                raise tornado.web.HTTPError(400, msg)
        else:
            access_log.error('Content-Type is not application/json.')
            raise tornado.web.HTTPError(400)

    def get_json_argument(self, name, default=None):
        """Find and return the argument with key 'name' from JSON request data.
        Similar to Tornado's get_argument() method.
        """
        if default is None:
            default = self._ARG_DEFAULT
        if not self._json_args:
            self.load_json()
        if name not in self._json_args:
            if default is self._ARG_DEFAULT:
                access_log.debug("Missing argument '%s'" % name)
                raise tornado.web.MissingArgumentError(name)
            access_log.debug("Returning default argument %s, as we couldn't find "
                             "'%s' in %s" % (default, name, self.request.arguments))
            return default
        arg = self._json_args[name]
        access_log.debug("Found '%s': %s in JSON arguments" % (name, arg))
        return arg

    def validation_url_sign(self):
        au = self.get_argument('au')
        tkn = self.get_argument('tkn')

        #根据SECRET_TOKEN从数据库中取得签名的Key
        authkey = self.db.get("SELECT SIGNATURE_KEY, USR_ID FROM auth_key where SECRET_TOKEN = %s", tkn)
        if not authkey:
            raise tornado.web.HTTPError(400)
        # 验证签名
        uri = '%s+%s+%s+%s' % (
            self.request.method, self.request.protocol, self.request.path, url_unescape(self.request.query))
        uri = uri.replace('&au=' + au, '')
        uri = uri.replace('&tkn=' + tkn, '')
        sign = util.signature(authkey['SIGNATURE_KEY'], uri)
        if sign != au:
            raise tornado.web.HTTPError(400)
        return authkey['USR_ID']

    def response_status(self, code=(500, 'Server Error!')):
        status_code = code[0]
        reason = code[1]

        self.set_status(status_code, reason=reason)
        # self.set_status(code[0], code[1])
        try:
            self.write_error(status_code)
        except Exception:
            access_log.error("Uncaught exception in write_error", exc_info=True)
        if not self._finished:
            self.finish()

    def response_status(self, code=(500, 'Server Error!')):
        print code
        self.set_status(code[0], code[1])


class AuthBaseHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(AuthBaseHandler, self).__init__(application, request, **kwargs)
        self._auth_request = True


class Navigate:
    def __init__(self, nid, name, parent, have_child):
        self.nid = nid
        self.name = name
        self.parent = parent
        # implicate if it have a child page
        self.have_child = have_child


def get_nav_list(pages):
    navlist = []
    for page in pages:
        have_child = False
        for sub in pages:
            if sub.parent == page.id:
                have_child = True
                break
        navlist.append(Navigate(page.id, page.title, page.parent, have_child))
    return navlist


def unittest():
    print is_skip_uri('/admin/page/edit/10')
    print is_skip_uri('/category/list')
    print is_skip_uri('/static/img/favour.ico')
    print is_skip_uri('/admin/page/edit/10')
    print not is_skip_uri('/post/id/6')
    print not is_skip_uri('/post/category/python/?p=1')

    print get_url('/post/id/2')

    print not is_post('/post/category/python/?p=1')
    print is_post('/post/id/10')
    agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36"
    print 'spider:', get_spider(agent)
    print 'browser:', get_browser(agent)
    print 'os:', get_os(agent)
    print 'se:', get_se(agent)

    from sqlalchemy.orm import scoped_session, sessionmaker
    from blog.model.models import engine

    db = scoped_session(sessionmaker(bind=engine))
    print get_stat_info(db)


if __name__ == '__main__':
    unittest()
    # pass