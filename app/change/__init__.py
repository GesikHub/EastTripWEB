from flask import Blueprint

bp = Blueprint('change', __name__)

from app.places import routes