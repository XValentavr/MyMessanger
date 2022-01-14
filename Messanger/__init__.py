# standard library imports
import os

from flask import Flask
from configuration import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

database = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from .views.homepage import messanger
    database.init_app(app)
    Migrate(app, database, directory=os.path.join('hospital_app', 'migrations'))
    login_manager.init_app(app)

    app.register_blueprint(messanger)
    return app
