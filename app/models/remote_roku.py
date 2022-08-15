from app import db
from roku import Roku


class Remote_Roku(db.Model, Roku):
    __tablename__ = 'roku'
    
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(17), nullable=False)
    name = db.Column(db.String(150))
    dev_type = db.Column(db.String(25), default='roku')

    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))

    roku = None
    
    def __init__(self, **kwargs):
        super(Remote_Roku, self).__init__(**kwargs)
        self.roku = Roku(kwargs['ip'])
        self.query_device_name()


    @db.reconstructor
    def init_on_load(self):
        self.roku = Roku(self.ip)


    def __repr__(self) -> str:
        if self.room_id == None:
            return f"<ID: {self.id} IP: {self.ip} Name: {self.name} Room ID: None>"
        else:
            return f"<ID: {self.id} IP: {self.ip} Name: {self.name} Room ID: {self.room.id}>"


    def query_device_name(self):
        self.name = self.roku.device_info.user_device_name
