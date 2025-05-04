from config import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable= False)
    phone_number = db.Column(db.String(11), nullable= False)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    lastlogin = db.Column(db.String(200), nullable=False)

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable= False)
    descrption = db.Column(db.Text, nullable= False)
    
    products = db.relationship('Product', backref='category', lazy=True)



class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable= False)
    descrption = db.Column(db.Text, nullable= False)
    price = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.String(200), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    basket_items = db.relationship('BasketItem',backref='product', lazy=True)


class Basket(db.Model):
    __tablename__ = 'baskets'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    descrption = db.Column(db.Text,)
    crested_at = db.Column(db.String(200), nullable= False)
    is_active = db.Column(db.Boolean, default=True)

    items = db.relationship('BasketItem', backref='basket', lazy=True)

class BasketItem(db.Model):
    __tablename__ = 'basket_items'

    id = db.Column(db.Integer, primary_key=True)
    basket_id = db.Column(db.Integer, db.ForeignKey('baskets.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer, nullable=False)
    descrption = db.Column(db.Text,)
    crested_date = db.Column(db.String(200), nullable= False)






