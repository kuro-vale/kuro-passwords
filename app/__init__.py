# App
from app.auth.models import UserModel
from app.auth.views import auth
from app.config import Config
# Flask
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)


def create_app():
    app = Flask(__name__)
    app.debug = 1
    app.env = "development"
    app.config.from_object(Config)
    Bootstrap(app)
    app.register_blueprint(auth)
    login_manager.init_app(app)
    return app
