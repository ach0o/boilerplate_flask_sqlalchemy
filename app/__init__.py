import os
import sys

import connexion
from flask import request
from loguru import logger

from . import commands, db, routes
from .config import ROOT_DIR

logger.configure(
    handlers=[
        dict(sink=sys.stderr),
        dict(sink=f'{ROOT_DIR}/log/app.log', rotation='200 MB', level='ERROR')
    ],
    activation=[
        ('app.routes.product', True)
    ]
)


def create_app(config=None):
    # Initialize flask app
    # app = Flask(__name__)
    cxn_app = connexion.FlaskApp(__name__, specification_dir='../')
    cxn_app.add_api('swagger.yml')

    app = cxn_app.app

    # Set database configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL',
        f"sqlite:///{os.path.join(ROOT_DIR, 'db.sqlite')}")
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
    app.url_map.strict_slashes = False

    # Add Commands
    app.cli.command()(commands.create_db)
    app.cli.command()(commands.drop_db)

    return app


app = create_app()


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
