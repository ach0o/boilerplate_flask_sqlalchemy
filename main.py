import os

from app import create_app

if __name__ == '__main__':
    debug = os.environ.get('ENV', 'dev') == 'dev'

    create_app().run(host='0.0.0.0',
                     port=int(os.environ.get('PORT', 5000)),
                     load_dotenv=True,
                     debug=debug)
