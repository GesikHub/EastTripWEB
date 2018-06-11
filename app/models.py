from flask_user import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app import db, login


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128))
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id'))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % (self.login)


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(256))
    users = db.relationship('User', backref='users', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % (self.name)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class DateMainWindow(db.Model):
    time_zone = db.Column(db.Integer(), primary_key=True)
    weather = db.Column(db.Integer())
    euro = db.Column(db.Integer())

    def __repr__(self):
        return '<Date %r>' % self.time_zone


class RouteName(db.Model):
    id_route = db.Column(db.Integer(), db.ForeignKey('route.id_route'), primary_key=True)
    language = db.Column(db.Integer(), db.ForeignKey('language.id_language'), primary_key=True)
    name = db.Column(db.String(256))

    def __repr__(self):
        return '<Name %r>' % self.name

    def to_json(self):
        data = Route.query.filter_by(id_route=self.id_route).first()
        if data is None:
            return {}
        else:
            data = data.to_json()
            data['name'] = self.name
            return data


class Route(db.Model):
    id_route = db.Column(db.Integer(), primary_key=True)
    average_check = db.Column(db.Float())
    time = db.Column(db.Float())
    distance = db.Column(db.Float())
    photo_url = db.Column(db.String(200))
    points = db.relationship('PointName', backref='points', lazy='dynamic')

    def __repr__(self):
        return '<Route %r>' % self.id_route

    def to_json(self):
        return {'id': self.id_route, 'average_check': self.average_check, 'time': self.time,
                'distance': self.distance, 'photo_url': self.photo_url}

class Language(db.Model):
    id_language = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.String(5))
    routes = db.relationship('RouteName', backref='Language', lazy='dynamic')


class PointName(db.Model):
    id_point = db.Column(db.Integer(), db.ForeignKey('point.id_point'), primary_key=True)
    language = db.Column(db.Integer(), db.ForeignKey('language.id_language'), primary_key=True)
    id_route = db.Column(db.Integer(), db.ForeignKey('route.id_route'))
    title = db.Column(db.String(256))

    def __repr__(self):
        return '<PointName %r>' % self.title

    def to_json(self):
        data = Point.query.filter_by(id_point=self.id_point).first()
        if data is None:
            return {}
        else:
            data = data.to_json()
            data['title'] = self.title
            return data


class Point(db.Model):
    id_point = db.Column(db.Integer(), primary_key=True)
    id = db.Column(db.String(10))
    latitude = db.Column(db.String(15))
    longitude = db.Column(db.String(15))
    subtitle = db.Column(db.String(100))
    illustration = db.Column(db.String(100))

    def __repr__(self):
        return  '<Point %r>' % self.title

    def to_json(self):
        return { 'coordinates': {'latitude': self.latitude, 'longitude': self.longitude},
        'id': self.id,
        'subtitle': self.subtitle,
        'illustration': self.illustration }
