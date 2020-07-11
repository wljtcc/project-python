from flask import render_template
from app import app


@app.route('/', defaults={'user':''})
def default(user):
    return render_template('index.html')
