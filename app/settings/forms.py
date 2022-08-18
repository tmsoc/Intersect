from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import Length, DataRequired, ValidationError
from app.models import Room, Roku, IR


class AddRoomForm(FlaskForm):
    room_name = StringField('Room Name:', validators=[Length(min=1, max=149, message='Data Required')])
    # room_name = StringField('Room Name:')#, validators=[DataRequired()])
    add_room_submit = SubmitField('Add')

    def validate_room_name(self, room_name):
        new_room = Room(name=room_name.data)
        room = Room.query.filter_by(url_path=new_room.url_path).all()
        if len(room) > 0:
            raise ValidationError('That name is already in use.')        


class DeleteRoomForm(FlaskForm):
    delete_rooms_list = SelectField('Rooms:', coerce=int)
    delete_room_submit = SubmitField('Confirm')


class RoomDetailsForm(FlaskForm):
    detail_rooms_list = SelectField('Rooms:')


