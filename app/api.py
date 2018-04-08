from flask import jsonify
from flask import request, abort
import jwt
from validate_email import validate_email
from app.models import User
from app.models import Client
from app import app, db


@app.route('/api/auth', methods=['POST'])
def api_l():
    if not request.json or not ('auth' in request.json and 'password' in request.json):
        abort(400)
    user = User.query.filter_by(login=request.json['auth']).first()
    if user is None or not user.check_password(request.json['password']):
        return jsonify({'completion': False, 'description': 'Invalid username or password'})
    user.active = True
    token = jwt.encode({'token_login': request.json['auth']},
            app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')
    client = Client(token=token, id_user=user.id)
    db.session.add(client)
    db.session.commit()
    return jsonify({'completion': True, 'token': token})


@app.route('/api/registration', methods=['POST'])
def api_registration():
    if not request.json or not ('auth' in request.json and 'password' in request.json and 'email' in request.json):
        abort(400)
    if not (User.query.filter_by(login=request.json['auth']).first() is None):
        return jsonify({'completion': False, 'description': 'This auth is already used'})
    if not (validate_email(request.json['email'])):
        return jsonify({'completion': False, 'description': 'Invalid e-mail'})
    if not (User.query.filter_by(email=request.json['email']).first() is None):
        return jsonify({'completion': False, 'description': 'This email is already used'})
    user = User(login=request.json['auth'], email=request.json['email'], active=False, role_id=2)
    user.set_password(password=request.json['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'completion': True})


