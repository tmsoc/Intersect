from flask import render_template, redirect, url_for, request, jsonify
from flask_login import login_required
from app.remote import bp
from app.models import Room, Roku


@bp.route('/remote')
@login_required
def remote_home():
    rooms = Room.query.all()
    if len(rooms) > 0:
        return redirect(url_for('remote.remote', room=rooms[0].url_path))
    return render_template('remote/remote_default.html', title='Remote')


@bp.route('/remote/<room>')
@login_required
def remote(room):
    rooms = Room.query.all()
    current_room = Room.query.filter_by(url_path=room).first()
    devices = Roku.query.filter_by(room=current_room).all()
    return render_template('remote/remote.html', title='Remote', room=current_room, rooms=rooms, devices=devices)


@bp.route('/remote/transmit', methods=['POST'])
@login_required
def transmit_UR():
    dev_type = request.form['device_type']
    func, dev_id = request.form['function'].split('_')

    if dev_type == 'roku':
        rk = Roku.query.get(dev_id)
        eval(f'rk.roku.{func}()')
    elif dev_type == 'ir':
        print('ir device')
    else:
        print("Error with remote action")
        
    return jsonify({'message': 'transmit complete'})