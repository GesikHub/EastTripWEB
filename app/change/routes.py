from app.change import bp
from app.models import User, Place
from app.change.forms import ChangeForm
from app import db
from flask_login import current_user, login_required
from flask import redirect, url_for, render_template


@bp.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    form = ChangeForm()
    user = User.query.filter_by(login=current_user.login).first()
    if form.validate_on_submit():
        if form.newPass.data == form.newPassR.data:
            user.set_password(form.newPass.data)
            db.session.commit()
    return render_template('change/editPass.html', form=form)


@bp.route('/personal', methods=['GET', 'POST'])
@login_required
def personal():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    user = User.query.filter_by(login=current_user.login).first()
    places = Place.query.filter_by(id_user=user.id)
    return render_template('change/PersonalPage.html', places=places)
