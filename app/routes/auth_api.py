from flask import jsonify, request
from flask.views import MethodView
from werkzeug.utils import secure_filename
from app.model.models import User
from config import db
import os
from config import app

class RegisterAPI(MethodView):
    def post(self):
    
        name = request.form.get('name')
        phone_number = request.form.get('phone_number')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        if 'profile_image' not in request.files:
            return jsonify({
                'error': 'No profile image uploaded'
            }), 400
        
        file = request.files['profile_image']

        if file.name == '':
            return jsonify({
                'error': 'No selected file'
            }), 400
        
        user_folder = os.path.join(app.config['UPLOAD_FOLDER'], username)
        os.makedirs(user_folder, exist_ok=True)
        
        filename = secure_filename(file.filename)
        print(filename)
        save_path = os.path.join(user_folder, filename)
        print(save_path)
        file.save(save_path)


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
            email = email,
            username = username,
            password = password,
            img_path = save_path
            #add lat login
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify(
            {
                'msg' : 'Your acoount successfully created.',
                'userId': new_user.id
            }
        )


     



class LoginAPI(MethodView):
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