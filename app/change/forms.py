from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import PasswordField, SubmitField
from app.models import User
from wtforms.validators import DataRequired, EqualTo


class ChangeForm(FlaskForm):
    oldPass = PasswordField('oldPass', validators=[DataRequired()])
    newPass = PasswordField('newPass', validators=[DataRequired()])
    newPassR = PasswordField('newPassR', validators=[DataRequired(), EqualTo('newPass')])
    submit = SubmitField('Изменить пароль')

    def validate_oldPass(self, oldPass):
        user = User.query.filter_by(login=current_user.login).first()
        if not user.check_password(oldPass.data):
           raise ValueError("Invalid password")
