from app import create_app, db
from app.models import User, Room, Roku, IR


app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Room': Room, 'Roku': Roku, 'IR': IR}
