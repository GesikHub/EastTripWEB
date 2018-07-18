from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, SelectMultipleField, widgets, TextAreaField
from wtforms_components import TimeField
from flask_uploads import UploadSet, IMAGES
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, Email
from app.models import Category, Service, CurrencyType, PaymentMethod, Language, Translate
from app import db

images = UploadSet('images', IMAGES)
category_list = [(category.type, category.name) for category
                 in Category.query.filter_by().all() if category.id_supergroup is not '']
service_list = [(service.type, service.name) for service in Service.query.filter_by().all()]
currency_list = [(currency.type, currency.name) for currency in CurrencyType.query.filter_by().all()]
payment_list = [(payment.type, payment.name) for payment in PaymentMethod.query.filter_by().all()]


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class PlaceForm(FlaskForm):
    upload = FileField("Image", validators=[FileRequired()])
    cName = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[Email()])
    website = StringField("Website")
    cAddress = StringField("Address", validators=[DataRequired()])
    country = SelectField("Country",
                          choices=[('Ukraine', 'Украина')], default="Ukraine")

    city = SelectField("City",
                       choices=[("Kharkiv", "Харьков")], default="Kharkiv")
    try:
        type_establ = SelectField("Type", choices=category_list, default=category_list[0][0])
    except IndexError:
        type_establ = SelectField("Type", choices=[], default=[])
    description = TextAreaField("Description", validators=[DataRequired()])
    create = SubmitField("Create")

    #   Time table

    oMon = TimeField("Open", format="%H:%M")
    cMon = TimeField("Close", format="%H:%M")
    oTue = TimeField("Open", format="%H:%M")
    cTue = TimeField("Close", format="%H:%M")
    oWed = TimeField("Open", format="%H:%M")
    cWed = TimeField("Close", format="%H:%M")
    oThu = TimeField("Open", format="%H:%M")
    cThu = TimeField("Close", format="%H:%M")
    oFri = TimeField("Open", format="%H:%M")
    cFri = TimeField("Close", format="%H:%M")
    oSat = TimeField("Open", format="%H:%M")
    cSat = TimeField("Close", format="%H:%M")
    oSun = TimeField("Open",  format="%H:%M")
    cSun = TimeField("Close", format="%H:%M")

    #   Finance
    try:
        way_to_pay = MultiCheckboxField("Way to pay",
                                    choices=payment_list, default=[])
    except IndexError as e:
        currency = SelectField("Way to pay", choices=[], default=[])

    average_check = StringField("Average check", validators=[DataRequired()])
    try:
        currency = SelectField("Currency", choices=currency_list, default=currency_list[0][0])
    except IndexError as e:
        currency = SelectField("Currency", choices=[], default='')

    #   Comfort
    '''tourism = MultiCheckboxField("Tourism",
                                 choices=[("Socket", "Розетка"), ("WelcomeTourists", "Туристы привествуются")],
                                 default=[''])
    visitors = MultiCheckboxField("Visitors",
                                  choices=[("ForChildren", "Для детей"), ("AnimalAccess", "Животные разрешены")],
                                  default=[''])'''
    try:
        services = MultiCheckboxField("Service", choices=service_list, default=[''])
    except IndexError as e:
        services = MultiCheckboxField('Service', choices=[], default=[''])
    '''sections_inclusiveness = MultiCheckboxField("Section of inclusiveness",
                                                choices=[("Ramp", "Пандус"), ("SpecialToilet", "Специальный туалет"),
                                                         ("SpecialService", "Специальный сервис")],
                                                default=[''])'''

    location = StringField("Location", validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)
        category_list = [(category.type, category.name) for category
                         in Category.query.filter_by().all() if category.id_supergroup is not '']
        service_list = [(service.type, service.name) for service in Service.query.filter_by().all()]
        currency_list = [(currency.type, currency.name) for currency in CurrencyType.query.filter_by().all()]
        payment_list = [(payment.type, payment.name) for payment in PaymentMethod.query.filter_by().all()]
        try:
            self.services.choices = service_list
            self.services.default = ['']
        except IndexError as e:
            self.services.choices = []
            self.services.default = ['']
        try:
            self.currency.choices = currency_list
            self.currency.default = currency_list[0][0]
        except IndexError as e:
            self.currency.choices = []
            self.currency.default = ''
        try:
            self.type_establ.choices = category_list
            self.type_establ.default = category_list[0][0]
        except IndexError:
            self.type_establ.choices = []
            self.type_establ.default = []
        try:
            self.way_to_pay.choices = payment_list
            self.way_to_pay.default = []
        except IndexError as e:
            self.way_to_pay.choices = []
            self.way_to_pay.default = []


class DescriptionForm(FlaskForm):
    languages = SelectField('Language', default='RUS')
    description = TextAreaField("Description", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    create = SubmitField("Сохранить")

    def __init__(self, len, id_place, *args, **kwargs):
        super(DescriptionForm, self).__init__(*args, **kwargs)
        try:
            self.languages.choices = [(language.type, language.name) for language in Language.query.filter_by().all() if
                                      language.type != "RUS"]
            for language in self.languages.choices:
                if language[0] == len:
                    self.languages.choices[self.languages.choices.index(language)], self.languages.choices[0] = self.languages.choices[0], self.languages.choices[self.languages.choices.index(language)]
                    self.languages.default = language[0]
        except IndexError:
            self.languages.choices = []
            self.languages.default = []
        translate = Translate.query.filter_by(id_place=id_place,
                                              language=Language.query.filter_by(type=len).first().id_language).first()
        if translate is not None:
            self.description.type = translate.description
            self.address.type = translate.address
            self.name.type = translate.name
