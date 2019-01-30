import os
import sys

import connexion
from flask import request
from loguru import logger

from . import commands, db, routes
from config import stage


def create_app():
    # Initialize flask app
    # app = Flask(__name__)
    cxn_app = connexion.FlaskApp(__name__, specification_dir='../')
    cxn_app.add_api('swagger.yml')

    app = cxn_app.app

    app.config.from_object(stage[os.environ.get('FLASK_ENV', 'development')])
    # possible configuration injection
    #   app.config.update(config) # dict
    #   app.config.from_json(config) # path to json file
    #   app.config.from_pyfile(config) # path to py file

    # Register app to other modules
    db.init_app(app)
    routes.register_blueprint(app)
    app.url_map.strict_slashes = False

    # Add Commands
    app.cli.command()(commands.create_db)
    app.cli.command()(commands.drop_db)

    return app


app = create_app()
logger.configure(
    handlers=[
        dict(sink=sys.stderr),
        dict(sink=app.config['LOG_DIR'], rotation='200 MB', level='ERROR')
    ],
    activation=[
        ('app.routes.product', True)
    ]
)


@app.after_request
def log_request(response):
    if response.status_code != 200:
        logger.error(f'{request.remote_addr} - {request.remote_user} '
                     f'referrer:{request.referrer} {request.user_agent} '
                     f'{request.method} {response.status_code} {request.url} '
                     f'req:{request.json} res:{response.get_json()}')
    else:
        logger.debug(f'{request.remote_addr} - {request.remote_user} '
                     f'referrer:{request.referrer} {request.user_agent} '
                     f'{request.method} {response.status_code} {request.url} '
                     f'req:{request.json} res:{response.get_json()}')
    return response
