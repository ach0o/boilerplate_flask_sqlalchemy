from flask_testing import TestCase

from tests.context import app
from app.db import db


class TestProductRoutes(TestCase):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TESTING = True

    def create_app(self):
        # add test configuration
        _app = app.create_app()
        _app.config['TESTING'] = True

        return _app 

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
