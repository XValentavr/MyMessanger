from flask import render_template, make_response, request, session, flash, redirect
from flask_login import login_required

from .homepage import messanger
from ..service.profile_service import update_avatar, get_avatar, get_profiles, get_foreign_values


@messanger.route('/profile')
@login_required
def profile():
    flag = False
    if get_profiles(session['UUID']):
        flag = True
    return render_template('profile.html', flag=flag, info=get_profiles(session['UUID']),
                           foreign=get_foreign_values(session['UUID']))


@messanger.route('/avatar')
@login_required
def avatar():
    response = make_response(get_avatar(session['UUID']))
    response.headers['Content-Type'] = 'image/png'
    return response


@messanger.route('/upload', methods=["POST", "GET"])
@login_required
def upload():
    if request.method == 'POST':
        file = request.files['file']
        try:
            img = file.read()
            update_avatar(img, session['UUID'])
        except FileNotFoundError as e:
            flash("An error occured. Please try again.", "error")
    else:
        flash("An error occured. This format file is not supported. Use png.", "error")

    return redirect(request.referrer)
