from flask_apscheduler import APScheduler
from app.models import DateMainWindow
from app import db
from requests import get


def date_main():
    date = DateMainWindow.query().first()
    result = get('https://api.apixu.com/v1/forecast.json?key=0cf0ec96a5eb4feb87b115613180905&q=Kharkiv',
                 data={}).json()
    date.weather = int(result['forecast']['forecastday'][0]['day']['avgtemp_c'])
    result = get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json&valcode=EUR',
                 data={}).json()
    date.euro = int(result[0]['rate'])
    db.session.commit()
