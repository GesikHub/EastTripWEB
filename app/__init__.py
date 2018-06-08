from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_restful import Resource, reqparse


bootstrap = Bootstrap()
login = LoginManager()
login.login_view = 'auth.login'
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    bootstrap.init_app(app)
    login.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.auth import bp as bp_login
    app.register_blueprint(bp_login)

    from app.main import bp as bp_main
    app.register_blueprint(bp_main)

    from app.api import bp as bp_api
    app.register_blueprint(bp_api)

    from app.admin import HomeAdminView
    admins = Admin(app, name='eastTrip', template_mode='bootstrap3', url='/', index_view=HomeAdminView('Home'))

    from app.models import (User, Role, Language, Route, Point)
    from app.admin import AdminView

    admins.add_view(AdminView(User, db.session))
    admins.add_view(AdminView(Role, db.session))
    admins.add_view(AdminView(Language, db.session))
    admins.add_view(AdminView(Route, db.session))
    admins.add_view(AdminView(Point, db.session))

    return app
