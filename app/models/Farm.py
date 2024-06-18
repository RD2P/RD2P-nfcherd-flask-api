from mongoengine import Document, StringField, ListField, ReferenceField, FloatField
from Farmer import Farmer

class Farm(Document):
    farm_id = StringField(required=True, unique=True, max_length=100)
    name = StringField(required=True, max_length=200)
    location = StringField(required=True, max_length=500)
    size_acres = FloatField(required=True)
    farmer_id = ReferenceField(Farmer, required=True)
    cattle_list = ListField(StringField(max_length=100)) 

    meta = {"collection": "farm_info"}