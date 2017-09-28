# -*- coding:utf-8 -*-
# __author__ = 'Wells Jia'
# flask_boilerplate 管理后台视图

from flask import request, flash, redirect, url_for, \
    abort, current_app

from flask.ext.login import login_required
from MySQLdb import MySQLError

from flask_boilerplate.forms import AddForm

from flask_boilerplate.admin import admin, theme
from flask_boilerplate.helpers import render_theme_template
from flask_boilerplate.helpers import _id_match, get_sorts
from flask_boilerplate.extensions import db


@admin.route('/admin_blog', methods=["GET", "POST"])
@login_required
def admin_blog():
    form = AddForm()
    if request.method == 'POST' and form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        excerpt = form.excerpt.data

        return title + content + excerpt
    sorts = get_sorts()
    return render_theme_template(theme, 'addBlog.html', form=form, sorts=sorts)


