from config  import app, db
import os
from app.model import models
from flask_migrate import Migrate



app_path = os.getcwd()
db_path = os.path.join(app_path + '/app/database')


app.config['SECRET_KEY'] = '1c954735a63f171d721b415008b830c73ec57564'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}/myShop.db'
db.init_app(app)

migrate = Migrate(app, db)
migrate.init_app(app, db)

from app.routes.auth_api import LoginAPI, RegisterAPI
from app.routes.user_api import UserInfoAPI, UserGetProductsAPI,\
UserAddToBasketAPI, UserShowBasketItem, UserSubmitedActiveBasketAPI,\
UserCancelingBasketApi

#routes

# Authentication route
app.add_url_rule('/api/user/login', view_func=LoginAPI.as_view('login_api'))
app.add_url_rule('/api/user/register', view_func=RegisterAPI.as_view('register_api'), methods= ['POST'])


# User route
app.add_url_rule('/api/user/info/<int:user_id>', view_func=UserInfoAPI.as_view('user_info_api'))
app.add_url_rule('/api/user/products', view_func=UserGetProductsAPI.as_view('user_products_api'))
app.add_url_rule('/api/user/products/add_to_card', view_func=UserAddToBasketAPI.as_view('user_add_card_api'))
app.add_url_rule('/api/user/active_basket/<int:user_id>', view_func=UserShowBasketItem.as_view('user_active_basket'))
app.add_url_rule('/api/user/submit_basket/<int:user_id>', view_func=UserSubmitedActiveBasketAPI.as_view('user_submit_active_basket'))
app.add_url_rule('/api/user/cancel_basket/<int:user_id>', view_func=UserCancelingBasketApi.as_view('user_cancel_active_basket'))


@app.before_request
def createDatabase():
    db.create_all()
    print("Tables created.")

if __name__ == '__main__':
    app.run(
        debug=True, host='0.0.0.0',
        port=5000,
        )


