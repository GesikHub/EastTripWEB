from flask import Blueprint
from flask_restful import Api

bp = Blueprint('api_bp', __name__)
api = Api(bp)


from app.api_bp import routes