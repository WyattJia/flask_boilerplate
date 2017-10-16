# -*- coding:utf-8 -*-
# __author__ = 'Wells Jia'
# flask_boilerplate 后端首页

from flask import make_response, request
from flask import url_for, g, redirect, current_app

from flask.ext.login import current_user, login_required, \
    login_user, logout_user
from sqlalchemy import or_

from flask_boilerplate.admin import admin, theme
from flask_boilerplate.extensions import lgm
from flask_boilerplate.models import User
from flask_boilerplate.forms import LoginForm
from flask_boilerplate.helpers import render_theme_template
from flask_boilerplate.helpers import verify_password
from flask_boilerplate.extensions import cache


@admin.before_request
def before_request():
    g.user = current_user


@lgm.user_loader
def user_loader(uid):
    return User.query.get(int(uid))


@admin.route('/')
@login_required
def index():
    return render_theme_template(theme, 'index.html')

