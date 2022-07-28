from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse
from app import app
from app.forms import LoginForm
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    if current_user.is_anonymous:
        return redirect(url_for('welcome'))
    return render_template('index.html', title="Home")


@app.route('/welcome')
def welcome():
    return render_template('welcome.html', title="Welcome")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('welcome'))


@app.route('/settings')
@login_required
def settings():
    return render_template('settings.html', title='Settings')


@app.route('/remote')
@login_required
def remote_home():
    # rooms = []
    rooms = [
        {'id': 1, 'name': 'Living Room', 'url_path': 'living_room'},
        {'id': 2, 'name': 'Office', 'url_path': 'office'},
        {'id': 3, 'name': 'Bedroom', 'url_path': 'bedroom'}
    ]
    if len(rooms) > 0:
        return redirect(url_for('remote', room=rooms[0]['url_path']))
    return render_template('remote_default.html', title='Remote')


@app.route('/remote/<room>')
@login_required
def remote(room):
    rooms = [
        {'id': 1, 'name': 'Living Room', 'url_path': 'living_room'},
        {'id': 2, 'name': 'Office', 'url_path': 'office'},
        {'id': 3, 'name': 'Bead Room', 'url_path': 'bead_room'}
    ]
    current_room = next((r for r in rooms if r['url_path'] == room), None)
    devices = [
        {'id': 1, 'name': 'roku', 'ip': '192.168.1.1', 'type': "roku"},
        {'id': 2, 'name': 'tv', 'ip': '192.168.1.1', 'type': "tv"},
        {'id': 3, 'name': 'receiver', 'ip': '192.168.1.1', 'type': "receiver"}
    ]
    return render_template('remote.html', room=current_room, rooms=rooms, devices=devices)
    