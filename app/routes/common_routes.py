# import datetime
# import platform

# from flask import Blueprint, jsonify, request
# from mongoengine import ValidationError

# from app.models.CattleInfo import CattleInfo, HealthRecord, VaccinationRecord

# from . import main


# @main.route("/", methods=["GET"])
# def default_server_status():
#     server_info = {
#         "server": "running",
#         "time": datetime.datetime.utcnow().isoformat() + "Z",
#         "platform": platform.system(),
#         "platform_version": platform.version(),
#         "architecture": platform.architecture()[0],
#     }
#     return jsonify(server_info), 200


# @main.route("/status", methods=["GET"])
# def get_server_status():
#     server_info = {
#         "server": "running",
#         "time": datetime.datetime.utcnow().isoformat() + "Z",
#         "platform": platform.system(),
#         "platform_version": platform.version(),
#         "architecture": platform.architecture()[0],
#     }
#     return jsonify(server_info), 200

import datetime
import platform

from flask import Blueprint, jsonify, request
from mongoengine import DoesNotExist, ValidationError

from app.models.CattleInfo import CattleInfo
from app.models.Farm import Farm

common_routes = Blueprint("common_routes", __name__)


@common_routes.route("/", methods=["GET"])
def default_server_status():
    server_info = {
        "server": "running",
        "time": datetime.datetime.utcnow().isoformat() + "Z",
        "platform": platform.system(),
        "platform_version": platform.version(),
        "architecture": platform.architecture()[0],
    }
    return jsonify(server_info), 200


@common_routes.route("/status", methods=["GET"])
def get_server_status():
    server_info = {
        "server": "running",
        "time": datetime.datetime.utcnow().isoformat() + "Z",
        "platform": platform.system(),
        "platform_version": platform.version(),
        "architecture": platform.architecture()[0],
    }
    return jsonify(server_info), 200
