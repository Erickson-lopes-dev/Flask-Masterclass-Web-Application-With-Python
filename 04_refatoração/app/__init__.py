from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'secret'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    from app import routes
    routes.init_app(app)

    return app