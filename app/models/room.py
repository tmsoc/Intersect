from app import db

class Room(db.Model):
    __tablename__ = 'room'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=True, nullable=False)
    url_path = db.Column(db.String(150), unique=True)

    # Attached Devices
    rokus = db.relationship('Remote_Roku', backref='room', lazy=True)
    ir_dev = db.relationship('Remote_Ir', backref='room', lazy=True)
    
    
    def __init__(self, **kwargs):
        super(Room, self).__init__(**kwargs)
        self.name = kwargs['name'].strip()
        self.url_path = self.name.lower().replace(' ', '_')

    def __repr__(self) -> str:
        return f'<ID: {self.id} name: {self.name} url path: {self.url_path}>'

    def add_roku(self, roku):
        self.rokus.append(roku)

    def remove_roku(self, roku):
        if roku in self.rokus:
            self.rokus.remove(roku)

    def add_ir_dev(self, ir_dev):
        self.ir_dev.append(ir_dev)

    def remove_ir_dev(self, ir_dev):
        if ir_dev in self.ir_dev:
            self.ir_dev.remove(ir_dev)