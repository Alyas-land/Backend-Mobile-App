from config  import app, db
import os
from app.model import models


app_path = os.getcwd()
db_path = os.path.join(app_path + '/app/database')


app.config['SECRET_KEY'] = '1c954735a63f171d721b415008b830c73ec57564'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}/myShop.db'
db.init_app(app)

@app.before_request
def createDatabase():
    db.create_all()
    print("Tables created.")

if __name__ == '__main__':
    app.run(debug=True)