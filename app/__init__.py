import os

import connexion

from . import commands, db, routes, logger
from config import stages


def create_app():
    # Initialize flask app
    # app = Flask(__name__)
    cxn_app = connexion.FlaskApp(__name__, specification_dir='../')
    cxn_app.add_api('swagger.yml')

    app = cxn_app.app

    app.config.from_object(stages[os.environ.get('FLASK_ENV', 'development')])
    # possible configuration injection
    #   app.config.update(config) # dict
    #   app.config.from_json(config) # path to json file
    #   app.config.from_pyfile(config) # path to py file

    # Register app to other modules
    db.init_app(app)
    routes.register_blueprint(app)
    app.url_map.strict_slashes = False
    logger.set_handlers(app)

    # Add Commands
    app.cli.command()(commands.create_db)
    app.cli.command()(commands.drop_db)

    return app


app = create_app()
