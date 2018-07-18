from flask_user import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app import db, login
from db_enum import DayEnum


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


class Place(db.Model):
    id_place = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.String(500))
    email = db.Column(db.String(350))
    website = db.Column(db.String(70))
    country = db.Column(db.String(60))
    city = db.Column(db.String(150))
    rating = db.Column(db.Integer)
    address = db.Column(db.String(100))
    number_of_reviews = db.Column(db.Integer)
    latitude = db.Column(db.String(20))
    longitude = db.Column(db.String(20))
    average_check = db.Column(db.Float())
    id_currency = db.Column(db.Integer, db.ForeignKey('currency_type.id_currency'))
    place_user = db.relationship('PlaceUser', backref='users', lazy='dynamic')
    place_category = db.relationship('CategoryPlace', backref='categories', lazy='dynamic')
    timetable_day = db.relationship('TimeTableDay', backref='timetable', lazy='dynamic')
    translate = db.relationship('Translate', backref='translate', lazy='dynamic')
    comfort = db.relationship('ServicePlace', backref='comfort', lazy='dynamic')
    payment_method = db.relationship('PaymentMethodPlace', backref='methods', lazy='dynamic')
    photo = db.relationship('Photo', backref='photos', lazy='dynamic')

    def __repr__(self):
        return '<Place %r>' % self.name

    def get_information(self):
        information = {'main_information': {'id_place': self.id_place, 'name': self.name,  'average_check': self.average_check,
                                                        'currency':
                                                            CurrencyType.query.filter_by(id_currency=self.id_currency).first().type,
                                                        'latitude': self.latitude, 'longitude': self.longitude},
                                   'additional_information':
                                                       {'description': self.description, 'email': self.email,
                                                        'website': self.website,
                                                        'country': self.country, 'city': self.city,
                                                        'rating': self.rating, 'address': self.address}}
        photos = [url.url for url in Photo.query.filter_by(id_place=self.id_place).all()]
        information['main_information']['photo_url'] = photos
        time_inf = [time_table.to_json() for time_table in TimeTableDay.query.filter_by(id_place=self.id_place).all()]
        service_id = [service.id_comfort for service in ServicePlace.query.filter_by(id_place=self.id_place).all()]
        service_inf = []
        for id in service_id:
            service_check = Service.query.filter_by(id_service=id)
            if service_check is not None:
                service_inf.append(service_check.name)
        payment_method_id = [payment.id_payment_method for payment in PaymentMethodPlace.query.filter_by(id_place=self.id_place).all()]
        payment_method_info = []
        for id in payment_method_id:
            payment_check = PaymentMethod.query.filter_by(id_payment_method=id)
            if payment_check is not None:
                payment_method_info.append(payment_check.name)
        information['main_information']['service'] = service_inf
        information['main_information']['payment_method'] = payment_method_info
        information['additional_information']['time_table'] = time_inf
        return information

    def add_timetable_day(self, open_time, close_time, day):
        time = TimeTable.query.filter_by(open_time=open_time, close_time=close_time).first()
        if time is None:
            time = TimeTable(open_time=open_time, close_time=close_time)
            db.session.add(time)
            db.session.commit()
        time_m = TimeTableDay(id_place=self.id_place, id_timetable=time.id_timetable, day=day)
        db.session.add(time_m)
        db.session.commit()

    def add_service(self, service):
        service_place = ServicePlace(id_place=self.id_place,
                                     id_comfort=Service.query.filter_by(type=service).first().id_service())
        db.session.add(service_place)
        db.session.commit()

    def add_payment_method(self, payment_method):
        payment_method_place = PaymentMethodPlace(id_place=self.id_place,
                                                  id_payment_method=PaymentMethod.query.filter_by(type=payment_method.first().id_payment_method))
        db.session.add(payment_method_place)
        db.session.commit()


class PlaceUser(db.Model):
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False, primary_key=True)
    id_place = db.Column(db.Integer, db.ForeignKey('place.id_place'), nullable=False, primary_key=True)

    def __repr__(self):
        return '<PlaceUser %r>' % str(self.id_user + ' ' + self.id_place)


class Category(db.Model):
    id_category = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(12))
    name = db.Column(db.String(12))
    id_supergroup = db.Column(db.Integer)
    places = db.relationship('CategoryPlace', backref='places', lazy='dynamic')

    def __repr__(self):
        return '<Category %r>' % self.name


class CategoryPlace(db.Model):
    id_place = db.Column(db.Integer, db.ForeignKey('place.id_place'), primary_key=True)
    id_category = db.Column(db.Integer, db.ForeignKey('category.id_category'), primary_key=True)

    def __repr__(self):
        return '<CategoryPlace %r>' % str(self.id_category + ' ' + self.id_place)


class CurrencyType(db.Model):
    id_currency = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(5))
    name = db.Column(db.String(5))
    places = db.relationship('Place', backref='finances', lazy='dynamic')

    def __repr__(self):
        return '<Finance %r>' % self.id_currency


class TimeTable(db.Model):
    id_timetable = db.Column(db.Integer, primary_key=True)
    open_time = db.Column(db.String(5))
    close_time = db.Column(db.String(5))
    days = db.relationship('TimeTableDay', backref='days', lazy='dynamic')

    def __repr__(self):
        return '<TimeTable %r>' % str(self.open_time + '-' + self.close_time)


class TimeTableDay(db.Model):
    day = db.Column(db.Enum(DayEnum), primary_key=True)
    id_place = db.Column(db.Integer, db.ForeignKey('place.id_place'), primary_key=True)
    id_timetable = db.Column(db.Integer, db.ForeignKey('time_table.id_timetable'))

    def __repr__(self):
        return '<TimeTableDay %r>' % self.day

    def to_json(self):
        return {self.day.value: {'open_time': TimeTable.query.filter_by(id_timetable=self.id_timetable).first().open_time,
                                 'close_time': TimeTable.query.filter_by(id_timetable=self.id_timetable).first().close_time
                                 }}


class Translate(db.Model):
    id_place = db.Column(db.Integer, db.ForeignKey('place.id_place'), primary_key=True)
    language = db.Column(db.Integer, db.ForeignKey('language.id_language'), primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.String(500))
    address = db.Column(db.String(100))

    def __repr__(self):
        return '<Translate %r>' % self.name + self.language.value

    def to_json(self):
        return {Language.query.filter_by(id_language=self.language).first().name:
                    {'name': self.name, 'description': self.description, 'address': self.address}}


class Language(db.Model):
    id_language = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10))
    name = db.Column(db.String(40), unique=True)
    region = db.Column(db.String(40))

    def __repr__(self):
        return '<Language %r' % self.name


class Service(db.Model):
    id_service = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    name = db.Column(db.String(50))
    place = db.relationship('ServicePlace', backref='places', lazy='dynamic')

    def __repr__(self):
        return '<Comfort %r>' % self.type

    def to_json(self):
        return {'service': self.type}


class ServicePlace(db.Model):
    id_place = db.Column(db.Integer, db.ForeignKey('place.id_place'), primary_key=True)
    id_comfort = db.Column(db.Integer, db.ForeignKey('service.id_service', primary_key=True))

    def __repr__(self):
        return '<ComfortPlace %r>' % self.id_place + ' ' + self.id_comfort


class PaymentMethod(db.Model):
    id_payment_method = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    name = db.Column(db.String(50))
    place = db.relationship('PaymentMethodPlace', backref='places', lazy='dynamic')

    def __repr__(self):
        return '<PaymentMethod %r>' % self.type

    def to_json(self):
        return {'paymentmethod': self.type}


class PaymentMethodPlace(db.Model):
    id_place = db.Column(db.Integer, db.ForeignKey('place.id_place'), primary_key=True)
    id_payment_method = db.Column(db.Integer, db.ForeignKey('payment_method.id_payment_method'), primary_key=True)

    def __repr__(self):
        return '<PaymentMethodPlace %r>' % self.id_place + ' ' + self.id_payment_method


class Photo(db.Model):
    id_photo = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256))
    id_place = db.Column(db.Integer, db.ForeignKey('place.id_place'))

    def __repr__(self):
        return '<Photo %r>' % self.url

    def to_json(self):
        return {'url': self.url}
