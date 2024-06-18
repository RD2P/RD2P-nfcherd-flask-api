from flask import Blueprint

main = Blueprint("main", __name__)

from .cattle_routes import cattle_routes
from .common_routes import common_routes
from .farm_routes import farm_routes
from .farmer_routes import farmer_routes

# Register blueprints
main.register_blueprint(cattle_routes, url_prefix="/api")
main.register_blueprint(common_routes, url_prefix="/api")
main.register_blueprint(farm_routes, url_prefix="/api")
main.register_blueprint(farmer_routes, url_prefix="/api")
