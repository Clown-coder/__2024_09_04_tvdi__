from . import auth
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField
from wtforms.validators import DataRequired,Length


class RegistrationForm(FlaskForm):
    username = StringField('Username')
    email = EmailField('E-mail')
    password = PasswordField('New Password')
    confirm_password = PasswordField('Confirm Password')


@auth.route('/regist')
def regist():
    form =RegistrationForm()
    return render_template('/auth/registration.j2',form=form)