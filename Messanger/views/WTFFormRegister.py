"""
This module creates WTForm to provide security of authentication

"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    """
    creates login form to authorize
    """
    username = StringField('Your name:', validators=[DataRequired(), Length(min=4, max=25,
                                                                            message='Field must be between 4 '
                                                                                    'and 25 characters long.')])
    password = PasswordField('Password:     ', validators=[DataRequired(), Length(min=4, max=100)])
    phone = StringField('Phone number: ', validators=[DataRequired(), Length(min=4, max=16)])

    register = SubmitField('Register')
