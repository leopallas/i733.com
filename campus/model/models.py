#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-16 12:14
# Copyright 2014 LEO

from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy.ext.declarative.clsregistry import _deferred_relationship

import logging

metaData = MetaData()

# engine = create_engine("mysql://root:root@192.168.1.101:3306/blog?charset=utf8", encoding="utf-8", echo=True)
# engine = create_engine('sqlite:///:memory:', echo=True)
# engine = create_engine('sqlite://', echo=True)
engine = create_engine('sqlite:////home/xw/foo.db', echo=True)

Base = declarative_base()  # declarative base class for SQLAlchemy


def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

class User(Base):
    __tablename__ = 'users'

    id = Column('ID', Integer(11), primary_key=True)
    name = Column('NAME', String(24))
    fullname = Column('FULL_NAME', String(24))
    password = Column('PASSWORD', String(24))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)

#
# User.__table__
# #
# # Table('users', metaData,
# #             Column('id', Integer, primary_key=True, nullable=False),
# #             Column('name', String(24),),
# #             Column('fullname', String(24)),
# #             Column('password', String(24)), schema=None)
#
# # metaData.create_all(engine)
# Base.metadata.create_all(engine)
#
# ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
#
# from sqlalchemy.orm import sessionmaker
#
# Session = sessionmaker(bind=engine)
#
# # Session = sessionmaker()
# # Session.configure(bind=engine)  # once engine is available
#
# session = Session()
# session.add(ed_user)
#
# our_user = session.query(User).filter_by(name='ed').first()
# print our_user
# if ed_user is our_user:
#     print 'true'
#
# session.add_all([
#     User(name='wendy', fullname='Wendy Williams', password='foobar'),
#     User(name='mary', fullname='Mary Contrary', password='xxg527'),
#     User(name='fred', fullname='Fred Flinstone', password='blah')
# ])
#
# ed_user.id
#
# ed_user.password = 'f8s7ccs'
# session.dirty
# session.new
#
# class ThingOne(object):
#     def go(self):
#         session = Session()
#         try:
#             session.query(User).update({'name', '5'})
#             session.commit()
#         except:
#             session.rollback()
#             raise

# session.commit()


        # class User(Base):
        #     """ SQLAlchemy ORM, mapping ot table user """
        #     __tablename__ = 'user'
        #
        #     usrId = Column("USR_ID", String(24), primary_key=True)
        #     comId = Column("COM_ID", String(24), nullable=False)
        #     usrName = Column("USR_NAME", String(50), nullable=False)
        #     usrPwd = Column("USR_PWD", String(24), nullable=False)
        #     usrRealName = Column("USR_REAL_NAME", String(50))
        #     usrIcType = Column("USR_IC_TYPE", Integer(11))
        #     usrIc = Column("USR_IC", String(50))
        #     usrType = Column("USR_TYPE", Integer(11), nullable=False)
        #     usrEmail = Column("USR_EMAIL", String(50))
        #     usrPhone = Column("USR_PHONE", String(50))
        #     createDt = Column("CREATE_DT", DateTime, nullable=False)
        #     updateDt = Column("UPDATE_DT", DateTime, nullable=False)
        #
        #
        #
        #
        # def init_db(engine):
        #     Base.metadata.create_all(bind=engine)
        #
        #
        # class entity(object):
        #     def __init__(self, field1, field2):
        #         self.field1 = field1
        #         self.field2 = field2
        #
        #
        # class entity_repository():
        #     def __init__(self, session):
        #         self.session = session
        #
        #     def load(self, id):
        #         return self.session.query(entity).filter(entity.id == id).first()
        #
        #     def save(self, instance):
        #         self.session.add(instance)
        #         self.session.commit()
        #
        #     def remove(self, instance):
        #         self.session.delete(instance)
        #         self.session.commit()
        #
        #     def list(self):
        #         return self.session.query(entity).all()
        #
        #
        # class ModelWrapper(object):
        #     """
        #         Wrapper around sqlalchemy model for having some easier functions
        #     """
        #
        #     def __init__(self, model):
        #         self.model = model
        #
        #     @property
        #     def __name__(self):
        #         return self.model.__name__
        #
        #     @property
        #     def __collectionname__(self):
        #         try:
        #             return self.model.__collectionname__
        #         except AttributeError:
        #             logging.warning("Missing collection name for %s using tablename" % self.model.__name__)
        #             return self.model.__tablename__
        #
        #
        #
        #             # CREATE TABLE `user` (
        #             #   `USR_ID` varchar(24) NOT NULL COMMENT '用户ID',
        #             #   `COM_ID` varchar(24) DEFAULT NULL COMMENT '社区ID',
        #             #   `USR_NAME` varchar(50) NOT NULL COMMENT '用户名',
        #             #   `USR_PWD` varchar(50) NOT NULL COMMENT '用户密码',
        #             #   `USR_REAL_NAME` varchar(50) DEFAULT NULL COMMENT '用户真实姓名',
        #             #   `USR_IC_TYPE` int(11) DEFAULT NULL COMMENT '用户证件类型(1=身份证, 2=护照, 3=其它证件)',
        #             #   `USR_IC` varchar(50) DEFAULT NULL COMMENT '用户证件号',
        #             #   `USR_TYPE` int(11) NOT NULL COMMENT '用户类型(1=普通帐户，2=子帐户，3=主帐户)',
        #             #   `USR_EMAIL` varchar(50) DEFAULT NULL COMMENT '用户电子邮箱',
        #             #   `USR_PHONE` varchar(50) DEFAULT NULL COMMENT '用户手机',
        #             #   `CREATE_DT` datetime NOT NULL COMMENT '创建时间',
        #             #   `UPDATE_DT` datetime NOT NULL COMMENT '更新时间',
        #             #   PRIMARY KEY (`USR_ID`)
        #             # ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';