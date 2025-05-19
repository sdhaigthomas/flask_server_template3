from flask import Flask, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import sys
from os import path

##########
app = Flask(__name__, template_folder="../tmplts")
app.config['SECRET_KEY'] = 'verysafekey!'
########## outer imports \/ others imports /\
parent_dir = path.dirname(
    path.dirname(path.abspath(__file__))
    )

sys.path.append(parent_dir)

from blprnts.nonauth import nonauth
from blprnts.auth import auth
##########

@app.route('/style.css')
def css():
    resp = make_response(render_template("style.css"))
    resp.headers['Content-type'] = 'text/css'
    return resp

app.register_blueprint(nonauth)
app.register_blueprint(auth)


if __name__ == '__main__': 
    app.run()

    db = SQLAlchemy()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../db/project.db"
    db.init_app(app)
    with app.app_context():
        db.create_all()

    from mdls.user import user