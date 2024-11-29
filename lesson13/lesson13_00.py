from flask import Flask,render_template
'''
flask 就是一個支援 wsgi的應用程式
真正支援wsgi的程式是 Gunicorn

執行時，在終端機輸入
flask --app 檔案名稱 run --debug

'''
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.j2')

