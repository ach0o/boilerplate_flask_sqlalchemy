import os

from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from . import db, routes


# Initialize flask app
app = Flask(__name__)
curr_dir = os.path.abspath(os.path.dirname(__file__))
base_dir = os.path.join(curr_dir, os.pardir)


# Set database configurations
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(base_dir, 'db.sqlite')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Register app to other modules
db.init_app(app)
routes.init_app(app)
