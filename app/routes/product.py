from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from app.db import db
from app.models import Product, product_schema, products_schema

api_product = Blueprint('product', __name__, url_prefix='/product')


# Create a product
@api_product.route('/', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']

    new_product = Product(name, description, price, quantity)

    db.session.add(new_product)

    try:
        db.session.commit()
    except IntegrityError:
        return jsonify({'message': 'Duplicate data entry'}), 400
    except Exception as e:
        return jsonify({'message': str(e.orig)}), 400

    return product_schema.jsonify(new_product)


# Get all products
@api_product.route('/', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)

    return jsonify(result.data)


# Get a single product
@api_product.route('/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)

    return product_schema.jsonify(product)


# Update a product
@api_product.route('/<id>', methods=['PUT'])
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
        return jsonify({'message': str(e.orig)}), 400

    return product_schema.jsonify(product)


# Delete a product
@api_product.route('/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)

    try:
        db.session.commit()
    except Exception as e:
        return jsonify({'message': str(e.orig)}), 400

    return product_schema.jsonify(product)
