from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


# Initialize sqlalchemy
db = SQLAlchemy()

# Initialize marshmallow
mw = Marshmallow()


def init_app(app):
    db.init_app(app)
    mw.init_app(app)
