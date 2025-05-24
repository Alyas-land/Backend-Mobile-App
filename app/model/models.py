from config import db
from flask_login import UserMixin
from persiantools.jdatetime import JalaliDateTime, JalaliDate
import pytz


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable= False)
    phone_number = db.Column(db.String(11), nullable= False)
    email = db.Column(db.String(200), nullable= False)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    lastlogin = db.Column(db.String(200), nullable=False, default= JalaliDateTime.now().strftime("%Y/%m/%d -- %H:%M"))
    img_path = db.Column(db.String(200))

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable= False)
    descrption = db.Column(db.Text, nullable= False)
    img_path = db.Column(db.String(200))


    
    products = db.relationship('Product', backref='category', lazy=True)



class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable= False)
    img_path = db.Column(db.String(200), nullable=False)
    descrption = db.Column(db.Text, nullable= False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.String(200), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    basket_items = db.relationship('BasketItem',backref='product', lazy=True)


class Basket(db.Model):
    __tablename__ = 'baskets'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(1000), nullable=False, default=f'سبد خرید')
    descrption = db.Column(db.Text,)
    crested_at = db.Column(db.String(200), default= JalaliDateTime.now().strftime("%Y/%m/%d -- %H:%M"))
    is_active = db.Column(db.Boolean, default=True)

    items = db.relationship('BasketItem', backref='basket', lazy=True)

    # def set_created_at_shamsi(self):
    #     date = 
    #     self.crested_at = date

class BasketItem(db.Model):
    __tablename__ = 'basket_items'

    id = db.Column(db.Integer, primary_key=True)
    basket_id = db.Column(db.Integer, db.ForeignKey('baskets.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer, nullable=False)
    descrption = db.Column(db.Text,)
    crested_date = db.Column(db.String(200), nullable= False, default= JalaliDate(JalaliDateTime.now()).strftime("%Y/%m/%d -- %H:%M"))






