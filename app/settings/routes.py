from flask import render_template, url_for, flash, request, jsonify, redirect
from flask_login import login_required
from app import db
from app.settings import bp
from app.settings.forms import AddRoomForm, DeleteRoomForm, RoomDetailsForm, \
    AddRokuForm, DeleteRokuForm, RokuAssingmentForm
from app.models import Room, Roku, IR



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


@bp.route('/settings/rooms/ar', methods=['POST'])
@login_required
def add_room():
    add_form = AddRoomForm()
    delete_form = DeleteRoomForm()
    details_list = RoomDetailsForm()
    
    if add_form.validate_on_submit():
        rm = Room(name=add_form.room_name.data)
        db.session.add(rm)
        db.session.commit()
        flash(f'{rm.name} added to database')

    add_form.room_name.data = ""
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


@bp.route('/settings/rooms/dr', methods=['POST'])
@login_required
def delete_room():
    add_form = AddRoomForm()
    delete_form = DeleteRoomForm()
    details_list = RoomDetailsForm()
    
    room_list = [(r.id, r.name) for r in Room.query.all()]
    details_list.detail_rooms_list.choices = room_list
    delete_form.delete_rooms_list.choices = room_list
    
    if delete_form.validate_on_submit():
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


@bp.route('/settings/rooms/get-devices', methods=['POST'])
@login_required
def query_room_devices():
    rm = Room.query.get(request.form['rm_id'])
    rks = rm.rokus
    irs = rm.ir_dev

    rks_dict = [{'name': r.name, 'ip': r.ip} for r in rks]
    irs_dict = [{'name': ir.name, 'ip': ir.ip} for ir in irs]

    data = {
        'message': 'query complete',
        'rks': rks_dict,
        'irs': irs_dict
    }

    return jsonify(data)


@bp.route('/settings/roku')
@login_required
def roku_setting():
    add_form = AddRokuForm()
    assign_form = RokuAssingmentForm()
    delete_form = DeleteRokuForm()

    assingments = []
    rks = Roku.query.all()
    for rk in rks:
        if rk.room == None:
            assingments.append({'roku': rk.name, 'room': 'Unassigned'})
        else:
            assingments.append({'roku': rk.name, 'room': rk.room.name})

    choices = [(0, 'Roku')] + [(r.id, r.name) for r in Roku.query.all()]
    assign_form.roku_assign_select.choices = choices

    choices = [(0, 'Room Assignment')] + [(r.id, r.name) for r in Room.query.all()]
    assign_form.room_assign_select.choices = choices

    delete_form.delete_roku_list.choices = [(r.id, r.name) for r in Roku.query.all()]

    return render_template(
        'settings/roku_setting.html', 
        title='Roku Settings', 
        add_form=add_form, 
        delete_form=delete_form, 
        assign_form=assign_form,
        assignments=assingments
    )