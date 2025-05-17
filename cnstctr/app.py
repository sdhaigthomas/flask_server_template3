from flask import Flask, render_template
import sys
from os import path

########## bluepint imports \/ imports /\
parent_dir = path.dirname(
    path.dirname(path.abspath(__file__))
    )

sys.path.append(
    path.join(parent_dir, 'blprnts')
    )

from nonauth import nonauth

##########
app = Flask(__name__, template_folder="../tmplts")

@app.route('/')
def index():
    return render_template("index.html")

app.register_blueprint(nonauth)

if __name__ == '__main__': 
    app.run()