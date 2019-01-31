from flask import Blueprint

bp_api = Blueprint('api', __name__)


def register_blueprint(app):
    app.register_blueprint(bp_api, url_prefix='/api/v1')
