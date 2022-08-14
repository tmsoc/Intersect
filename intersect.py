from app import create_app, db
from app.models import User
from app.models import Room
from app.models import Remote_Roku

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Room': Room, 'Roku': Remote_Roku}
