from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import database_initialize
import os


app = Flask(__name__)
db = SQLAlchemy() 

# database_initialize(app=app, db=db)

