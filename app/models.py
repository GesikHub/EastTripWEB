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
    clients = db.relationship('Client', backref='clients', lazy='dynamic')
    place = db.relationship('Place', backref='places', lazy='dynamic')

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


class Client(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    token = db.Column(db.String(512), unique=True)
    id_user = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return '<Client %r>' % (self.token)


class Place(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    photo_name = db.Column(db.String(256))
    name = db.Column(db.String(256))
    name_l = db.Column(db.String(256))
    email = db.Column(db.String(256))
    website = db.Column(db.String(256))
    address = db.Column(db.String(256))
    address_l = db.Column(db.String(256))
    country = db.Column(db.String(64))
    city = db.Column(db.String(64))
    type_establ = db.Column(db.String(32))
    location = db.Column(db.String(128))
    id_user = db.Column(db.Integer(), db.ForeignKey("user.id"))
    time = db.relationship('TimeTable', backref='tables', lazy='dynamic')
    comfort = db.relationship('Comfort', backref='comforts', lazy='dynamic')
    finance = db.relationship('Finance', backref='finances', lazy='dynamic')

    def __repr__(self):
        return '<Place %r>' % (self.name_l)


class TimeTable(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    day = db.Column(db.Integer())
    open_time = db.Column(db.Time())
    close_time = db.Column(db.Time())
    id_place = db.Column(db.Integer(), db.ForeignKey("place.id"), nullable=False)

    def __repr__(self):
        return '<Table %r>' % (self.day)


class Comfort(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    socket = db.Column(db.Boolean(), default=False)
    welcome = db.Column(db.Boolean(), default=False)
    forChildren = db.Column(db.Boolean(), default=False)
    animal = db.Column(db.Boolean(), default=False)
    rentBikes = db.Column(db.Boolean(), default=False)
    polygraph = db.Column(db.Boolean(), default=False)
    ramp = db.Column(db.Boolean(), default=False)
    specialToilet = db.Column(db.Boolean(), default=False)
    specialService = db.Column(db.Boolean(), default=False)
    id_place = db.Column(db.Integer(), db.ForeignKey("place.id"))

    def is_null(self):
        if self.socket is True:
            return False
        if self.welcome is True:
            return False
        if self.forChildren is True:
            return False
        if self.animal is True:
            return False
        if self.rentBikes is True:
            return False
        if self.polygraph is True:
            return False
        if self.ramp is True:
            return False
        if self.specialToilet is True:
            return False
        if self.specialToilet is True:
            return False
        return True

    def __repr__(self):
        return '<Place %r>' % (self.id)


class Finance(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    debit_card = db.Column(db.Boolean(), default=False)
    credit_card = db.Column(db.Boolean, default=False)
    electronic_payment = db.Column(db.Boolean(), default=False)
    average_check = db.Column(db.Integer())
    currency = db.Column(db.String(4))
    id_place = db.Column(db.Integer(), db.ForeignKey("place.id"))

    def __repr__(self):
        return '<Finance %r>' % (self.average_check)
