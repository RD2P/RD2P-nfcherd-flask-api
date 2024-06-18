import datetime
from mongoengine import Document, StringField, DateField

class CowInfo(Document):
    cattle_id = StringField(required=True, max_length=100)
    farm_id = StringField(required=True, max_length=100)
    last_update = DateField(default=datetime.datetime.utcnow)

    meta = {"collection": "cow_info"}