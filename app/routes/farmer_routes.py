import uuid

from flask import Blueprint, jsonify, request
from mongoengine import DoesNotExist, ValidationError

from app.models.Farm import Farm
from app.models.Farmer import Farmer

farmer_routes = Blueprint("farmer_routes", __name__)


@farmer_routes.route("/farms", methods=["POST"])
def add_farm():
    try:
        data = request.get_json()
        farmer_id = data.get("farmer_id")

        if not farmer_id:
            return jsonify({"error": "Farmer ID is required"}), 400

        farmer = Farmer.objects.get(farmer_id=farmer_id)

        farm = Farm(
            farm_id=str(uuid.uuid4()),
            name=data["name"],
            location=data["location"],
            size_acres=data["size_acres"],
            farmer_id=farmer,
        )
        farm.save()

        return jsonify(farm.to_json()), 201
    except DoesNotExist:
        return jsonify({"error": "Farmer not found"}), 404
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@farmer_routes.route("/farmer/<farmer_id>/farms", methods=["GET"])
def get_farms_by_farmer(farmer_id):
    try:
        farms = Farm.objects(farmer_id=farmer_id)
        farms_json = [farm.to_json() for farm in farms]
        print(farms_json)
        return jsonify(farms_json), 200
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@farmer_routes.route("/farmer/<username>", methods=["GET"])
def get_farmer_by_username(username):
    try:
        farmer = Farmer.objects.get(username=username)
        # return jsonify(farmer.to_json()), 200
        return jsonify(farmer.to_json()), 200
    except DoesNotExist:
        return jsonify({"error": "Farmer not found"}), 404
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
