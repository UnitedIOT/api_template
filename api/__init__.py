# coding=utf-8
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


def create_app():
    """
    :return: application for starting
    """
    app.config.from_object('api.local_settings')

    api = Api(app)

    db.init_app(app)

    @app.route('/hello')
    def index():
        """
        :return:
        """
        return "Hello, World!"

    return app
