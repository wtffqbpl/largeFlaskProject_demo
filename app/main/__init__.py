#!/usr/bin/env python
# coding:utf-8
# Author: Yuanjun Ren

from flask import Blueprint

main = Blueprint("main", __name__)

from . import views, errors