import os

from dotenv import load_dotenv

load_dotenv()

# Root Directory Config
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        f'sqlite:///{os.path.join(ROOT_DIR, "db.sqlite")}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    SECRET_KEY = os.environ.get(
        'SECRET_KEY',
        f'{os.urandom(64)}')
    LOG_DIR = os.environ.get(
        'LOG_DIR',
        f'{os.path.join(ROOT_DIR, "log/app.log")}')


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URL',
        f'sqlite://')


stage = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
