"""
This module represents the logic of authentication of user
"""
from datetime import timedelta

from flask import render_template, redirect, session, app, url_for, flash
from flask_login import login_required, logout_user, login_user
from .homepage import messanger
from . import WTFormLogin
from Messanger.service import user_service
from Messanger import login_manager
from werkzeug.security import check_password_hash


@login_manager.user_loader
def load_user(UUID):
    return user_service.Authorize.query.get(UUID)


@messanger.route('/login', methods=["POST", "GET"])
def login():
    """
    Handle requests to the /login route
    Cretates login page using WTForm using post-requests.
    Admin data contains in MySQL database

    :return: html page
    """
    form = WTFormLogin.LoginForm()
    if 'UUID' in session:
        return redirect(url_for('messanger.homepage'))
    elif form.validate_on_submit():
        current_user = user_service.get_user_by_name(form.username.data)
        if form.remember.data:
            session.permanent = True
            app.permanent_session_lifetime = timedelta(hours=24)
        if current_user is not None and check_password_hash(current_user.password, form.password.data):
            login_user(current_user)
            session['UUID'] = current_user.UUID
            return redirect(url_for('messanger.homepage'))
        flash('An error occured. Try again', 'error')
    return render_template('login.html', form=form)


@messanger.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Allow  to logout moving to home page.
    """
    logout_user()
    session.pop('UUID')
    return redirect(url_for('messanger.homepage'))
