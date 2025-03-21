from app import db
from datetime import datetime

class User(db.Model):
    """
    User model for the database.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def set_password(self, password):
        """
        Hashes the password and stores it in the database.
        """
        from bcrypt import hashpw, gensalt
        self.password = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

    def check_password(self, password):
        """
        Verifies if the provided password matches the hashed password in the database.
        """
        from bcrypt import checkpw
        return checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

class Product(db.Model):
    """
    Product model for the database.
    """
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)