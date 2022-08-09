from flask import Blueprint

bp = Blueprint('remote', __name__)

from app.remote import routes