#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-16 11:11
# Copyright 2014 LEO

"""
Contains reCaptcha fields for WTForms which can be used
for various forms. This library depends on `recaptcha-client` ~> 1.0.6.
Example usage is below.

Defining a form with a ``RecaptchaField``:

    from wtforms import Form
    from recaptcha_field import RecaptchaField

    class MyForm(Form):
        captcha = RecaptchaField(public_key="my_pub_key",
                                 private_key="my_private_key")

Showing the field (example template):

    Verify you're human: {{ form.captcha() }}

Validating the input, example code from a potentional handler
in a web framework:

    form = MyForm(request.arguments,
                  captcha=dict(remote_addr=request.remote_ip))
    if form.validate():
        # Do something, the form is valid!
    else:
        # Invalid form.

"""

from recaptcha.client import captcha
from wtforms.fields import Field
from wtforms.validators import ValidationError

_unset_value = object()

class RecaptchaWidget(object):
    """
    This is the widget which displays reCaptcha objects. This is used by
    default for the RecaptchaField and isn't usually used on its own.
    """

    def __call__(self, field):
        if not isinstance(field, RecaptchaField):
            raise ValueError, "RecaptchaWidget can only be attached to a RecaptchaField"

        return captcha.displayhtml(field.public_key)

class RecaptchaValidator(object):
    """
    This is a validator for a RecaptchaField. Note that this is typically
    not used directly, since the RecaptchaField automatically adds this
    validator.
    """

    def __init__(self, message=None):
        if not message:
            message = "Incorrect response."

        self.message = message

    def __call__(self, form, field):
        if not isinstance(field, RecaptchaField):
            raise ValueError, "RecaptchaValidator can only be attached to a RecaptchaField"

        # Validate the reCaptcha data with the reCaptcha service.
        response = captcha.submit(
            field.challenge,
            field.data,
            field.private_key,
            field.remote_addr
        )

        if not response.is_valid:
            raise ValidationError(self.message)

class RecaptchaField(Field):
    """
    This field represents a reCaptcha field. This uses the RecaptchaWidget
    to show a reCaptcha entry field and will also handle validation for you.
    """

    widget = RecaptchaWidget()

    def __init__(self, label="", public_key=None, private_key=None, secure=False, **kwargs):
        """
        Initialize a reCaptcha field. ``public_key`` and ``private_key``, though
        they appear optional, are in fact required (they are only optional due to
        fields by default having optional arguments).
        """

        # Create the field with the reCaptcha validator, since that
        # is the whole point.
        super(RecaptchaField, self).__init__(label, [RecaptchaValidator()], **kwargs)

        if not public_key or not private_key:
            raise ValueError, "reCaptcha public_key and private_key are required."

        self.public_key = public_key
        self.private_key = private_key
        self.secure = secure

    def process(self, formdata, data=_unset_value):
        self.process_errors = []

        # The data is always expected to be the remote IP address,
        # since reCaptcha uses this to validate the response
        self.remote_addr = None
        if isinstance(data, dict):
            self.remote_addr = data.pop("remote_addr", None)

        if formdata is not None:
            if not self.remote_addr:
                raise ValueError, "Must set remote_addr on data for captcha."

            # reCaptcha sends two fields with it: challenge and response.
            # We need to capture both and put them in the data for this
            # field.
            challenge = formdata.getlist("recaptcha_challenge_field")
            if not challenge:
                raise ValueError, self.gettext("reCaptcha challenge data not sent.")
            self.challenge = challenge[0]

            self.data = None
            self.raw_data = formdata.getlist("recaptcha_response_field")
            self.process_formdata(self.raw_data)

        for filter in self.filters:
            try:
                self.data = filter(self.data)
            except ValueError, e:
                self.process_errors.append(e.args[0])