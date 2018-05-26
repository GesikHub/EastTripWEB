from app.api import api
from flask_restful import Resource
from app.models import DateMainWindow
import pytz
import datetime


class MainWindow(Resource):
    def get(self):
        try:
            mytz = pytz.timezone('Europe/Kiev')
            date = DateMainWindow.query().first()
            weather = date.weather
            val = date.euro
            time = datetime.datetime.now(mytz).hour + ':' + datetime.datetime.now(mytz).minute
            data = datetime.datetime.now(mytz).day
            return {'message': {'weather': weather, 'currency': val, 'time': time, 'data': data}}, 200
        except Exception as e:
            return {'message': e}, 400


api.add_resource(MainWindow, '/api/data_main')
