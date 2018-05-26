import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    JOBS = [
        {
            'id': 'main_window',
            'func': 'test:job1',
            'trigger': 'interval',
            'seconds': 86400
        }
    ]
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
