from app import db

class Room(db.Model):
    __tablename__ = 'room'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=True, nullable=False)
    url_path = db.Column(db.String(150), unique=True)

    # Attached Devices
    rokus = db.relationship('Remote_Roku', backref='room', lazy=True)
    
    
    def __init__(self, **kwargs):
        super(Room, self).__init__(**kwargs)
        self.name = kwargs['name'].strip()
        self.url_path = self.name.lower().replace(' ', '_')

    def __repr__(self) -> str:
        return f'id: {self.id}\nname: {self.name}\nurl_path: {self.url_path}'

