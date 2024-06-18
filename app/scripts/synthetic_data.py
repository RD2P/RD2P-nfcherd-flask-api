import datetime
import json
import random
import uuid

from faker import Faker

fake = Faker()


# Schemas
class Farmer:
    def __init__(self):
        self.farmer_id = str(uuid.uuid4())
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.address = fake.address().replace("\n", ", ")
        self.contact_number = fake.phone_number()
        self.date_of_birth = fake.date_of_birth(
            tzinfo=None, minimum_age=18, maximum_age=80
        ).isoformat()
        self.username = fake.user_name()
        self.password = fake.password()
        self.farms = []


class Farm:
    def __init__(self, farmer_id):
        self.farm_id = str(uuid.uuid4())
        self.name = fake.company()
        self.location = fake.address().replace("\n", ", ")
        self.size_acres = round(random.uniform(10, 1000), 2)
        self.farmer_id = farmer_id
        self.cattle_list = []


class Cattle:
    def __init__(self, farm_id):
        self.rfid = str(uuid.uuid4())
        self.animal_id = str(uuid.uuid4())
        self.breed = random.choice(
            ["Angus", "Hereford", "Holstein", "Jersey", "Simmental"]
        )
        self.date_of_birth = fake.date_between(
            start_date="-10y", end_date="today"
        ).isoformat()
        self.gender = random.choice(["Male", "Female"])
        self.farm_id = farm_id
        self.location = fake.address().replace("\n", ", ")
        self.health_records = [
            {
                "checkup_date": fake.date_this_decade(
                    before_today=True, after_today=False
                ).isoformat(),
                "notes": fake.sentence(),
                "veterinarian": fake.name(),
            }
            for _ in range(random.randint(1, 3))
        ]
        self.vaccination_records = [
            {
                "vaccine_name": random.choice(
                    [
                        "Rabies",
                        "Bovine Virus",
                        "Foot-and-Mouth Disease",
                        "Bovine Tuberculosis",
                        "Clostridial Disease",
                    ]
                ),
                "date": fake.date_this_decade(
                    before_today=True, after_today=False
                ).isoformat(),
                "administered_by": fake.name(),
            }
            for _ in range(random.randint(1, 3))
        ]
        self.weight = round(random.uniform(300, 1500), 2)
        self.last_update = datetime.datetime.utcnow().isoformat()


# Generate data
farmers = []
for _ in range(5):
    farmer = Farmer()
    for _ in range(random.randint(1, 3)):
        farm = Farm(farmer.farmer_id)
        for _ in range(random.randint(1, 15)):
            cattle = Cattle(farm.farm_id)
            farm.cattle_list.append(cattle.__dict__)
        farmer.farms.append(farm.__dict__)
    farmers.append(farmer.__dict__)

# Save to JSON file
with open("farmers_data.json", "w") as file:
    json.dump(farmers, file, indent=4)
