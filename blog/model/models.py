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
    autoload = Column('autoload', VARCHAR(length=20), nullable=False)

    #relation definitions


class Post(Base):
    __tablename__ = 'post'

    __table_args__ = {}

    #column definitions
    id = Column('id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False)
    author = Column('author', BIGINT(display_width=20, unsigned=True), nullable=False)
    date = Column('date', DATETIME(), nullable=False)
    date_gmt = Column('date_gmt', DATETIME(), nullable=False)
    content = Column('content', LONGTEXT(), nullable=False)
    title = Column('title', TEXT(), nullable=False)
    excerpt = Column('excerpt', TEXT(), nullable=False)
    status = Column('status', VARCHAR(length=20), nullable=False)
    comment_status = Column('comment_status', VARCHAR(length=20), nullable=False)
    ping_status = Column('ping_status', VARCHAR(length=20), nullable=False)
    password = Column('password', VARCHAR(length=20), nullable=False)
    name = Column('name', VARCHAR(length=200), nullable=False)
    to_ping = Column('to_ping', TEXT(), nullable=False)
    pinged = Column('pinged', TEXT(), nullable=False)
    modified = Column('modified', DATETIME(), nullable=False)
    modified_gmt = Column('modified_gmt', DATETIME(), nullable=False)
    content_filtered = Column('content_filtered', LONGTEXT(), nullable=False)
    parent = Column('parent', BIGINT(display_width=20, unsigned=True), nullable=False)
    guid = Column('guid', VARCHAR(length=255), nullable=False)
    menu_order = Column('menu_order', INTEGER(display_width=11), nullable=False)
    type = Column('type', VARCHAR(length=20), nullable=False)
    mime_type = Column('mime_type', VARCHAR(length=100), nullable=False)
    comment_count = Column('comment_count', BIGINT(display_width=20), nullable=False)

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
    term_group = Column('term_group', BIGINT(display_width=10), nullable=False)

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
    login = Column('login', VARCHAR(length=60), nullable=False)
    _password = Column('password', VARCHAR(length=64), nullable=False)
    nicename = Column('nicename', VARCHAR(length=50), nullable=False)
    email = Column('email', VARCHAR(length=100), nullable=False)
    url = Column('url', VARCHAR(length=100), nullable=False)
    registered = Column('registered', DATETIME(), nullable=False)
    activation_key = Column('activation_key', VARCHAR(length=60), nullable=False)
    status = Column('status', INTEGER(display_width=11), nullable=False)
    display_name = Column('display_name', VARCHAR(length=250), nullable=False)

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


if __name__ == '__main__':
    # drop_db()
    # init_db()
    pass