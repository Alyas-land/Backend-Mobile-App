from flask import jsonify, request
from flask.views import MethodView
from app.model.models import User, Product, Basket, BasketItem
from config import db


class UserInfoAPI(MethodView):
    def get(self, user_id):

        user_info = User.query.filter_by(id=user_id).one_or_none()

        if user_info:

            return jsonify(
                {
                    'name': user_info.name,
                    'username': user_info.username,
                    'phone_number': user_info.phone_number,
                    'lastlogin': user_info.lastlogin
                }
            ), 200
        
        return jsonify(
            {
                'msg': 'User Not Found'
            }
        ), 400
    

class UserGetProductsAPI(MethodView):
    def get(self):

        get_all_products = Product.query.all()
        result = [
            {
                'id': int(item.id),
                'name': item.name,
                'imgPath': item.img_path,
                'description': item.descrption,
                
                'price': int(item.price)
            } 
            for item in get_all_products
        ]

        print(result)
        return jsonify(result), 200


class UserAddToBasketAPI(MethodView):
    def post(self):
        data = request.get_json()
        user_id = data.get('user_id')
        product_id = data.get('product_id')
        quantity = data.get('quantity')


        check_basket = Basket.query.filter_by(user_id=user_id, is_active=True).first()
        if check_basket:
            check_exist_product_in_basket = BasketItem.query.filter_by(basket_id=check_basket.id, product_id=product_id).one_or_none()

            if check_exist_product_in_basket:
                check_exist_product_in_basket.quantity += 1

            else:
                new_basket_item = BasketItem(
                    basket_id = check_basket.id,
                    product_id = product_id,
                    quantity = 1,
                    descrption = 'Add to My Basket',
                    # crested_date,
                )
                db.session.add(new_basket_item)
            
        else:
            new_basket = Basket(
                user_id = user_id,
                descrption = 'Create Basket',
                # crested_at ,
            )
            # new_basket.crested_at = new_basket.set_created_at_shamsi()
            db.session.add(new_basket)
            db.session.flush()
            

            new_basket_item = BasketItem(
                    basket_id = new_basket.id,
                    product_id = product_id,
                    quantity = 1,
                    descrption = 'Add to My Basket',
                    # crested_date,
                )
            db.session.add(new_basket_item)       
            
        db.session.commit()
        product = Product.query.filter_by(id=product_id).one_or_none()
        return jsonify(
            {
                'msg': f'{product.name} Basket updated.'
            }
        ), 200
    

class UserShowBasketItem(MethodView):
    def get(self, user_id):
        

        get_basket = Basket.query.filter_by(user_id=user_id, is_active=True).one_or_none()
        if not get_basket:
            return jsonify({'msg': 'Basket not found'}), 404
        
        basket_item_request = BasketItem.query.filter_by(basket_id=get_basket.id).all()
        result = [
            {
                'product_id': item.product_id,
                'product_name': item.product.name,
                'product_description': item.product.descrption,
                'product_price': item.product.price,
                'quantity': item.quantity,
                'img_path': item.product.img_path,
                'item_descrption': item.descrption,
                'item_created_date': item.crested_date,
            }
            for item in basket_item_request
        ]

        return jsonify(result), 200
    

class UserSubmitedActiveBasketAPI(MethodView):
    def get(self, user_id):
        
        basket_request = Basket.query.filter_by(user_id=user_id, is_active=True).one_or_none()
        if not basket_request:
            return jsonify({'msg': 'Basket not found'}), 404
        
        basket_request.is_active = False
        db.session.commit()
        return jsonify({'msg': 'Basket successfully submited'}), 200
    

class UserCancelingBasketApi(MethodView):
    def get(self, user_id):

        basket_request = Basket.query.filter_by(user_id=user_id, is_active=True).one_or_none()
        if not basket_request:
            return jsonify({'msg': 'Basket not found'}), 404
        
        db.session.delete(basket_request)
        db.session.commit()
        return jsonify({'msg': 'Basket successfully canceled'}), 200


class UserAddProductFromCard(MethodView):
    def get(self, user_id, product_id):
        
        basket_target = Basket.query.filter_by(user_id=user_id, is_active=True).one_or_none()

        basket_item_target = BasketItem.query.filter_by(basket_id=basket_target.id, product_id=product_id).one_or_none()

        basket_item_target.quantity += 1
        db.session.commit()

        return jsonify(200)

        

class UserMinusProductFromCard(MethodView):
    def get(self, user_id, product_id):

        basket_target = Basket.query.filter_by(user_id=user_id, is_active=True).one_or_none()

        basket_item_target = BasketItem.query.filter_by(basket_id=basket_target.id, product_id=product_id).one_or_none()

        if (basket_item_target.quantity == 1):
            print('in if')
            db.session.delete(basket_item_target)
            db.session.commit()

            return jsonify(200)
        
        basket_item_target.quantity -= 1
        
        db.session.commit()

        return jsonify(200)
    