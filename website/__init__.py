from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nwkgocqjrnbdnl:079b698c90f7ad4a6562fd41bfcb500720e9b6486c02626f2175a02f2f4f3e33@ec2-34-199-200-115.compute-1.amazonaws.com:5432/d109afai1n644g'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Post,Img

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists("website/" + "nwkgocqjrnbdnl:079b698c90f7ad4a6562fd41bfcb500720e9b6486c02626f2175a02f2f4f3e33@ec2-34-199-200-115.compute-1.amazonaws.com:5432/d109afai1n644g"):
        db.create_all(app=app)
        print("Created database!")

