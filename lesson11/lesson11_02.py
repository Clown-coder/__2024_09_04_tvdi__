from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''
    <!doctype html>
    <html>
    <head>
    <meta charset="utf-8">
    <title>測試集</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./normalize.css">
    <link href="style.css" rel="stylesheet" type="text/css">
    </head>

    <body>
    <div class="header">
    <h1>X-focus</h1>
    <ul>
        <li><a href="#">產品</a></li>
        <li><a href="#">熱門活動</a></li>
        <li><a href="#">商務行銷</a></li>
        <li><a href="#">服務與社群</a></li>
        <li><a href="#">商店</a></li>
        </ul>
        </div>

        </body>
        </html>


    '''

@app.route("/name")
def who():
    return '''
        <h1>NAME</h1>
        <h2>NAM</h2>
        <h3>NA</h3>
        <h4>N</h4>

    '''