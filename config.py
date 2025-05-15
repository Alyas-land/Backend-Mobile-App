from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import database_initialize
import os
from flask_cors import CORS



app = Flask(__name__, static_folder='app/static')
CORS(app)
db = SQLAlchemy() 


# database_initialize(app=app, db=db)

