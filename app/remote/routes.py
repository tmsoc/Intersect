from flask import render_template, redirect, url_for
from flask_login import login_required
from app.remote import bp

#temp development imports
from app.models import dev_rooms, dev_devices


@bp.route('/remote')
@login_required
def remote_home():
    rooms = dev_rooms
    if len(rooms) > 0:
        return redirect(url_for('remote.remote', room=rooms[0]['url_path']))
    return render_template('remote/remote_default.html', title='Remote')


@bp.route('/remote/<room>')
@login_required
def remote(room):
    rooms = dev_rooms
    current_room = next((r for r in rooms if r['url_path'] == room), None)
    devices = dev_devices
    return render_template('remote/remote.html', room=current_room, rooms=rooms, devices=devices)
