from . import auth


@auth.route('/success')
def success():
    return "<h1>789789789789<h1>"