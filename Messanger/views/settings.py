from flask import render_template, session
from flask_login import login_required

from .homepage import messanger


@messanger.route('/profile/settings')
@login_required
def settings():
    return render_template('settings.html', session=dict(session))
