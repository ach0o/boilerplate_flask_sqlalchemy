import os

from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from . import commands, db, routes


def create_app(config=None):
    # Initialize flask app
    app = Flask(__name__)
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    base_dir = os.path.join(curr_dir, os.pardir)

    # Set database configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL',
        'sqlite:///../db.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.json'):
            app.config.from_json(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    # Register app to other modules
    db.init_app(app)
    routes.register_blueprint(app)

    # Add Commands
    app.cli.command()(commands.create_db)
    app.cli.command()(commands.drop_db)

    return app
