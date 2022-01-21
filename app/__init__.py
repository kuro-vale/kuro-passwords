# App
from app.config import Config
# Flask
from flask import Flask
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    app.debug = 1
    app.env = "development"
    app.config.from_object(Config)
    Bootstrap(app)
    return app
