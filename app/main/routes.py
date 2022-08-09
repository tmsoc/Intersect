from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required
from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    if current_user.is_anonymous:
        return redirect(url_for('main.welcome'))
    return render_template('main/index.html', title="Home")


@bp.route('/welcome')
def welcome():
    return render_template('main/welcome.html', title="Welcome")

