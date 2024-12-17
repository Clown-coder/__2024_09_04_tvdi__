from . import auth
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField
from wtforms.validators import DataRequired,Length


class RegistrationForm(FlaskForm):
    username = StringField('使用者名稱')
    email = EmailField('信箱')
    password = PasswordField('新密碼')
    confirm_password = PasswordField('再次輸入密碼')


@auth.route('/regist')
def regist():
    form =RegistrationForm()
    return render_template('/auth/registration.j2',form=form)