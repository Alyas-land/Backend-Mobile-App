import os

def database_initialize(app, db):
    app_path = os.getcwd()
    db_path = os.path.join(app_path + '/app/database')


    if (os.path.isfile(os.path.isfile(db_path + '/myShop.db'))):
        pass
    else:
        app.config['SECRET_KEY'] = '1c954735a63f171d721b415008b830c73ec57564'
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}/myShop.db'
        db.init_app(app)



    

# db = Sq
# print(os.path.isfile(db_path + '/myShop.db'))