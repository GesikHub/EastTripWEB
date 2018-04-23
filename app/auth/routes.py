from app import db
from app.auth import bp
from flask import render_template, redirect, url_for, flash, request
from app.auth.forms import LoginForm, RegistrationForm
from app.models import User
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.start'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return render_template('login/login_error.html', form=form)
        login_user(user, remember=form.remember_me.data)
        user.active = True
        db.session.commit()
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.start')
        return redirect(next_page)
    return render_template('login/login.html', form=form)


@bp.route('/logout')
def logout():
    if current_user.is_authenticated:
        user = User.query.filter_by(login=current_user.login).first()
        user.active = False
        db.session.commit()
        logout_user()
        return redirect(url_for('main.start'))
    else:
        return redirect(url_for('auth.login'))


@bp.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('main.start'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(login=form.username.data, email=form.email.data, active=False, role_id=2)
        user.set_password(password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('login/register.html', form=form)


