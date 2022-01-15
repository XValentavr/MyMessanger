from flask import render_template
from flask_login import login_required

from .homepage import messanger


@messanger.route('/profile')
@login_required
def profile():
    return render_template('profile.html')
