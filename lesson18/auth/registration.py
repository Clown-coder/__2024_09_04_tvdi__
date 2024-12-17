from . import auth
from flask import render_template,request,url_for,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,validators
from wtforms.validators import DataRequired,Length
from werkzeug.security import generate_password_hash

class RegistrationForm(FlaskForm):
    username = StringField('使用者名稱',[
        validators.Length(min=8,max=25),
        validators.InputRequired("使用者名稱不為空")
    ])
    email = EmailField('信箱',[
        validators.Length(min=3,max=35),
        validators.InputRequired("信箱不為空")
    ])
    password = PasswordField('新密碼',[
        validators.Length(min=8,max=30),
        validators.DataRequired("密碼不為空"),
        validators.EqualTo('confirm_password',message='密碼不相同，請重新輸入')
    ])
    confirm_password = PasswordField('再次輸入密碼',[
        validators.InputRequired("再次輸入密碼"),

    ])


@auth.route('/regist',methods=['GET','POST'])
def regist():
    form =RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        name= form.username.data
        email = form.email.data
        password = form.password.data
        password_hash= generate_password_hash(password=password,method='pbkdf2:sha256:600000',salt_length=8)
        print(password_hash)
        return redirect(url_for('auth.success'))
    return render_template('/auth/registration.j2',form=form)