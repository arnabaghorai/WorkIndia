from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import uuid
import hashlib 
import datetime
from functools import wraps
import os
from config import MYSQL_USER ,MYSQL_PASS


# FLASK APP INIT
app = Flask(__name__)
app.config["SECRET_KEY"] = 'shushsecret'

# DATABASE INIT
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@localhost/api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

ma = Marshmallow(app)


# IMPORT views/routes
from .routes import api
app.register_blueprint(api)
