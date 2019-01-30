from logging import Formatter
from logging.handlers import TimedRotatingFileHandler


def set_handlers(app):
    rotating_handler = TimedRotatingFileHandler(
        app.config['LOG_FILEPATH'],
        when='D',
        interval=1,
        backupCount=5)
    rotating_handler.setLevel(app.config['LOG_LEVEL'])
    formatter = Formatter(
        fmt='[%(asctime)s] %(levelname)s '
            '[%(name)s.%(funcName)s:%(lineno)d] %(message)s')
    rotating_handler.setFormatter(formatter)
    app.logger.addHandler(rotating_handler)
