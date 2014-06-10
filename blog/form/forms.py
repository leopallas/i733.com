#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-30 16:03
# Copyright 2014 LEO


from iwtform import Form
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import Length, InputRequired, Email, EqualTo
from wtforms.fields import IntegerField, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class AdminLoginForm(Form):
    username = StringField(u'用户名', [InputRequired(), Length(max=32)])
    password = PasswordField(u'密码', [InputRequired(), Length(min=6, max=60)])


class UserEditForm(Form):
    displayname = StringField(u'Displayname', [InputRequired(), Length(min=2, max=32)])
    email = StringField(u'Email Address', [InputRequired(), Length(min=6, max=250), Email()])
    password0 = PasswordField(u'Old Password', [InputRequired(), Length(min=6, max=32)])
    password1 = PasswordField(u'New Password', [InputRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField(u'Confirm', [InputRequired(), Length(min=6, max=32)])


class PostAddForm(Form):
    title = StringField(u'Title', [InputRequired(), Length(min=4)])
    parent = QuerySelectField(get_label=u'title', allow_blank=True, blank_text=u'默认')
    content = TextAreaField(u'Content', [InputRequired(), Length(min=10)])
    excerpt = TextAreaField(u'Except')
    date = DateField(u'Date', [InputRequired()])


class PageAddForm(Form):
    title = StringField(u'Name', [InputRequired(), Length(min=1, max=20)])
    parent = QuerySelectField(get_label='title', allow_blank=True, blank_text=u'Default')
    description = TextAreaField(u'Content')
    order = IntegerField(u'Order', [InputRequired()])


class TermAddForm(Form):
    name = StringField(u'Name', [InputRequired(), Length(min=1, max=20)])
    parent = QuerySelectField(get_label='name', allow_blank=True, blank_text=u'Default')
    description = TextAreaField(u'Description')
