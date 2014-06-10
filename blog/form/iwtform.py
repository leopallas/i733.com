#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-30 16:03
# Copyright 2014 LEO
from wtforms import Form
from wtforms import StringField

# class FormDataDict(dict):
#     '''Tornado handler arguments to MultiDict, wtforms required.'''
#     def __init__(self, arguments):
#         self.arguments = arguments
#
#     def __iter__(self):
#         return iter(self.arguments)
#
#     def __len__(self):
#         return len(self.arguments)
#
#     def __contains__(self, name):
#         return (name in self.arguments)
#
#     def getlist(self, key):
#         """
#         Returns the list of values for the passed key. If key doesn't exist,
#         then an empty list is returned.
#         """
#         try:
#             return [i.decode("utf-8") for i in self.arguments[key]]
#         except KeyError:
#             return []

# class Form(Form):
#     def __init__(self, handler=None, obj=None, prefix='', formdata=None, **kwargs):
#         if handler:
#             formdata = FormDataDict(handler.request.arguments)
#             self.handler = handler
#             self.current_user = handler.current_user
#         super(Form, self).__init__(formdata=formdata, **kwargs)


class Form(Form):
    """
    `WTForms` wrapper for Tornado.
    """
    def __init__(self, formdata=None, obj=None, prefix='', **kwargs):
        """
        Wrap the `formdata` with the `TornadoInputWrapper` and call the base
        constuctor.
        """
        self._handler = formdata
        super(Form, self).__init__(formdata=TornadoInputWrapper(self._handler), obj=obj, prefix=prefix, **kwargs)

    def _get_translations(self):
        return TornadoLocaleWrapper(self._handler.locale)

    # static_url = StringField('static', [InputRequired(), Length(max=32)])

class TornadoInputWrapper(object):

    def __init__(self, handler):
        self._handler = handler

    def __iter__(self):
        return iter(self._handler.request.arguments)

    def __len__(self):
        return len(self._handler.request.arguments)

    def __contains__(self, name):
        return (name in self._handler.request.arguments)

    def getlist(self, name):
        return self._handler.get_arguments(name)


class TornadoLocaleWrapper(object):

    def __init__(self, locale):
        self.locale = locale

    def gettext(self, message):
        return self.locale.translate(message)

    def ngettext(self, message, plural_message, count):
        return self.locale.translate(message, plural_message, count)