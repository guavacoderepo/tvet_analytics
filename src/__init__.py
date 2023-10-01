from flask import Flask
from flask_cors import CORS

from src.controllers.graduates import graduates





def create():
    app = Flask(__name__)
    CORS(app=app)

    app.register_blueprint(graduates)


    return app



