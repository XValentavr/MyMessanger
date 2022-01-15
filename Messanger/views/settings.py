from flask import render_template
from flask_login import login_required

from .homepage import messanger


@messanger.route('/settings')
@login_required
def settings():
    return render_template('settings.html')
