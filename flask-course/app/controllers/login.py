from flask import render_template
from app import app

from app.models.forms import LoginForm


@app.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template('login.html',
                            form_login=form)
