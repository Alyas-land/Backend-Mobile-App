from config  import app, db
import os
from app.model import models



app_path = os.getcwd()
db_path = os.path.join(app_path + '/app/database')


app.config['SECRET_KEY'] = '1c954735a63f171d721b415008b830c73ec57564'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}/myShop.db'
db.init_app(app)

from app.routes.auth_api import LoginAPI
from app.routes.user_api import UserInfoAPI

#routes
app.add_url_rule('/api/user/login', view_func=LoginAPI.as_view('login_api'))
app.add_url_rule('/api/user/info/<int:user_id>', view_func=UserInfoAPI.as_view('user_info_api'))


@app.before_request
def createDatabase():
    db.create_all()
    print("Tables created.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


