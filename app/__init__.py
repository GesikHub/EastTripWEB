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
    admin = Admin(app, name='eastTrip', template_mode='bootstrap3', url='/', index_view=HomeAdminView('Admin panel'))

    import app.models as models
    from app.admin import AdminView

    admin.add_view(AdminView(models.Place, db.session))
    admin.add_view(AdminView(models.User, db.session))
    admin.add_view(AdminView(models.Role, db.session))
    admin.add_view(AdminView(models.PlaceUser, db.session))
    admin.add_view(AdminView(models.Category, db.session))
    admin.add_view(AdminView(models.CategoryPlace, db.session))
    admin.add_view(AdminView(models.CurrencyType, db.session))
    admin.add_view(AdminView(models.TimeTable, db.session))
    admin.add_view(AdminView(models.TimeTableDay, db.session))
    admin.add_view(AdminView(models.Translate, db.session))
    admin.add_view(AdminView(models.Language, db.session))
    admin.add_view(AdminView(models.Service, db.session))
    admin.add_view(AdminView(models.ServicePlace, db.session))
    admin.add_view(AdminView(models.PaymentMethod, db.session))
    admin.add_view(AdminView(models.PaymentMethodPlace, db.session))
    admin.add_view(AdminView(models.Photo, db.session))
    return app
