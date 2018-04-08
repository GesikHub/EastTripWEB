from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, SubmitField, SelectMultipleField, widgets
from wtforms_components import TimeField
from flask_uploads import UploadSet, IMAGES
from flask_wtf.file import FileField, FileRequired
from app.models import Place
from wtforms.validators import DataRequired, Email

images = UploadSet('images', IMAGES)


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class PlaceForm(FlaskForm):
    upload = FileField("Image", validators=[FileRequired()])
    cName = StringField("Name", validators=[DataRequired()])
    lName = StringField("L_Name")
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[Email()])
    website = StringField("Website")
    cAddress = StringField("Address", validators=[DataRequired()])
    lAddress = StringField("L_Address")
    country = SelectField("Country",
                          choices=[('Ukraine', 'Украина')], default="Ukraine")

    city = SelectField("City",
                       choices=[("Kharkiv", "Харьков"), ("Poltava", "Полтава"), ("Odessa", "Одесса"),
                                ("Kyuiv", "Киев")], default="Kharkiv")
    type_establ = SelectField("Type",
                              choices=[("Cafe", "Кафе"), ("CoffeeShop", "Кофейня"), ("Restaurant", "Ресторан"),
                                       ("Hotel", "Отель")
                                       ], default="Cafe")
    create = SubmitField("Create")

    #   Time table
    open_var = RadioField("Option",
                          choices=[("NoWeekend", "24\\7 без выходных"), ("Weekend", "Не работаю по выходных")
                                   ], default="")
    oSet = TimeField("Open", validators=[DataRequired()], format="%H:%M")
    cSet = TimeField("Close", validators=[DataRequired()], format="%H:%M")
    oMon = TimeField("Open", validators=[DataRequired()], format="%H:%M")
    cMon = TimeField("Close", validators=[DataRequired()], format="%H:%M")
    oTue = TimeField("Open", validators=[DataRequired()], format="%H:%M")
    cTue = TimeField("Close", validators=[DataRequired()], format="%H:%M")
    oWed = TimeField("Open", validators=[DataRequired()], format="%H:%M")
    cWed = TimeField("Close", validators=[DataRequired()], format="%H:%M")
    oThu = TimeField("Open", validators=[DataRequired()], format="%H:%M")
    cThu = TimeField("Close", validators=[DataRequired()], format="%H:%M")
    oFri = TimeField("Open", validators=[DataRequired()], format="%H:%M")
    cFri = TimeField("Close", validators=[DataRequired()], format="%H:%M")
    oSat = TimeField("Open", validators=[DataRequired()], format="%H:%M")
    cSat = TimeField("Close", validators=[DataRequired()], format="%H:%M")
    oSun = TimeField("Open", validators=[DataRequired()], format="%H:%M")
    cSun = TimeField("Close", validators=[DataRequired()], format="%H:%M")

    #   Finance
    way_to_pay = MultiCheckboxField("Way to pay",
                            choices=[("DebitCard", "Дебитная карта"), ("CreditCard", "Кредитная карта"),
                                     ("ElectronicPayment", "Электронная оплата")], default=[])

    average_check = StringField("Average check", validators=[DataRequired()])
    currency = SelectField("Currency",
                           choices=[("UA", "Гривны"), ("USD", "Доллары"), ("EUR", "Евро"), ("RUS", "Рубли")],
                           default="UA")

    #   Comfort
    tourism = MultiCheckboxField("Tourism",
                         choices=[("Socket", "Розетка"), ("WelcomeTourists", "Туристы привествуются")],
                                 default=[''])
    visitors = MultiCheckboxField("Visitors",
                          choices=[("ForChildren", "Для детей"), ("AnimalAccess", "Животные разрешены")],
                                  default=[''])

    services = MultiCheckboxField("Service",
                          choices=[("RentBikes", "Рента велосипедов"), ("Polygraph", "Полигрофия\\Буклеты")],
                                  default=[''])
    sections_inclusiveness = MultiCheckboxField("Section of inclusiveness",
                                        choices=[("Ramp", "Пандус"), ("SpecialToilet", "Специальный туалет"),
                                                 ("SpecialService", "Специальный сервис")],
                                                default=[''])

    location = StringField("Location", validators=[DataRequired()])

    def validate_location(self, location):
        place = Place.query.filter_by(location=location).first()
        if place is not None:
            raise ValueError('Place with it location is already used')


