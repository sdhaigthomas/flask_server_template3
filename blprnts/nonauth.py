from blprnts.blprntboilerplate import *
nonauth = setup("nonauth")

@nonauth.route('/')
def index():
    return render_template("index.html")

@nonauth.route('/signin', methods=["POST","GET"])
def signin():
    username = request.form.get("username")
    if username:
        to_flash = username_val(username)
        if to_flash: flash(to_flash)

    return render_template("signin.html")

@nonauth.route('/signup')
def signup():
    return render_template("index.html")
