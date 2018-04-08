from app.main import bp
from flask import render_template


@bp.route('/')
def start():
    return render_template('home/app.html')

