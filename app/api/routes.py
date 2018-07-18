from app.api import api
from flask_restful import Resource, reqparse
from app.models import User as User_db
from app.models import Category as Category_db
from app.models import Place as Place_db
from app.models import CategoryPlace as CategoryPlace_db
from app import db


class UserAdd(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id_user', type=int, help='Error')
    parser.add_argument('login', help='Error')
    parser.add_argument('name', help='Error')
    parser.add_argument('surname', help='Error')
    parser.add_argument('latitude', type=float, help='Error')
    parser.add_argument('longitude', type=float, help='Error')

    def post(self):
        data = self.parser.parse_args()
        user = User_db.query.filter_by(id_user=data['id_user']).first()
        try:
            if user is None:
                user = User_db(id_user=data['id_user'], login=data['login'], name=data['name'], surname=data['surname'],
                               latitude=data['latitude'], longitude=data['longitude'])
                db.session.add(user)
                db.session.commit()
                return {'message': {'add_user': 'Create!'}}, 200
            return {'message': {'add_user': 'User exists'}}, 201
        except Exception as e:
            return {'message': e}, 400


class CategoryApi(Resource):

    def get(self):
        try:
            category = [category.name for category in
                         Category_db.query.order_by(Category_db.name).filter_by(id_supergroup='').all()]
            return {'message': category}, 200
        except Exception as e:
            return {'message': e}, 400


class SubCategory(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('category')

    def get(self):
        data = self.parser.parse_args()
        try:
            category = [category.name for category in Category_db.query.filter_by(
                id_supergroup=Category_db.query.filter_by(name=data['category']).first().id_category).all()]
            return {'message': category}, 200
        except Exception as e:
            return {'message': e}, 400


class PlaceApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('category')
    parser.add_argument('num')

    def get(self):
        data = self.parser.parse_args()
        try:
            place_id = [place.id_place for place in CategoryPlace_db.query.filter_by(id_category=
                                                                                    Category_db.query.filter_by(
                                                                                    name=data['category']).first().id_category).all()]
            for id in place_id:
                places = [place.get_information() for place in Place_db.query.filter_by(
                    id_place=id).all()]
            return {'message': places}
        except Exception as e:
            return {'message': e}, 400


class OnePlace(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id_place')

    def get(self):
        data = self.parser.parse_args()
        try:

            place = Place_db.query.filter_by(id_place=data['id_place']).first()
            places = place.get_information()
            return {'message': places}
        except Exception as e:
            return {'message': e}, 400


api.add_resource(CategoryApi, '/api/category')
api.add_resource(SubCategory, '/api/subcategory')
api.add_resource(PlaceApi, '/api/place')
api.add_resource(OnePlace, '/api/place_id')