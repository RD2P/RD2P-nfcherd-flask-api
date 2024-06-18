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

    from app.routes import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from app.routes.cattle_routes import cattle_routes as cattle_blueprint

    app.register_blueprint(cattle_blueprint, url_prefix="/api")

    from app.routes.common_routes import common_routes as common_blueprint

    app.register_blueprint(common_blueprint, url_prefix="/api")

    from app.routes.farm_routes import farm_routes as farm_blueprint

    app.register_blueprint(farm_blueprint, url_prefix="/api")

    from app.routes.farmer_routes import farmer_routes as farmer_blueprint

    app.register_blueprint(farmer_blueprint, url_prefix="/api")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
