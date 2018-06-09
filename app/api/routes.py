from app.api import api
from flask_restful import Resource
import pytz
import datetime
from requests import get
from app.models import Route as Route_db, PointName as Point_db, Language, RouteName

week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']


class MainWindow(Resource):
    def get(self):
        try:
            mytz = pytz.timezone('Europe/Kiev')
            result = get('https://api.apixu.com/v1/forecast.json?key=0cf0ec96a5eb4feb87b115613180905&q=Kharkiv',
                         data={}).json()
            weather = result['forecast']['forecastday'][0]['day']['avgtemp_c']
            result = get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json&valcode=EUR',
                         data={}).json()
            val = result[0]['rate']
            time = str(datetime.datetime.now(mytz).hour) + ':' + str(datetime.datetime.now(mytz).minute)
            data = datetime.datetime.now(mytz).day
            return {'message': {'weather': int(weather), 'currency': int(val), 'time': time, 'data': data, 'week_day': week[datetime.datetime.now(mytz).weekday()]}}, 200
        except Exception as e:
            return {'message': e}, 400


class Route(Resource):

    def get(self, language):
        try:
            lan = Language.query.filter_by(type=language).first()
            if lan is None:
                return {'message': []}, 200
            else:
                return {'message': [route.to_json() for route in RouteName.query.filter_by(
                    language=lan.id_language).all()]}, 200
        except Exception as e:
            return {'message': e}, 400


class Point(Resource):

    def get(self, id_route, language):
        try:
            lan = Language.query.filter_by(type=language).first()
            if lan is None:
                return {'message': []}, 200
            return {'message': [point.to_json() for point in Point_db.query.filter_by(id_route=id_route,
                                                                                      language=lan.id_language).all()]}, 200
        except Exception as e:
            return {'message': e}, 400


api.add_resource(MainWindow, '/api/data_main')
api.add_resource(Route, '/api/route/<language>')
api.add_resource(Point, '/api/route_point/<id_point>/<language>')