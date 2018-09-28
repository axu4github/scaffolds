# coding=utf-8

from flask import Flask
from flaskr.configs import config


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(config["testing"])

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    from .apis import apis
    app.register_blueprint(apis)

    return app
