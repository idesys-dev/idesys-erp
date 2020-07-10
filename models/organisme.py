import mongoengine as me
from models.labels import Labels

class Organisme(me.Document):
    name = me.StringField(required=True)
    adresse = me.StringField(required=True)
    city = me.StringField(required=True)
    postalCode = me.IntField(required=True)
    listLabels = me.ListField(me.ReferenceField(Labels))
