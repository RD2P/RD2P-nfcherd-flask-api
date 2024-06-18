from flask import Blueprint, jsonify, request
from mongoengine import DoesNotExist, ValidationError

from app.models.CattleInfo import CattleInfo
from app.models.Farm import Farm

cattle_routes = Blueprint("cattle_routes", __name__)


@cattle_routes.route("/cattle/<cattle_id>", methods=["GET"])
def get_cattle_info(cattle_id):
    try:
        cattle = CattleInfo.objects.get(animal_id=cattle_id)
        return jsonify(cattle.to_json()), 200
    except DoesNotExist:
        return jsonify({"error": "Cattle not found"}), 404
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@cattle_routes.route("/farm/<farm_id>/cattles", methods=["GET"])
def get_cattles_by_farm(farm_id):
    try:
        farm = Farm.objects.get(farm_id=farm_id)
        cattles = CattleInfo.objects(farm_id=farm)
        cattles_json = [cattle.to_json() for cattle in cattles]
        return jsonify(cattles_json), 200
    except DoesNotExist:
        return jsonify({"error": "Farm not found"}), 404
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
