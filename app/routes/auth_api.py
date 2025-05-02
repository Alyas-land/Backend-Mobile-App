from flask import jsonify, request
from flask.views import MethodView
from app.model.models import User
from config import db

class Register(MethodView):
    def post(self):
        data = request.get_json()

        name = data.get('name')
        phone_number = data.get('phone_number')
        username = data.get('username')
        password = data.get('password')

        check_exist_user = User.query.filter_by(username=username).one_or_none()

        if check_exist_user:
            return jsonify(
                {
                    'msg' : 'User already exist'
                }
            ), 400
        
        new_user = User(
            name = name,
            phone_number = phone_number,
            username = username,
            password = password
            #add lat login
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify(
            {
                'msg' : 'Your acoount successfully created.'
            }
        )


     



class Login(MethodView):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        check_user = User.query.filter_by(username=username).one_or_none()
        
        if not check_user or password != check_user.password:
            return jsonify(
                {
                    'msg': 'Invalid Data'
                }
            ), 400
        
        elif check_user and password == check_user.password:
            return jsonify(
                {'id': check_user.id,}
            ), 200