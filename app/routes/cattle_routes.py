from flask import Blueprint, jsonify, request
from mongoengine import ValidationError

from app.models.CattleInfo import CattleInfo, HealthRecord, OwnerInfo, VaccinationRecord

from . import main


@main.route("/cattle/<rfid>", methods=["GET"])
def get_cattle_info(rfid):
    try:
        cattle = CattleInfo.objects.get(rfid=rfid)
        return jsonify(cattle.to_json()), 200
    except CattleInfo.DoesNotExist:
        return jsonify({"error": "Cattle not found"}), 404
    except ValidationError:
        return jsonify({"error": "Invalid RFID"}), 400


@main.route("/cattle", methods=["POST"])
def add_cattle():
    data = request.get_json()
    try:
        owner_info = OwnerInfo(**data.get("owner_info"))
        vaccination_records = [
            VaccinationRecord(**v) for v in data.get("vaccination_records", [])
        ]
        health_records = [HealthRecord(**h) for h in data.get("health_records", [])]

        cattle = CattleInfo(
            rfid=data["rfid"],
            animal_id=data["animal_id"],
            breed=data.get("breed"),
            date_of_birth=data.get("date_of_birth"),
            gender=data.get("gender"),
            owner_info=owner_info,
            location=data.get("location"),
            health_records=health_records,
            vaccination_records=vaccination_records,
            weight=data.get("weight"),
            last_update=data.get("last_update"),
        )
        cattle.save()
        return jsonify(cattle.to_json()), 201
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400


@main.route("/cattle/<rfid>", methods=["PUT"])
def update_cattle(rfid):
    data = request.get_json()
    try:
        cattle = CattleInfo.objects.get(rfid=rfid)
        if "owner_info" in data:
            cattle.owner_info = OwnerInfo(**data["owner_info"])
        if "vaccination_records" in data:
            cattle.vaccination_records = [
                VaccinationRecord(**v) for v in data["vaccination_records"]
            ]
        if "health_records" in data:
            cattle.health_records = [HealthRecord(**h) for h in data["health_records"]]

        cattle.update(
            animal_id=data.get("animal_id", cattle.animal_id),
            breed=data.get("breed", cattle.breed),
            date_of_birth=data.get("date_of_birth", cattle.date_of_birth),
            gender=data.get("gender", cattle.gender),
            owner_info=cattle.owner_info,
            location=data.get("location", cattle.location),
            health_records=cattle.health_records,
            vaccination_records=cattle.vaccination_records,
            weight=data.get("weight", cattle.weight),
            last_update=data.get("last_update", cattle.last_update),
        )
        return jsonify(cattle.to_json()), 200
    except CattleInfo.DoesNotExist:
        return jsonify({"error": "Cattle not found"}), 404
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400


@main.route("/cattle/<rfid>", methods=["DELETE"])
def delete_cattle(rfid):
    try:
        cattle = CattleInfo.objects.get(rfid=rfid)
        cattle.delete()
        return jsonify({"message": "Cattle deleted successfully"}), 200
    except CattleInfo.DoesNotExist:
        return jsonify({"error": "Cattle not found"}), 404
    except ValidationError:
        return jsonify({"error": "Invalid RFID"}), 400
