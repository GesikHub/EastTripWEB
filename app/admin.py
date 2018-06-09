from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user
from flask import redirect, url_for, request
from app.models import User


class AdminView(ModelView):
    def is_accessible(self):
        if not current_user.is_authenticated:
            return False
        else:
            user = User.query.filter_by(login=current_user.login).first()
            if user is None:
                redirect(url_for('register'))
            else:
                if user.role_id == 1:
                    return True
                else:
                    return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))


class HomeAdminView(AdminIndexView):
    def is_accessible(self):
        if not current_user.is_authenticated:
            return False
        else:
            user = User.query.filter_by(login=current_user.login).first()
            if user is None:
                redirect(url_for('auth.register'))
            else:
                if user.role_id == 1:
                    return True
                else:
                    return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))


class RouteView(ModelView):
    list_columns = ('id_route', 'language', 'name',)
    form_columns = ('id_route', 'language', 'name',)


class PointView(ModelView):
    list_columns = ('id_point', 'language', 'title',)
    form_columns = ('id_point', 'language', 'title',)
