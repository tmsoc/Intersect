from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Tony"}
    return render_template('index.html', title="home", user=user)


@app.route('/welcome')
def welcome():
    return render_template('welcome.html', title="Welcome")