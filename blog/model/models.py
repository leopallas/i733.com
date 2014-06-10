#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-16 12:14
# Copyright 2014 LEO
from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation
from sqlalchemy.dialects.mysql import \
    BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
    DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
    LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
    NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
    TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

import logging
from blog.setting import DB_CONNECT_STRING, DB_ENCODING, DB_ECHO

engine = create_engine(DB_CONNECT_STRING, encoding=DB_ENCODING, echo=DB_ECHO)
Base = declarative_base()  # declarative base class for SQLAlchemy


class Comment(Base):
    __tablename__ = 'comment'

    __table_args__ = {}

    #column definitions
    id = Column('id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False)
    post_id = Column('post_id', BIGINT(display_width=20, unsigned=True), nullable=False)
    author = Column('author', TINYTEXT(), nullable=False)
    author_email = Column('author_email', VARCHAR(length=100), nullable=False)
    author_url = Column('author_url', VARCHAR(length=200), nullable=False)
    author_ip = Column('author_ip', VARCHAR(length=100), nullable=False)
    date = Column('date', DATETIME(), nullable=False)
    date_gmt = Column('date_gmt', DATETIME(), nullable=False)
    content = Column('content', TEXT(), nullable=False)
    karma = Column('karma', INTEGER(display_width=11), nullable=False)
    approved = Column('approved', VARCHAR(length=20), nullable=False)
    agent = Column('agent', VARCHAR(length=255), nullable=False)
    type = Column('type', VARCHAR(length=20), nullable=False)
    parent = Column('parent', BIGINT(display_width=20, unsigned=True), nullable=False)
    user_id = Column('user_id', BIGINT(display_width=20, unsigned=True), nullable=False)

    #relation definitions


class Commentmeta(Base):
    __tablename__ = 'commentmeta'

    __table_args__ = {}

    #column definitions
    meta_id = Column('meta_id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False)
    comment_id = Column('comment_id', BIGINT(display_width=20, unsigned=True), nullable=False)
    meta_key = Column('meta_key', VARCHAR(length=255))
    meta_value = Column('meta_value', LONGTEXT())

    #relation definitions


class Link(Base):
    __tablename__ = 'link'

    __table_args__ = {}

    #column definitions
    id = Column('id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False)
    url = Column('url', VARCHAR(length=255), nullable=False)
    name = Column('name', VARCHAR(length=255), nullable=False)
    image = Column('image', VARCHAR(length=255), nullable=False)
    target = Column('target', VARCHAR(length=25), nullable=False)
    description = Column('description', VARCHAR(length=255), nullable=False)
    visible = Column('visible', VARCHAR(length=20), nullable=False)
    owner = Column('owner', BIGINT(display_width=20, unsigned=True), nullable=False)
    rating = Column('rating', INTEGER(display_width=11), nullable=False)
    updated = Column('updated', DATETIME(), nullable=False)
    rel = Column('rel', VARCHAR(length=255), nullable=False)
    notes = Column('notes', MEDIUMTEXT(), nullable=False)
    rss = Column('rss', VARCHAR(length=255), nullable=False)

    #relation definitions


class Option(Base):
    __tablename__ = 'option'

    __table_args__ = {}

    #column definitions
    id = Column('id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False)
    name = Column('name', VARCHAR(length=64), nullable=False)
    value = Column('value', LONGTEXT(), nullable=False)
    autoload = Column('autoload', VARCHAR(length=20), nullable=False, default=u'yes')

    #relation definitions


class Post(Base):
    __tablename__ = 'post'

    __table_args__ = {}

    #column definitions
    id = Column('id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False)
    author = Column('author', BIGINT(display_width=20, unsigned=True), nullable=False, default=0)
    date = Column('date', DATETIME(), nullable=False, default=u"'0000-00-00 00:00:00'")
    date_gmt = Column('date_gmt', DATETIME(), nullable=False, default=u"'0000-00-00 00:00:00'")
    content = Column('content', LONGTEXT(), nullable=False)
    title = Column('title', TEXT(), nullable=False)
    excerpt = Column('excerpt', TEXT(), nullable=False)
    status = Column('status', VARCHAR(length=20), nullable=False, default=u'publish')
    comment_status = Column('comment_status', VARCHAR(length=20), nullable=False, default=u'open')
    ping_status = Column('ping_status', VARCHAR(length=20), nullable=False, default=u'open')
    password = Column('password', VARCHAR(length=20), nullable=False, default=u'')
    name = Column('name', VARCHAR(length=200), nullable=False, default=u'')
    to_ping = Column('to_ping', TEXT(), nullable=False)
    pinged = Column('pinged', TEXT(), nullable=False)
    modified = Column('modified', DATETIME(), nullable=False)
    modified_gmt = Column('modified_gmt', DATETIME(), nullable=False)
    content_filtered = Column('content_filtered', LONGTEXT(), nullable=False)
    parent = Column('parent', BIGINT(display_width=20, unsigned=True), nullable=False, default=0)
    guid = Column('guid', VARCHAR(length=255), nullable=False, default=u'')
    menu_order = Column('menu_order', INTEGER(display_width=11), nullable=False, default=0)
    type = Column('type', VARCHAR(length=20), nullable=False, default=u'post')
    mime_type = Column('mime_type', VARCHAR(length=100), nullable=False, default=u'')
    comment_count = Column('comment_count', BIGINT(display_width=20), nullable=False, default=0)

    #relation definitions


class Postmeta(Base):
    __tablename__ = 'postmeta'

    __table_args__ = {}

    #column definitions
    meta_id = Column('meta_id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False)
    post_id = Column('post_id', BIGINT(display_width=20, unsigned=True), nullable=False)
    meta_key = Column('meta_key', VARCHAR(length=255))
    meta_value = Column('meta_value', LONGTEXT())

    #relation definitions


class Term(Base):
    __tablename__ = 'term'

    __table_args__ = {}

    #column definitions
    id = Column('id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False)
    name = Column('name', VARCHAR(length=200), nullable=False)
    slug = Column('slug', VARCHAR(length=200), nullable=False)
    term_group = Column('term_group', BIGINT(display_width=10), nullable=False, default=0)

    #relation definitions


class TermRelationship(Base):
    __tablename__ = 'term_relationship'

    __table_args__ = {}

    #column definitions
    object_id = Column('object_id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False)
    term_taxonomy_id = Column('term_taxonomy_id', BIGINT(display_width=20, unsigned=True), primary_key=True,
                              nullable=False)
    term_order = Column('term_order', INTEGER(display_width=11), nullable=False)

    #relation definitions


class TermTaxonomy(Base):
    __tablename__ = 'term_taxonomy'

    __table_args__ = {}

    #column definitions
    id = Column('id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False)
    term_id = Column('term_id', BIGINT(display_width=20, unsigned=True), nullable=False)
    taxonomy = Column('taxonomy', VARCHAR(length=32), nullable=False)
    description = Column('description', LONGTEXT(), nullable=False)
    parent = Column('parent', BIGINT(display_width=20, unsigned=True), nullable=False)
    count = Column('count', BIGINT(display_width=20), nullable=False)

    #relation definitions


class User(Base):
    __tablename__ = 'user'

    __table_args__ = {}

    #column definitions
    id = Column('id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False)
    login = Column('login', VARCHAR(length=60), nullable=False, default=u'')
    _password = Column('password', VARCHAR(length=64), nullable=False, default=u'')
    nicename = Column('nicename', VARCHAR(length=50), nullable=False, default=u'')
    email = Column('email', VARCHAR(length=100), nullable=False, default=u'')
    url = Column('url', VARCHAR(length=100), nullable=False, default=u'')
    registered = Column('registered', DATETIME(), nullable=False, default=u'0000-00-00 00:00:00')
    activation_key = Column('activation_key', VARCHAR(length=60), nullable=False, default=u'')
    status = Column('status', INTEGER(display_width=11), nullable=False, default=u'0')
    display_name = Column('display_name', VARCHAR(length=250), nullable=False, default=u'')

    #relation definitions

    @property
    def password(self):
        return self._password

    @property
    def pas(self):
        return self.url

    @password.setter
    def password(self, password):
        import hashlib
        # encrypt the password with md5
        self._password = unicode(hashlib.md5(password).hexdigest(), 'utf-8')


class Usermeta(Base):
    __tablename__ = 'usermeta'

    __table_args__ = {}

    #column definitions
    umeta_id = Column('umeta_id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False)
    user_id = Column('user_id', BIGINT(display_width=20, unsigned=True), nullable=False)
    meta_key = Column('meta_key', VARCHAR(length=255))
    meta_value = Column('meta_value', LONGTEXT())

    #relation definitions


from sqlalchemy import func


class StatTrace(Base):
    __tablename__ = 'stat_trace'

    id = Column('id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False)
    date = Column('date', DATE(), default=func.now(), nullable=False)
    time = Column('time', TIME(), default=func.now(), nullable=False)
    ip = Column(VARCHAR(length=39), default='')
    request_uri = Column('request_uri', TEXT(), default='')
    agent = Column('agent', TEXT(), default='')
    referrer = Column('referrer', TEXT(), default='')
    os = Column('os', VARCHAR(length=128), default='')
    browser = Column('browser', VARCHAR(length=128), default='')
    search_engine = Column('search_engine', VARCHAR(length=128), default='')
    spider = Column('spider', VARCHAR(length=128), default='')
    feed = Column('feed', VARCHAR(length=128), default='')
    nation = Column('nation', VARCHAR(length=16), default='')
    real_post = Column('real_post', INTEGER(display_width=11), default=1)


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


def init_tables():
    # delete all tables
    #drop_db()
    #create all tables
    #init_db()
    from sqlalchemy.orm import scoped_session, sessionmaker
    from sqlalchemy.engine import reflection

    db = scoped_session(sessionmaker(bind=engine))
    tables = reflection.Inspector.from_engine(engine).get_table_names()

    default_category = 1

    # determine if it needs to re-create the table.
    import datetime

    if 'user' not in tables:
        User.__table__.create(engine)
        user = User(login='leo',
                    password='123456',
                    nicename=u'鸟人',
                    email='leopallas@gmail.com',
                    url='www.i733.com',
                    registered=datetime.datetime.now(),
                    activation_key='123456',
                    status=1,
                    display_name='leo'
        )
        db.add(user)
        db.commit()

    if 'usermeta' not in tables:
        Usermeta.__table__.create(engine)

    if 'post' not in tables:
        Post.__table__.create(engine)
        post = Post(author=1,
                    date=datetime.datetime.now(),
                    date_gmt=datetime.datetime.now(),
                    title=u'我的第一篇文章哦',
                    content=u'欢迎使用python,tornado开发的博客系统',
                    excerpt=u'欢迎使用python,tornado开发的博客系统',
                    modified=datetime.datetime.now(),
                    modified_gmt=datetime.datetime.now(),
                    to_ping=u'',
                    pinged=u'',
                    content_filtered=u''
                    )
        db.add(post)
        db.commit()

    if 'postmeta' not in tables:
        Postmeta.__table__.create(engine)

    if 'comment' not in tables:
        Comment.__table__.create(engine)

    if 'commentmeta' not in tables:
        Commentmeta.__table__.create(engine)

    if 'link' not in tables:
        Link.__table__.create(engine)

    if 'term' not in tables:
        Term.__table__.create(engine)
        term = Term(name=u'未分类',
                    slug='uncategoried',
                    )
        db.add(term)
        db.commit()
        default_category = term.id

    if 'term_relationship' not in tables:
        TermRelationship.__table__.create(engine)

    if 'term_taxonomy' not in tables:
        TermTaxonomy.__table__.create(engine)

    if 'option' not in tables:
        Option.__table__.create(engine)
    db.add_all([Option(name='blogname', value='Leo Blog'),
                Option(name='blogdescription', value=u'欢迎使用鸟人的博客系统'),
                Option(name='users_can_register', value='0'),
                Option(name='admin_email', value='test@example.com'),
                Option(name='comments_notify', value='0'),
                Option(name='posts_per_rss', value='10'),
                Option(name='rss_use_excerpt', value='0'),
                # 缺省的文章是未分类
                Option(name='default_category', value=default_category),
                # 是否允许评论
                Option(name='users_can_comment', value='1'),
                # 每页最多显示多少条文章
                Option(name='posts_per_page', value='10'),
                Option(name='posts_per_recent_post', value='10'),
                Option(name='posts_per_recent_comment', value='10'),
                Option(name='mailserver_url', value='mail.example.com'),
                Option(name='mailserver_login', value='login@example.com'),
                Option(name='mailserver_pass', value='password'),
                Option(name='mailserver_port', value='110')])
    db.commit()

    if 'stat_trace' not in tables:
        StatTrace.__table__.create(engine)


if __name__ == '__main__':
    init_tables()
    pass