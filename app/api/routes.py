from app.api import api
from flask_restful import Resource
from requests import get


class MainWindow(Resource):
    def get(self):
        try:
            result = get('https://api.apixu.com/v1/forecast.json?key=0cf0ec96a5eb4feb87b115613180905&q=Kharkiv',
                         data={}).json()
            weather = result['forecast']['forecastday'][0]['day']['avgtemp_c']
            result = get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json&valcode=EUR',
                         data={}).json()
            val = result[0]['rate']
            return {'message': {'weather': weather, 'currency': val}}, 200
        except Exception as e:
            return {'message': e}, 400


api.add_resource(MainWindow, '/api/data_main')
