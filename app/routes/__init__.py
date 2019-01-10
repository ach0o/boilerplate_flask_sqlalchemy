from .product import api_product


def register_blueprint(app):
    app.register_blueprint(api_product)
