#!/usr/bin/env python
# coding:utf-8
# Author: Yuanjun Ren

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Required(),
                                             Length(1, 64),
                                             Email()])
    password = PasswordField("Password", validators=[Required()])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField("Log In")
