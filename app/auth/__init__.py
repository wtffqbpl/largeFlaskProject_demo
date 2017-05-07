#!/usr/bin/env python
# coding:utf-8
# Author: Yuanjun Ren

from flask import Blueprint

auth = Blueprint("auth", __name__)

from . import views