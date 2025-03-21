from flask import request, jsonify
from app import db
from app.models import User, Product

def init_app(app):
    """
    Initialize routes for the Flask app.
    """
    @app.route('/signup', methods=['POST'])
    def signup():
        """
        Endpoint to register a new user.
        """
        data = request.get_json()
        name = data.get('name')
        username = data.get('username')
        password = data.get('password')

        # Create a new user
        new_user = User(name=name, username=username)
        new_user.set_password(password)  # Hash the password

        # Add to the database
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created"}), 201

    @app.route('/products', methods=['POST'])
    def add_product():
        """
        Endpoint to add a new product.
        """
        data = request.get_json()
        pname = data.get('pname')
        description = data.get('description')
        price = data.get('price')
        stock = data.get('stock')

        # Create a new product
        new_product = Product(pname=pname, description=description, price=price, stock=stock)

        # Add to the database
        db.session.add(new_product)
        db.session.commit()

        return jsonify({"message": "Product added"}), 201