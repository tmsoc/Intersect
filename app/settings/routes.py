from flask import render_template, url_for, flash
from flask_login import login_required
from app import db
from app.settings import bp
from app.settings.forms import AddRoomForm, DeleteRoomForm, RoomDetailsForm
from app.models import Room



# @bp.route('/settings', methods=['GET', 'POST'])
# @login_required
# def settings():
#     return render_template('settings/settings.html', title='Settings')


@bp.route("/settings")
@bp.route("/settings/rooms")
@login_required
def room_setting():
    add_form = AddRoomForm()
    delete_form = DeleteRoomForm()
    details_list = RoomDetailsForm()
    
    room_list = [(r.id, r.name) for r in Room.query.all()]
    details_list.detail_rooms_list.choices = room_list
    delete_form.delete_rooms_list.choices = room_list

    return render_template(
        "settings/room_setting.html",
        title="Room Settings",
        add_form=add_form,
        delete_form=delete_form,
        details_list=details_list
    )


@bp.route('/settings/room/add_room', methods=['POST'])
@login_required
def add_room():
    add_form = AddRoomForm()
    delete_form = DeleteRoomForm()
    details_list = RoomDetailsForm()
    
    if add_form.validate_on_submit():
        rm = Room(name=add_form.room_name.data)
        db.session.add(rm)
        db.session.commit()
        add_form.room_name.data = ''
        flash(f'{rm.name} added to database')

    room_list = [(r.id, r.name) for r in Room.query.all()]
    details_list.detail_rooms_list.choices = room_list
    delete_form.delete_rooms_list.choices = room_list

    return render_template(
        "settings/room_setting.html",
        title="Room Settings",
        add_form=add_form,
        delete_form=delete_form,
        details_list=details_list
    )


@bp.route('/settings/room/delete_room', methods=['POST'])
@login_required
def delete_room():
    add_form = AddRoomForm()
    delete_form = DeleteRoomForm()
    details_list = RoomDetailsForm()
    
    room_list = [(r.id, r.name) for r in Room.query.all()]
    details_list.detail_rooms_list.choices = room_list
    delete_form.delete_rooms_list.choices = room_list
    
    if delete_form.validate_on_submit():
        print(delete_form.delete_rooms_list.data)
        rm = Room.query.get(delete_form.delete_rooms_list.data)
        db.session.delete(rm)
        db.session.commit()

    room_list = [(r.id, r.name) for r in Room.query.all()]
    details_list.detail_rooms_list.choices = room_list
    delete_form.delete_rooms_list.choices = room_list

    return render_template(
        "settings/room_setting.html",
        title="Room Settings",
        add_form=add_form,
        delete_form=delete_form,
        details_list=details_list
    )