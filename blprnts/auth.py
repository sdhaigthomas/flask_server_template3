from blprnts.blprntboilerplate import *
auth = setup("auth")

@auth.route('/user') # userarea
def user():
    return render_template("index.html")