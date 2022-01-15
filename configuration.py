"""Specify configurations"""
from datetime import timedelta


class Config(object):
    """
    Base configuration for flask site
    """
    PERMANENT_SESSION_LIFETIME = timedelta(hours=60)
    MAX_CONTENT_LENGTH = 1024 * 1024
    SECRET_KEY = '7b0342f12ee64296aaaa9738c72ca2c4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/messanger'
