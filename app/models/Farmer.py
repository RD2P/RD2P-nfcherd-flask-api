from mongoengine import Document, StringField, DateField, ListField

class Farmer(Document):
    farmer_id = StringField(required=True, unique=True, max_length=100)
    first_name = StringField(required=True, max_length=100)
    last_name = StringField(required=True, max_length=100)
    address = StringField(required=True, max_length=500)
    contact_number = StringField(required=True, max_length=20)
    date_of_birth = DateField(required=True)
    username = StringField(required=True, unique=True, max_length=100)
    password = StringField(required=True, max_length=255)
    farm_ids = ListField(StringField(max_length=100))

    meta = {"collection": "farmer_info"}
