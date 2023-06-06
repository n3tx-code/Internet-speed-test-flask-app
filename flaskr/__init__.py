from flask import Flask

from . import databse


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='./db.sqlite',
    )
    databse.init_app(app)
    return app
