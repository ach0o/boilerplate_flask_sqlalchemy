import os

from pytest import fixture

from app import create_app
from app.config import ROOT_DIR
from app.db import db
from app.models import Product

from .context import app


@fixture(scope='session')
def fx_app():
    test_config = {
        "SQLALCHEMY_DATABASE_URI":
        f"sqlite:///{os.path.join(ROOT_DIR, 'test.sqlite')}"
    }

    app = create_app(config=test_config)
    app.config['TESTING'] = True

    app.app_context().push()

    fx_db = db
    fx_db.init_app(app)

    # Reset the database
    fx_db.session.remove()
    fx_db.drop_all()
    fx_db.session.commit()

    fx_db.create_all()
    return app


@fixture
def fx_session(fx_app):
    fx_db = db
    fx_db.init_app(fx_app)

    # Reset the database
    fx_db.session.remove()
    fx_db.drop_all()
    fx_db.session.commit()

    fx_db.create_all()
    return fx_db.session


@fixture(scope='session')
def fx_client(fx_app):
    return fx_app.test_client()


@fixture
def data():
    return dict(name='A black pen', description='A pen with black ink',
                price=2.00, quantity=300)


@fixture
def another_data():
    return dict(name='A red pen', description='A pen with red ink',
                price=1.80, quantity=100)
