from . import auth
from flask import session,redirect,url_for,render_template
@auth.route('logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))