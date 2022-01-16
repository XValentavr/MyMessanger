"""
This module creates homepage page
"""
from flask import Blueprint, session, redirect, url_for
from flask import render_template

messanger = Blueprint('messanger', __name__)


@messanger.route('/')
@messanger.route('/home')
def homepage():
    """
    Render the home page template on the / route
    """
    if 'UUID' in session:
        return render_template('index.html')
    return redirect(url_for('messanger.login'))


@messanger.app_errorhandler(404)
def handle_404(err):
    """
    Handel 404 error and redirect to 404.html page
    """
    return render_template('404.html'), 404


@messanger.app_errorhandler(401)
def handle_401(err):
    """
    Handel 404 error and redirect to 404.html page
    """
    return render_template('401.html'), 401
