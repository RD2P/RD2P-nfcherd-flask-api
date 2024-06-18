import mongoengine as me
from flask import Flask

from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    print(" ********************* Initialized Flask ********************* ")

    me.connect(app.config["MONGODB_NAME"], host=app.config["MONGODB_URI"])

    with app.app_context():
        print("Plug in any app context here")

    from .routes import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
