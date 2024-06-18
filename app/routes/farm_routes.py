from flask import Blueprint, jsonify, request
from mongoengine import DoesNotExist, ValidationError

from app.models.Farm import Farm
from app.models.Farmer import Farmer

farm_routes = Blueprint("farm_routes", __name__)


@farm_routes.route("/farm/<farm_id>", methods=["GET"])
def get_farm_by_id(farm_id):
    try:
        farm = Farm.objects.get(farm_id=farm_id)
        return jsonify(farm.to_json()), 200
    except DoesNotExist:
        return jsonify({"error": "Farm not found"}), 404
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# @farm_routes.route("/farms", methods=["POST"])
# def add_farm():
#     try:
#         data = request.get_json()
#         farmer_id = data.get("farmer_id")

#         if not farmer_id:
#             return jsonify({"error": "Farmer ID is required"}), 400

#         farmer = Farmer.objects.get(farmer_id=farmer_id)

#         farm = Farm(
#             farm_id=str(uuid.uuid4()),
#             name=data["name"],
#             location=data["location"],
#             size_acres=data["size_acres"],
#             farmer_id=farmer,
#         )
#         farm.save()

#         return jsonify(farm.to_json()), 201
#     except DoesNotExist:
#         return jsonify({"error": "Farmer not found"}), 404
#     except ValidationError as e:
#         return jsonify({"error": str(e)}), 400
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
