from flask import current_app, jsonify, request
from sqlalchemy.exc import IntegrityError

from app.db import db
from app.models import Product, product_schema, products_schema
from app.routes import bp_api


# Create a product
@bp_api.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']

    new_product = Product(name, description, price, quantity)

    db.session.add(new_product)

    try:
        db.session.commit()
    except IntegrityError as ie:
        current_app.logger.error(f'duplicate data entry: {str(ie.orig)}')
        return jsonify({'message': 'Duplicate data entry'}), 400
    except Exception as e:
        current_app.logger.error(f'Unexpected Error: {str(e)}',
                                 exc_info=True)
        return jsonify({'message': str(e.orig)}), 500

    return product_schema.jsonify(new_product)


# Get all products
@bp_api.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)

    return jsonify(result.data)


# Get a single product
@bp_api.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)

    return product_schema.jsonify(product)


# Update a product
@bp_api.route('/product/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']

    product.name = name
    product.description = description
    product.price = price
    product.quantity = quantity

    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(f'Unexpected Error: {str(e)}',
                                 exc_info=True)
        return jsonify({'message': str(e.orig)}), 500

    return product_schema.jsonify(product)


# Delete a product
@bp_api.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)

    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(f'Unexpected Error: {str(e)}',
                                 exc_info=True)
        return jsonify({'message': str(e.orig)}), 500

    return product_schema.jsonify(product)
