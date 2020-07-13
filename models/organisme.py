import mongoengine as me

class Organisme(me.Document):
    name = me.StringField(required=True)
    typeStructure = me.StringField(required=True)
    adresse = me.StringField(required=True)
    city = me.StringField(required=True)
    postalCode = me.IntField(required=True)
    sector = me.StringField(required=True)
