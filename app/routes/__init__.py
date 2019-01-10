from .product import api_product


def init_app(app):
    app.register_blueprint(api_product)
