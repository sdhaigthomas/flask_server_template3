from blprntboilerplate import setup
nonauth = setup("nonauth")

@nonauth.route('/nat')
def nonauthtest():
    return render_template
