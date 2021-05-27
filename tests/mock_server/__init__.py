from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    if os.environ.get("FLASK_ENV") == "development":
        app.config["ENV"] = "development"
        app.config["DEBUG"] = 1

    from .discourse import discourse

    app.register_blueprint(discourse)

    return app
