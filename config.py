from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import database_initialize
import os
from flask_cors import CORS



app = Flask(__name__, static_url_path='/app/static', static_folder='app/static')

UPLOAD_FOLDER = 'app/static/uploads/profile_images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)
db = SQLAlchemy() 


# database_initialize(app=app, db=db)

