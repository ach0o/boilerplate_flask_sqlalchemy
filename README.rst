Boilerplate Flask SQLAlchemy
============================

|build| |coverage|

Overview
--------

This is a boilerplate RESTful app based on Flask + SQLAlchemy
with gunicorn, Nginx and Docker.

....

Getting Started
---------------

Installation
^^^^^^^^^^^^
.. code-block:: console

  $ cd boilerplate_flask_sqlalchemy/

  $ pip install -U pipenv  # If you don't have pipenv, checkout https://pipenv.readthedocs.io/en/latest/#install-pipenv-today
  $ export PIPENV_VENV_IN_PROJECT=1  # Let the virtual environment and packages to be installed in the project
  $ pipenv install  # Install required packages
  $ pipenv shell  # Activate the virtual environment

  $(.venv) flask create-db  # Initialize database
  $(.venv) gunicorn --workers 1 --bind 0.0.0.0:8901 app:app  # Launch the app


Try it out
^^^^^^^^^^
.. code-block:: console

  $ curl -i http://0.0.0.0:8901/product


Setup for development
^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

  $ pipenv install --dev  # Install dev-packages like pytest

  $ git config core.hooksPath hooks  # Set hooks for `git commit` and `git push`

  $ cp .env_example .env  # Create a copy of dotenv file for configurations

....

Working with Docker
-------------------

1. Install `docker <https://www.docker.com/>`_ and `docker-compose <https://docs.docker.com/compose/>`_

2. Build docker image:

  .. code-block:: console

    $ docker-compose build


  To edit a tag of the docker image, edit ``image`` from the ``docker-compose.yml``

3. Launch:

  .. code-block:: console

    $ docker-compose up -d

....

Deployment
----------

Heroku
^^^^^^
- Refer to `Heroku Deployment <https://devcenter.heroku.com/categories/deployment>`_

Private Server (TODO)
^^^^^^^^^^^^^^^^^^^^^
1. Create new docker image from CircleCi
2. Push the image to the Container Registry (eg. `DockerHub <https://www.docker.com/products/docker-hub>`_)
3. Assess your server and install dependencies like docker and docker-compose
4. Pull the image created and run:

  .. code-block:: console

    $ docker run -p 80:80 -d <IMAGE ID>


....

Documentation
-------------

General Documentation
^^^^^^^^^^^^^^^^^^^^^

To build the documentation, simply run


.. code-block:: console

  $ cd docs/
  $ . ./collect_and_build.sh

Documentation page will automatically open up!


API Documentation (RESTful)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Swagger UI is used for this documentation. The configuration can be found at ``swagger.yml``.

To see the documentation, run the app and simply go to

* ``http://{YOUR_HOST}:{YOUR_PORT}/ui``

.. |build| image:: https://circleci.com/gh/achooan/boilerplate_flask_sqlalchemy/tree/master.svg?style=shield
    :target: https://circleci.com/gh/achooan/boilerplate_flask_sqlalchemy/tree/master

.. |coverage| image:: https://codecov.io/gh/achooan/boilerplate_flask_sqlalchemy/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/achooan/boilerplate_flask_sqlalchemy