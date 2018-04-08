from app.places import bp
from app.models import Place, User, TimeTable, Comfort, Finance
import os
from app.places.forms import PlaceForm
from config import basedir
from flask_login import current_user, login_required
from app import db
from flask import render_template, redirect, url_for
from werkzeug.utils import secure_filename
from time import time


@bp.route('/newplace', methods=['GET', 'POST'])
@login_required
def new_place():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    form = PlaceForm()
    user = User.query.filter_by(login=current_user.login).first()
    if form.validate_on_submit():
        f = form.upload.data
        filename = secure_filename(str(time()) + '.jpg')
        f.save(os.path.join(
            basedir + '\\picture',  filename
        ))
        place = Place(photo_name=filename, name=form.cName.data, name_l=form.lName.data,
                      email=form.email.data, website=form.website.data, address=form.cAddress.data,
                      address_l=form.lAddress.data, country=form.country.data, city=form.city.data,
                      type_establ=form.type_establ.data, location=form.location.data, id_user=user.id)
        db.session.add(place)
        db.session.commit()
        if form.oMon.data and form.cMon.data:
            time_m = TimeTable(day=1, open_time=form.oMon.data, close_time=form.cMon.data,
                               id_place=place.id)
            db.session.add(time_m)
        if form.oTue.data and form.cTue.data:
            time_t = TimeTable(day=2, open_time=form.oTue.data, close_time=form.cTue.data,
                               id_place=place.id)
            db.session.add(time_t)
        if form.oWed.data and form.cWed.data:
            time_w = TimeTable(day=3, open_time=form.oWed.data, close_time=form.cWed.data,
                               id_place=place.id)
            db.session.add(time_w)
        if form.oThu.data and form.cThu.data:
            time_th = TimeTable(day=4, open_time=form.oThu.data, close_time=form.cThu.data,
                                id_place=place.id)
            db.session.add(time_th)
        if form.oFri.data and form.cFri.data:
            time_fr = TimeTable(day=5, open_time=form.oFri.data, close_time=form.cFri.data,
                                id_place=place.id)
            db.session.add(time_fr)
        if form.oSun.data and form.cSun.data:
            time_s = TimeTable(day=6, open_time=form.oSun.data, close_time=form.cSun.data,
                               id_place=place.id)
            db.session.add(time_s)
        if form.oSat.data and form.cSat.data:
            time_st = TimeTable(day=7, open_time=form.oSat.data, close_time=form.cSat.data,
                                id_place=place.id)
            db.session.add(time_st)

        comfort = Comfort()
        if form.tourism.data or form.visitors.data or form.services.data or form.sections_inclusiveness.data:
            if form.tourism.data:
                if "Socket" in form.tourism.data:
                    comfort.socket = True
                if "WelcomeTourism" in form.tourism.data:
                    comfort.welcome = True
            if form.visitors.data:
                if "ForChildren" in form.visitors.data:
                    comfort.forChildren = True
                if "AnimalAccess" in form.visitors.data:
                    comfort.animal = True
            if form.services.data:
                if "RentBikes" in form.services.data:
                    comfort.rentBikes = True
                if "Polygraph" in form.services.data:
                    comfort.polygraph = True
            if form.sections_inclusiveness.data:
                if "Ramp" in form.sections_inclusiveness.data:
                    comfort.ramp = True
                if "SpecialToilet" in form.sections_inclusiveness.data:
                    comfort.specialToilet = True
                if "SpecialService" in form.sections_inclusiveness.data:
                    comfort.specialService = True
            comfort.id_place = place.id
            db.session.add(comfort)

        finance = Finance()
        if form.way_to_pay.data:
            if "DebitCard" in form.way_to_pay.data:
                finance.debit_card = True
            if "CreditCard" in form.way_to_pay.data:
                finance.credit_card = True
            if "ElectronicPayment" in form.way_to_pay.data:
                finance.electronic_payment = True
        finance.average_check = form.average_check.data
        db.session.add(finance)
        db.session.commit()

    return render_template('place/addNewPlace.html', form=form)