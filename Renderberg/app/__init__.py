from flask import Flask
from .feature.routes import feature


def create_app():
    app = Flask(__name__)
    app.register_blueprint(feature)
    return app

