from . import auth
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.validators import DataRequired,Length

class MyForm(FlaskForm):
    email_field = fields.EmailField("Email address",validators=[DataRequired("必須要有資料")])
    password_field = fields.PasswordField("請輸入密碼",validators=[DataRequired("必須要有資料"),Length(5,10)])
    e_paper_field = fields.BooleanField("訂閱電子報")
    submit_field = fields.SubmitField("確認送出")

@auth.route("/login",methods=['POST','GET'])
def login():
    myForm = MyForm()
    return render_template('auth/login.j2',myForm = myForm)