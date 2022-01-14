"""
This module creates homepage page
"""
from flask import Blueprint, session, redirect, url_for
from flask import render_template
from flask_login import login_required

messanger = Blueprint('messanger', __name__)


@messanger.route('/')
@messanger.route('/home')
@login_required
def homepage():
    """
    Render the home page template on the / route
    """
    if 'UUID' in session:
        return render_template('index.html')
    return redirect(url_for('messanger.login'))
