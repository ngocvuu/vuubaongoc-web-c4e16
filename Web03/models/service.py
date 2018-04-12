from mongoengine import *
import datetime
# Create collection
# Design database
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() #0: female, 1: male
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    image = URLField()
    description = StringField()
    measurements = ListField()

class Customer(Document):
    name = StringField()
    email = EmailField()
    username = StringField()
    password = StringField()

class Order(Document):
    serviceid = ReferenceField(Service)
    userid = ReferenceField(Customer)
    time = DateTimeField()
    is_accepted = BooleanField()
