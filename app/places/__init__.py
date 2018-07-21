from flask import Blueprint

bp = Blueprint('places', __name__)

from app.places import forms, routes
