import json

from app.models.CattleInfo import CattleInfo, HealthRecord, VaccinationRecord
from app.models.Farm import Farm
from app.models.Farmer import Farmer


def seed_database():
    # Load JSON data from file
    with open("app/data/farmers_data.json", "r") as file:
        data = json.load(file)

    # Iterate through the JSON data and insert into the database
    for farmer_data in data:
        # Check if the farmer already exists
        if not Farmer.objects(farmer_id=farmer_data["farmer_id"]):
            # Create Farmer document
            farmer = Farmer(
                farmer_id=farmer_data["farmer_id"],
                first_name=farmer_data["first_name"],
                last_name=farmer_data["last_name"],
                address=farmer_data["address"],
                contact_number=farmer_data["contact_number"],
                date_of_birth=farmer_data["date_of_birth"],
                username=farmer_data["username"],
                password=farmer_data["password"],
            )
            farmer.save()

            # Iterate through farms
            for farm_data in farmer_data["farms"]:
                # Check if the farm already exists
                if not Farm.objects(farm_id=farm_data["farm_id"]):
                    # Create Farm document
                    farm = Farm(
                        farm_id=farm_data["farm_id"],
                        name=farm_data["name"],
                        location=farm_data["location"],
                        size_acres=farm_data["size_acres"],
                        farmer_id=farmer,
                    )
                    farm.save()

                    # Iterate through cattle
                    for cattle_data in farm_data["cattle_list"]:
                        # Check if the cattle already exists
                        if not CattleInfo.objects(rfid=cattle_data["rfid"]):
                            health_records = [
                                HealthRecord(
                                    checkup_date=record["checkup_date"],
                                    notes=record["notes"],
                                    veterinarian=record["veterinarian"],
                                )
                                for record in cattle_data["health_records"]
                            ]
                            vaccination_records = [
                                VaccinationRecord(
                                    vaccine_name=record["vaccine_name"],
                                    date=record["date"],
                                    administered_by=record["administered_by"],
                                )
                                for record in cattle_data["vaccination_records"]
                            ]
                            cattle = CattleInfo(
                                rfid=cattle_data["rfid"],
                                animal_id=cattle_data["animal_id"],
                                breed=cattle_data["breed"],
                                date_of_birth=cattle_data["date_of_birth"],
                                gender=cattle_data["gender"],
                                farm_id=farm,  # Reference to the Farm document
                                location=cattle_data["location"],
                                health_records=health_records,
                                vaccination_records=vaccination_records,
                                weight=cattle_data["weight"],
                                last_update=cattle_data["last_update"],
                            )
                            cattle.save()
