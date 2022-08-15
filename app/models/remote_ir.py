import socket
from app import db

DEVICES = {
    'tv':       b'\x00',
    'receiver': b'\x01'
}

FUNCTIONS = {
    'power':    b'\x00',
    'back':     b'\x01',
    'home':     b'\x02',
    'up':       b'\x03',
    'down':     b'\x04',
    'left':     b'\x05',
    'right':    b'\x06',
    'select':   b'\x07',
    'menu':     b'\x08',
    'vol_up':   b'\x09',
    'vol_down': b'\x0A',
    'ch_up':    b'\x0B',
    'ch_down':  b'\x0C',
    'mute':     b'\x0D',
    'input':    b'\x0E',
    'tv_in':    b'\x0F',
    'dvd_in':   b'\x10',
    'phono_in': b'\x11',
}

HEADER = b'\x01\x02\x04\x08\x10'

REMOTE_MESSAGE_TYPE = b'\x52'
STATUS_MESSAGE_TYPE = b'\x53'
CONFIG_MESSAGE_TYPE = b'\x43'

PORT = 6000

class Remote_Ir(db.Model):
    __tablename__ = 'ir'

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(17), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    dev_type = db.Column(db.String(25), default='tv')

    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))

    def __repr__(self) -> str:
        if self.room_id == None:
            return f'<ID: {self.id} Name: {self.name} Type: {self.dev_type} Room ID: None>'
        else:
            return f'<ID: {self.id} Name: {self.name} Type: {self.dev_type} Room ID: {self.room.id}>'
    
    def ir_command(self, device, function):
        print('function working')
        if device in DEVICES and function in FUNCTIONS:
            print('device & function good')
            print(self.ip)
            print(self.name)
            message = HEADER + REMOTE_MESSAGE_TYPE + DEVICES[device] + FUNCTIONS[function]
            self._send_udp_bytes(message)

    def _send_udp_bytes(self, data):
        open_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        open_socket.sendto(data, (self.ip, PORT))
        open_socket.close()

