from app.places import bp
from app import places
from app import db
from flask import render_template, redirect, url_for
from cloudinary.uploader import upload
from app.models import Category, CategoryPlace, Place, CurrencyType, Translate, Language, Photo
from db_enum import DayEnum
from cloudinary.utils import cloudinary_url


@bp.route('/newplace', methods=['GET', 'POST'])
def new_place():
    form = places.forms.PlaceForm()
    if form.validate_on_submit():
        f = form.upload.data
        upload_result = upload(f, width="600", height="300")
        place = Place(name=form.cName.data, description=form.description.data,
                      email=form.email.data, website=form.website.data, address=form.cAddress.data,
                      country=form.country.data, city=form.city.data,
                      rating=0, number_of_reviews=0)
        photo = Photo(id_place=place.id_place, url=upload_result['url'])
        place.latitude = form.location.data.split(';')[0].rstrip()
        place.longitude = form.location.data.split(';')[1].rstrip()
        db.session.add(place)
        photo = Photo(id_place=place.id_place, url=upload_result['url'])
        db.session.add(photo)
        db.session.commit()
        place_category = CategoryPlace(id_place=place.id_place, id_category=Category.query.filter_by(
            type=form.type_establ.data).first().id_category)
        db.session.add(place_category)
        db.session.commit()
        if form.oMon.data and form.cMon.data:
            place.add_timetable_day(str(form.oMon.data), str(form.cMon.data), DayEnum.Monday)
        if form.oTue.data and form.cTue.data:
            place.add_timetable_day(str(form.oTue.data), str(form.cTue.data), DayEnum.Tuesday)
        if form.oWed.data and form.cWed.data:
            place.add_timetable_day(str(form.oWed.data), str(form.cWed.data), DayEnum.Wednesday)
        if form.oThu.data and form.cThu.data:
            place.add_timetable_day(str(form.oThu.data), str(form.cThu.data), DayEnum.Thursday)
        if form.oFri.data and form.cFri.data:
            place.add_timetable_day(str(form.oFri.data), str(form.cFri.data), DayEnum.Friday)
        if form.oSun.data and form.cSun.data:
            place.add_timetable_day(str(form.oSun.data), str(form.cSun.data), DayEnum.Sunday)
        if form.oSat.data and form.cSat.data:
            place.add_timetable_day(str(form.oSat.data), str(form.cSat.data), DayEnum.Saturday)
        if form.services.data:
            for service in form.services.data:
                place.add_service(service)
        place.average_check = form.average_check.data
        if form.way_to_pay.data:
            for payment_method in form.way_to_pay.data:
                place.add_payment_method(payment_method)
        place.id_currency = CurrencyType.query.filter_by(type=form.currency.data).first().id_currency
        url_for('places.add_description', lan="ENG", place=place.id_place)
    else:
        print(form.errors)
    return render_template('place/addNewPlace.html', form=form)


@bp.route('/add_description&lan=<lan>&place=<place>', methods=['GET', 'POST'])
def add_description(lan, place):
    form = places.forms.DescriptionForm(lan, place)
    print('hi')
    #if form.validate_on_submit():
    print('hi')
    translate = Translate.query.filter_by(id_place=int(place),
                          language=Language.query.filter_by(type=lan).first().id_language).first()
    if translate is None:
        translate = Translate(id_place=int(place),
                          language=Language.query.filter_by(type=lan).first().id_language,
                          description=form.description.data, name=form.name.data, address=form.address.data)
        db.session.add(translate)
    else:
        translate.name = form.name.data
        translate.description = form.description.data
        translate.address = form.address.data
    db.session.commit()
    #else:
    print(form.errors)
    return render_template('place/addPhrases.html', form=form, place=place)


