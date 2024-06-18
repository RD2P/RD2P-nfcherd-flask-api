import datetime
from mongoengine import connect
from bcrypt import hashpw, gensalt

from CattleInfo import CattleInfo, OwnerInfo, VaccinationRecord, HealthRecord
from CowInfo import CowInfo
from Farm import Farm
from Farmer import Farmer

connect('farm_db')

def create_mock_data():
    farmers = []
    for i in range(10):
        farmer = Farmer(
            farmer_id=f"farmer_{i}",
            first_name=f"FirstName_{i}",
            last_name=f"LastName_{i}",
            address=f"Address_{i}",
            contact_number=f"123-456-78{i:02d}",
            date_of_birth=datetime.datetime(1970, 1, 1 + i),
            username=f"user_{i}",
            password=hashpw(f"password_{i}".encode('utf-8'), gensalt()).decode('utf-8'),
            farm_ids=[f"farm_{i}"]
        )
        farmer.save()
        farmers.append(farmer)

    farms = []
    for i in range(10):
        farm = Farm(
            farm_id=f"farm_{i}",
            name=f"FarmName_{i}",
            location=f"Location_{i}",
            size_acres=100.0 + i,
            farmer_id=farmers[i],
            cattle_list=[f"cattle_{i}", f"cattle_{(i+1)%10}"]
        )
        farm.save()
        farms.append(farm)

    cattle_infos = []
    for i in range(10):
        cattle_info = CattleInfo(
            rfid=f"rfid_{i}",
            animal_id=f"animal_{i}",
            breed=f"Breed_{i}",
            date_of_birth=datetime.datetime(2020, 1, 1 + i),
            gender="Male" if i % 2 == 0 else "Female",
            owner_info=OwnerInfo(
                name=f"Owner_{i}",
                address=f"OwnerAddress_{i}",
                contact_number=f"321-654-78{i:02d}"
            ),
            location=f"Location_{i}",
            health_records=[
                HealthRecord(
                    checkup_date=datetime.datetime(2021, 1, 1 + i),
                    notes=f"Notes_{i}",
                    veterinarian=f"Vet_{i}"
                )
            ],
            vaccination_records=[
                VaccinationRecord(
                    vaccine_name=f"Vaccine_{i}",
                    date=datetime.datetime(2021, 6, 1 + i),
                    administered_by=f"Admin_{i}"
                )
            ],
            weight=100.0 + i,
            last_update=datetime.datetime.utcnow()
        )
        cattle_info.save()
        cattle_infos.append(cattle_info)

    for i in range(10):
        cow_info = CowInfo(
            cattle_id=f"cattle_{i}",
            farm_id=f"farm_{i}",
            last_update=datetime.datetime.utcnow()
        )
        cow_info.save()

create_mock_data()
