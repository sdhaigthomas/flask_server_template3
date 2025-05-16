from flask import Blueprint

nonauth = Blueprint('nonauth', __name__)

@nonauth.route('/nat')
def nonauthtest():
    return "This is an example app"
