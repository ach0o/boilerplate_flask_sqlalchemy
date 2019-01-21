from app.db import db, mw


__all__ = ['Product', 'product_schema', 'products_schema']


# Product Class/Model
class Product(db.Model):
    """Class represents a data model with primary id, unique name, description,
    price and quantity.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def __init__(self, name, description, price, quantity):
        """An initialization method for data model

        Args:
            name: An unique and identifiable name of a product

        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


# Product schema
class ProductSchema(mw.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'quantity')


# Initialize schema
product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(strict=True, many=True)
