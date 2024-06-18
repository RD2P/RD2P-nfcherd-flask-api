import uuid

from mongoengine import Document, FloatField, ListField, ReferenceField, StringField

from app.models.Farmer import Farmer


class Farm(Document):
    farm_id = StringField(primary_key=True, default=lambda: str(uuid.uuid4()))
    name = StringField(required=True, max_length=200)
    location = StringField(required=True, max_length=500)
    size_acres = FloatField(required=True)
    farmer_id = ReferenceField(Farmer, required=True)
    cattle_list = ListField(StringField(max_length=100))

    meta = {"collection": "farm_info"}
