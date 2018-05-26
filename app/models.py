from flask_user import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app import db, login
from db_enum import CurrencyEnum, DayEnum, LanguageEnum, ComfortEnum, PaymentMethodEnum


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128))
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id'))
    clients = db.relationship('Client', backref='clients', lazy='dynamic')
    place_user = db.relationship('PlaceUser', backref='places', lazy='dynamic')

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
    token = db.Column(db.String(256), unique=True)
    id_user = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return '<Client %r>' % (self.token)


class Place(db.Model):
    id_place = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.String(500))
    email = db.Column(db.String(350))
    website = db.Column(db.String(70))
    country = db.Column(db.String(60))
    city = db.Column(db.String(150))
    location = db.Column(db.String(40))
    address = db.Column(db.String(100))
    place_user = db.relationship('PlaceUser', backref='users', lazy='dynamic')
    place_category = db.relationship('CategoryPlace', backref='categories', lazy='dynamic')
    finance = db.relationship('Finance', backref='finances', lazy='dynamic')
    timetable_day = db.relationship('TimeTableDay', backref='timetable', lazy='dynamic')
    translate = db.relationship('Translate', backref='translate', lazy='dynamic')
    comfort = db.relationship('ComfortPlace', backref='comfort', lazy='dynamic')
    payment_method = db.relationship('PaymentMethodPlace', backref='methods', lazy='dynamic')
    photo = db.relationship('Photo', backref='photos', lazy='dynamic')

    def __repr__(self):
        return '<Place %r>' % self.name_l



class PlaceUser(db.Model):
    id_place_user = db.Column(db.Integer(), primary_key=True)
    id_user = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    id_place = db.Column(db.Integer(), db.ForeignKey('place.id_place'), nullable=False)

    def __repr__(self):
        return '<PlaceUser %r>' % str(self.id_user + ' ' + self.id_place)


class Category(db.Model):
    id_category = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(12))
    id_supergroup = db.Column(db.Integer())
    places = db.relationship('CategoryPlace', backref='places', lazy='dynamic')

    def __repr__(self):
        return '<Category %r>' % self.name


class CategoryPlace(db.Model):
    id_category_place = db.Column(db.Integer(), primary_key=True)
    id_place = db.Column(db.Integer(), db.ForeignKey('place.id_place'))
    id_category = db.Column(db.Integer(), db.ForeignKey('category.id_category'))

    def __repr__(self):
        return '<CategoryPlace %r>' % str(self.id_category + ' ' + self.id_place)


class Finance(db.Model):
    id_finance = db.Column(db.Integer(), primary_key=True)
    average_check = db.Column(db.Integer())
    currency = db.Column(db.Enum(CurrencyEnum))
    id_place = db.Column(db.Integer(), db.ForeignKey('place.id_place'))

    def __repr__(self):
        return '<Finance %r>' % self.id_finance


class TimeTable(db.Model):
    id_timetable = db.Column(db.Integer(), primary_key=True)
    open_time = db.Column(db.Time())
    close_time = db.Column(db.Time())
    days = db.relationship('TimeTableDay', backref='days', lazy='dynamic')

    def __repr__(self):
        return '<TimeTable %r>' % str(self.open_time + '-' + self.close_time)


class TimeTableDay(db.Model):
    id_timetable_day = db.Column(db.Integer(), primary_key=True)
    day = db.Column(db.Enum(DayEnum))
    id_place = db.Column(db.Integer(), db.ForeignKey('place.id_place'))
    id_timetable = db.Column(db.Integer(), db.ForeignKey('time_table.id_timetable'))

    def __repr__(self):
        return '<TimeTableDay %r>' % self.day


class Translate(db.Model):
    id_translate = db.Column(db.Integer(), primary_key=True)
    language = db.Column(db.Enum(LanguageEnum))
    name = db.Column(db.String(64))
    description = db.Column(db.String(500))
    address = db.Column(db.String(100))
    id_place = db.Column(db.Integer(), db.ForeignKey('place.id_place'))

    def __repr__(self):
        return '<Translate %r>' % self.name + self.language.value


class Comfort(db.Model):
    id_comfort = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.Enum(ComfortEnum))
    place = db.relationship('ComfortPlace', backref='places', lazy='dynamic')

    def __repr__(self):
        return '<Comfort %r>' % self.type


class ComfortPlace(db.Model):
    id_comfort_place = db.Column(db.Integer(), primary_key=True)
    id_place = db.Column(db.Integer(), db.ForeignKey('place.id_place'))
    id_comfort = db.Column(db.Integer(), db.ForeignKey('comfort.id_comfort'))

    def __repr__(self):
        return '<ComfortPlace %r>' % self.id_place + ' ' + self.id_comfort


class PaymentMethod(db.Model):
    id_payment_method = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.Enum(PaymentMethodEnum))
    place = db.relationship('PaymentMethodPlace', backref='places', lazy='dynamic')

    def __repr__(self):
        return '<PaymentMethod %r>' % self.type


class PaymentMethodPlace(db.Model):
    id_payment_place = db.Column(db.Integer(), primary_key=True)
    id_place = db.Column(db.Integer(), db.ForeignKey('place.id_place'))
    id_payment_method = db.Column(db.Integer(), db.ForeignKey('payment_method.id_payment_method'))

    def __repr__(self):
        return '<PaymentMethodPlace %r>' % self.id_place + ' ' + self.id_payment_method


class Photo(db.Model):
    id_photo = db.Column(db.Integer(), primary_key=True)
    url = db.Column(db.String(256))
    id_place = db.Column(db.Integer(), db.ForeignKey('place.id_place'))

    def __repr__(self):
        return '<Photo %r>' % self.url


class DateMainWindow(db.Model):
    time_zone = db.Column(db.Integer(), primary_key=True)
    weather = db.Column(db.Integer())
    euro = db.Column(db.Integer())

    def __repr__(self):
        return '<Date %r>' % self.time_zone
