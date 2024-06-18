from flask import Blueprint

main = Blueprint("main", __name__)

from .cattle_routes import *
from .common_routes import *
