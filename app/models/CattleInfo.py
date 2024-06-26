import datetime

from mongoengine import (
    DateField,
    Document,
    EmbeddedDocument,
    EmbeddedDocumentField,
    FloatField,
    ListField,
    ReferenceField,
    StringField,
)


class VaccinationRecord(EmbeddedDocument):
    vaccine_name = StringField(required=True, max_length=200)
    date = DateField(required=True)
    administered_by = StringField(max_length=200)


class HealthRecord(EmbeddedDocument):
    checkup_date = DateField(required=True)
    notes = StringField(max_length=1000)
    veterinarian = StringField(max_length=200)


class CattleInfo(Document):
    rfid = StringField(required=True, unique=True, max_length=50)
    animal_id = StringField(required=True, max_length=100)
    breed = StringField(max_length=100)
    date_of_birth = DateField()
    gender = StringField(choices=["Male", "Female"], max_length=10)
    farm_id = ReferenceField("Farm", required=True)  # Reference to the Farm schema
    location = StringField(max_length=500)
    health_records = ListField(EmbeddedDocumentField(HealthRecord))
    vaccination_records = ListField(EmbeddedDocumentField(VaccinationRecord))
    weight = FloatField()
    last_update = DateField(default=datetime.datetime.utcnow)

    meta = {"collection": "cattle_info"}
