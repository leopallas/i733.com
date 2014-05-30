#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-30 15:01
# Copyright 2014 LEO
from sqlalchemy import create_engine, Column, MetaData, Table, text, Index
# from sqlalchemy.types import *
from sqlalchemy.dialects.mysql import \
    BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
    DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
    LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
    NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
    TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

from blog.setting import DB_CONNECT_STRING, DB_ENCODING, DB_ECHO

engine = create_engine(DB_CONNECT_STRING, encoding=DB_ENCODING, echo=DB_ECHO)


metadata = MetaData()
comment = Table('comment', metadata,
                Column('id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False),
                Column('post_id', BIGINT(display_width=20, unsigned=True), primary_key=False, nullable=False,
                       default=text(u"'0'")),
                Column('author', TINYTEXT(), primary_key=False, nullable=False),
                Column('author_email', VARCHAR(length=100), primary_key=False, nullable=False, default=text(u"''")),
                Column('author_url', VARCHAR(length=200), primary_key=False, nullable=False, default=text(u"''")),
                Column('author_ip', VARCHAR(length=100), primary_key=False, nullable=False, default=text(u"''")),
                Column('date', DATETIME(), primary_key=False, nullable=False, default=text(u"'0000-00-00 00:00:00'")),
                Column('date_gmt', DATETIME(), primary_key=False, nullable=False,
                       default=text(u"'0000-00-00 00:00:00'")),
                Column('content', TEXT(), primary_key=False, nullable=False),
                Column('karma', INTEGER(display_width=11), primary_key=False, nullable=False, default=text(u"'0'")),
                Column('approved', VARCHAR(length=20), primary_key=False, nullable=False, default=text(u"'1'")),
                Column('agent', VARCHAR(length=255), primary_key=False, nullable=False, default=text(u"''")),
                Column('type', VARCHAR(length=20), primary_key=False, nullable=False, default=text(u"''")),
                Column('parent', BIGINT(display_width=20, unsigned=True), primary_key=False, nullable=False,
                       default=text(u"'0'")),
                Column('user_id', BIGINT(display_width=20, unsigned=True), primary_key=False, nullable=False,
                       default=text(u"'0'")),


)
Index('date_gmt', comment.c.date_gmt, unique=False)
Index('parent', comment.c.parent, unique=False)
Index('post_id', comment.c.post_id, unique=False)
Index('approved_date_gmt', comment.c.approved, comment.c.date_gmt, unique=False)

commentmeta = Table('commentmeta', metadata,
                    Column('meta_id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False),
                    Column('comment_id', BIGINT(display_width=20, unsigned=True), primary_key=False, nullable=False,
                           default=text(u"'0'")),
                    Column('meta_key', VARCHAR(length=255), primary_key=False),
                    Column('meta_value', LONGTEXT(), primary_key=False),


)
Index('comment_id', commentmeta.c.comment_id, unique=False)
Index('meta_key', commentmeta.c.meta_key, unique=False)

link = Table('link', metadata,
             Column('id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False),
             Column('url', VARCHAR(length=255), primary_key=False, nullable=False, default=text(u"''")),
             Column('name', VARCHAR(length=255), primary_key=False, nullable=False, default=text(u"''")),
             Column('image', VARCHAR(length=255), primary_key=False, nullable=False, default=text(u"''")),
             Column('target', VARCHAR(length=25), primary_key=False, nullable=False, default=text(u"''")),
             Column('description', VARCHAR(length=255), primary_key=False, nullable=False, default=text(u"''")),
             Column('visible', VARCHAR(length=20), primary_key=False, nullable=False, default=text(u"'Y'")),
             Column('owner', BIGINT(display_width=20, unsigned=True), primary_key=False, nullable=False,
                    default=text(u"'1'")),
             Column('rating', INTEGER(display_width=11), primary_key=False, nullable=False, default=text(u"'0'")),
             Column('updated', DATETIME(), primary_key=False, nullable=False, default=text(u"'0000-00-00 00:00:00'")),
             Column('rel', VARCHAR(length=255), primary_key=False, nullable=False, default=text(u"''")),
             Column('notes', MEDIUMTEXT(), primary_key=False, nullable=False),
             Column('rss', VARCHAR(length=255), primary_key=False, nullable=False, default=text(u"''")),


)
Index('visible', link.c.visible, unique=False)

option = Table('option', metadata,
               Column('id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False),
               Column('name', VARCHAR(length=64), primary_key=False, nullable=False, default=text(u"''")),
               Column('value', LONGTEXT(), primary_key=False, nullable=False),
               Column('autoload', VARCHAR(length=20), primary_key=False, nullable=False, default=text(u"'yes'")),


)
Index('name', option.c.name, unique=True)

post = Table('post', metadata,
             Column('id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False),
             Column('author', BIGINT(display_width=20, unsigned=True), primary_key=False, nullable=False,
                    default=text(u"'0'")),
             Column('date', DATETIME(), primary_key=False, nullable=False, default=text(u"'0000-00-00 00:00:00'")),
             Column('date_gmt', DATETIME(), primary_key=False, nullable=False, default=text(u"'0000-00-00 00:00:00'")),
             Column('content', LONGTEXT(), primary_key=False, nullable=False),
             Column('title', TEXT(), primary_key=False, nullable=False),
             Column('excerpt', TEXT(), primary_key=False, nullable=False),
             Column('status', VARCHAR(length=20), primary_key=False, nullable=False, default=text(u"'publish'")),
             Column('comment_status', VARCHAR(length=20), primary_key=False, nullable=False, default=text(u"'open'")),
             Column('ping_status', VARCHAR(length=20), primary_key=False, nullable=False, default=text(u"'open'")),
             Column('password', VARCHAR(length=20), primary_key=False, nullable=False, default=text(u"''")),
             Column('name', VARCHAR(length=200), primary_key=False, nullable=False, default=text(u"''")),
             Column('to_ping', TEXT(), primary_key=False, nullable=False),
             Column('pinged', TEXT(), primary_key=False, nullable=False),
             Column('modified', DATETIME(), primary_key=False, nullable=False, default=text(u"'0000-00-00 00:00:00'")),
             Column('modified_gmt', DATETIME(), primary_key=False, nullable=False,
                    default=text(u"'0000-00-00 00:00:00'")),
             Column('content_filtered', LONGTEXT(), primary_key=False, nullable=False),
             Column('parent', BIGINT(display_width=20, unsigned=True), primary_key=False, nullable=False,
                    default=text(u"'0'")),
             Column('guid', VARCHAR(length=255), primary_key=False, nullable=False, default=text(u"''")),
             Column('menu_order', INTEGER(display_width=11), primary_key=False, nullable=False, default=text(u"'0'")),
             Column('type', VARCHAR(length=20), primary_key=False, nullable=False, default=text(u"'post'")),
             Column('mime_type', VARCHAR(length=100), primary_key=False, nullable=False, default=text(u"''")),
             Column('comment_count', BIGINT(display_width=20), primary_key=False, nullable=False, default=text(u"'0'")),


)
Index('parent', post.c.parent, unique=False)
Index('name', post.c.name, unique=False)
Index('author', post.c.author, unique=False)
Index('type_status_date', post.c.type, post.c.status, post.c.date, post.c.id, unique=False)

postmeta = Table('postmeta', metadata,
                 Column('meta_id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False),
                 Column('post_id', BIGINT(display_width=20, unsigned=True), primary_key=False, nullable=False,
                        default=text(u"'0'")),
                 Column('meta_key', VARCHAR(length=255), primary_key=False),
                 Column('meta_value', LONGTEXT(), primary_key=False),


)
Index('post_id', postmeta.c.post_id, unique=False)
Index('meta_key', postmeta.c.meta_key, unique=False)

stat_trace = Table('stat_trace', metadata,
                   Column('id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False),
                   Column('date', DATE(), primary_key=False, nullable=False),
                   Column('time', TIME(), primary_key=False, nullable=False),
                   Column('ip', VARCHAR(length=39), primary_key=False),
                   Column('request_uri', TEXT(), primary_key=False),
                   Column('agent', TEXT(), primary_key=False),
                   Column('referrer', TEXT(), primary_key=False),
                   Column('os', VARCHAR(length=128), primary_key=False),
                   Column('browser', VARCHAR(length=128), primary_key=False),
                   Column('search_engine', VARCHAR(length=128), primary_key=False),
                   Column('spider', VARCHAR(length=128), primary_key=False),
                   Column('feed', VARCHAR(length=128), primary_key=False),
                   Column('nation', VARCHAR(length=16), primary_key=False),
                   Column('real_post', INTEGER(display_width=11), primary_key=False),
)

term = Table('term', metadata,
             Column('id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False),
             Column('name', VARCHAR(length=200), primary_key=False, nullable=False, default=text(u"''")),
             Column('slug', VARCHAR(length=200), primary_key=False, nullable=False, default=text(u"''")),
             Column('term_group', BIGINT(display_width=10), primary_key=False, nullable=False, default=text(u"'0'")),


)
Index('slug', term.c.slug, unique=True)
Index('name', term.c.name, unique=False)

term_relationship = Table('term_relationship', metadata,
                          Column('object_id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False,
                                 default=text(u"'0'")),
                          Column('term_taxonomy_id', BIGINT(display_width=20, unsigned=True), primary_key=True,
                                 nullable=False, default=text(u"'0'")),
                          Column('term_order', INTEGER(display_width=11), primary_key=False, nullable=False,
                                 default=text(u"'0'")),


)
Index('term_taxonomy_id', term_relationship.c.term_taxonomy_id, unique=False)

term_taxonomy = Table('term_taxonomy', metadata,
                      Column('id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False),
                      Column('term_id', BIGINT(display_width=20, unsigned=True), primary_key=False, nullable=False,
                             default=text(u"'0'")),
                      Column('taxonomy', VARCHAR(length=32), primary_key=False, nullable=False, default=text(u"''")),
                      Column('description', LONGTEXT(), primary_key=False, nullable=False),
                      Column('parent', BIGINT(display_width=20, unsigned=True), primary_key=False, nullable=False,
                             default=text(u"'0'")),
                      Column('count', BIGINT(display_width=20), primary_key=False, nullable=False,
                             default=text(u"'0'")),


)
Index('term_id_taxonomy', term_taxonomy.c.term_id, term_taxonomy.c.taxonomy, unique=True)
Index('taxonomy', term_taxonomy.c.taxonomy, unique=False)

user = Table('user', metadata,
             Column('id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False),
             Column('login', VARCHAR(length=60), primary_key=False, nullable=False, default=text(u"''")),
             Column('password', VARCHAR(length=64), primary_key=False, nullable=False, default=text(u"''")),
             Column('nicename', VARCHAR(length=50), primary_key=False, nullable=False, default=text(u"''")),
             Column('email', VARCHAR(length=100), primary_key=False, nullable=False, default=text(u"''")),
             Column('url', VARCHAR(length=100), primary_key=False, nullable=False, default=text(u"''")),
             Column('registered', DATETIME(), primary_key=False, nullable=False,
                    default=text(u"'0000-00-00 00:00:00'")),
             Column('activation_key', VARCHAR(length=60), primary_key=False, nullable=False, default=text(u"''")),
             Column('status', INTEGER(display_width=11), primary_key=False, nullable=False, default=text(u"'0'")),
             Column('display_name', VARCHAR(length=250), primary_key=False, nullable=False, default=text(u"''")),


)
Index('login_key', user.c.login, unique=False)
Index('nicename', user.c.nicename, unique=False)

usermeta = Table('usermeta', metadata,
                 Column('umeta_id', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False),
                 Column('user_id', BIGINT(display_width=20, unsigned=True), primary_key=False, nullable=False,
                        default=text(u"'0'")),
                 Column('meta_key', VARCHAR(length=255), primary_key=False),
                 Column('meta_value', LONGTEXT(), primary_key=False),


)
Index('user_id', usermeta.c.user_id, unique=False)
Index('meta_key', usermeta.c.meta_key, unique=False)


def init_db():
    # create the table and tell it to create it in the
    # database engine that is passed
    metadata.create_all(engine)


def drop_db():
    # drop the table and tell it to drop it in the
    # database engine that is passed
    metadata.drop_all(engine)


def map_entities():
    from sqlalchemy.orm import mapper
    mapper(User, user)
    return metadata


class User(object):
    #----------------------------------------------------------------------
    def __init__(self, name, fullname, password):
        """Constructor"""
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

if __name__ == '__main__':
    drop_db()
    init_db()
    # pass