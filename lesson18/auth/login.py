from . import auth
from flask import render_template,request,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.validators import DataRequired,Length
from datasource import get_password
from werkzeug.security import check_password_hash

class MyForm(FlaskForm):
    email_field = fields.EmailField("Email address",validators=[DataRequired("必須要有資料")])
    password_field = fields.PasswordField("請輸入密碼",validators=[DataRequired("必須要有資料"),Length(5,10)])
    
    submit_field = fields.SubmitField("確認送出")

@auth.route("/login",methods=['POST','GET'])
def login():
    myForm = MyForm()
    if request.method =="POST" and myForm.validate():
        email = myForm.email_field.data
        password = myForm.password_field.data
        try:
            username, password_hash = get_password(email)

            if check_password_hash(password_hash,password):
                session['username'] = username
                return redirect(url_for('index'))
            else:
                myForm.password_field.errors.append("登入失敗")
        except:
            myForm.password_field.errors.append("登入失敗")

    return render_template('auth/login.j2',myForm = myForm)