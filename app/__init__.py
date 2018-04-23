from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


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

    from app.places import bp as bp_place
    app.register_blueprint(bp_place)

    from app.change import bp as bp_change
    app.register_blueprint(bp_change)

    from app.admin import HomeAdminView
    admins = Admin(app, name='eastTrip', template_mode='bootstrap3', url='/', index_view=HomeAdminView('Home'))

    from app.models import (User, Role, Client, Place,
                            TimeTable, Comfort, Finance)
    from app.admin import AdminView

    admins.add_view(AdminView(User, db.session))
    admins.add_view(AdminView(Role, db.session))
    admins.add_view(AdminView(Client, db.session))
    admins.add_view(AdminView(Place, db.session))
    admins.add_view(AdminView(TimeTable, db.session))
    admins.add_view(AdminView(Comfort, db.session))
    admins.add_view(AdminView(Finance, db.session))

    return app
