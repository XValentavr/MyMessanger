from flask import render_template, make_response, request, session, flash, redirect, url_for
from flask_login import login_required

from .homepage import messanger
from ..service.profile_service import check_if_is_available, update_avatar, get_avatar


@messanger.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@messanger.route('/avatar')
@login_required
def avatar():
    response = make_response(get_avatar(session['_user_id']))
    response.headers['Content-Type'] = 'image/png'
    return response


@messanger.route('/upload', methods=["POST", "GET"])
@login_required
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and check_if_is_available(file.filename):
            try:
                img = file.read()
                update_avatar(img, session['_user_id'])
            except FileNotFoundError as e:
                flash("An error occured. Please try again.", "error")
        else:
            flash("An error occured. This format file is not supported. Use png.", "error")

    return redirect(url_for('messanger.profile'))
