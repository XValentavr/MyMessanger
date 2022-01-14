"""
This module represents the logic of authentication of user
"""
from flask import render_template, flash, redirect, url_for, session
import uuid

from flask_login import login_user

from .homepage import messanger
from Messanger.service import user
from . import WTFFormRegister
from werkzeug.security import generate_password_hash


@messanger.route('/register', methods=["POST", "GET"])
def register():
    register_form = WTFFormRegister.RegisterForm()
    if register_form.validate_on_submit():
        if user.get_user_by_name(login=register_form.username.data) is None and user.get_user_by_phone(
                phone=register_form.phone.data) is None:
            user.authorize_user(password=generate_password_hash(register_form.password.data),
                                login=register_form.username.data,
                                phone=register_form.phone.data,
                                UUID=uuid.uuid4())
            flash('you have been registered successfully registered', 'success')
            current_user = user.get_user_by_name(register_form.username.data)
            login_user(current_user)
            session['UUID'] = current_user.UUID
            return redirect(url_for('messanger.homepage'))
        else:
            flash('Your login or number are already taken. Select another ', 'error')
    return render_template('register.html', form=register_form)