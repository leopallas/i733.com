#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-30 16:03
# Copyright 2014 LEO

import wtforms
from wtforms import widgets, validators, StringField, PasswordField, TextAreaField
from wtforms.validators import Length, InputRequired, Email, EqualTo
from wtforms.fields import IntegerField, DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class Form(wtforms.Form):
    """
    `WTForms` wrapper for Tornado.
    """
    def __init__(self, handler=None, formdata=None, obj=None, prefix='', **kwargs):
        """
        Wrap the `formdata` with the `TornadoInputWrapper` and call the base
        constuctor.
        """
        if handler:
            self._handler = handler
        super(Form, self).__init__(formdata=TornadoInputWrapper(self._handler), obj=obj, prefix=prefix, **kwargs)

    def _get_translations(self):
        return TornadoLocaleWrapper(self._handler.locale)


class TornadoInputWrapper(object):

    def __init__(self, handler):
        self._handler = handler

    def __iter__(self):
        return iter(self._handler.request.arguments)

    def __len__(self):
        return len(self._handler.request.arguments)

    def __contains__(self, name):
        return name in self._handler.request.arguments

    def getlist(self, name):
        return self._handler.get_arguments(name)


class TornadoLocaleWrapper(object):

    def __init__(self, locale):
        self.locale = locale

    def gettext(self, message):
        return self.locale.translate(message)

    def ngettext(self, message, plural_message, count):
        return self.locale.translate(message, plural_message, count)


class TextInput(widgets.TextInput):
    def __call__(self, field, **kwargs):
        if field.errors:
            c = kwargs.pop('class', '') or kwargs.pop('class_', '')
            kwargs['class'] = u'%s %s' % ('error', c)

        for validator in field.validators:
            if type(validator) == validators.Length and validator.max > 0:
                kwargs['maxlength'] = str(validator.max)

        return super(TextInput, self).__call__(field, **kwargs)


class PasswordInput(widgets.PasswordInput):
    def __call__(self, field, **kwargs):
        if field.errors:
            c = kwargs.pop('class', '') or kwargs.pop('class_', '')
            kwargs['class'] = u'%s %s' % ('error', c)

        for validator in field.validators:
            if type(validator) == validators.Length and validator.max > 0:
                kwargs['maxlength'] = str(validator.max)

        return super(PasswordInput, self).__call__(field, **kwargs)


class Select(widgets.Select):
    def __call__(self, field, **kwargs):
        c = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class'] = u'%s %s' % ('expand', c)

        if field.errors:
            c = kwargs.pop('class', '') or kwargs.pop('class_', '')
            kwargs['class'] = u'%s %s' % ('error', c)

        return super(Select, self).__call__(field, **kwargs)


class SelectField(wtforms.SelectField):
    widget = Select()


class AdminLoginForm(Form):
    username = StringField(u'用户名', [InputRequired(), Length(max=32)], widget=TextInput())
    # username = StringField(u'用户名', [validators.input_required(), validators.length(max=32)], widget=TextInput())
    password = PasswordField(u'密码', [InputRequired(), Length(min=6, max=60)], widget=PasswordInput())


class PostAddForm(Form):
    title = StringField(u'Title', [InputRequired(), Length(min=4)], widget=TextInput())
    parent = QuerySelectField(get_label=u'title', allow_blank=True, blank_text=u'默认')
    content = TextAreaField(u'Content', [InputRequired(), Length(min=10)])
    excerpt = TextAreaField(u'Except')
    date = DateField(u'Date', [InputRequired()])


class UserEditForm(Form):
    displayname = StringField(u'Displayname', [InputRequired(), Length(min=2, max=32)])
    email = StringField(u'Email Address', [InputRequired(), Length(min=6, max=250), Email()])
    password0 = PasswordField(u'Old Password', [InputRequired(), Length(min=6, max=32)])
    password1 = PasswordField(u'New Password', [InputRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField(u'Confirm', [InputRequired(), Length(min=6, max=32)])


class PageAddForm(Form):
    title = StringField(u'Name', [InputRequired(), Length(min=1, max=20)])
    parent = QuerySelectField(get_label='title', allow_blank=True, blank_text=u'Default')
    description = TextAreaField(u'Content')
    order = IntegerField(u'Order', [InputRequired()])


class TermAddForm(Form):
    name = StringField(u'Name', [InputRequired(), Length(min=1, max=20)])
    parent = QuerySelectField(get_label='name', allow_blank=True, blank_text=u'Default')
    description = TextAreaField(u'Description')
