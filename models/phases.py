import mongoengine as me


class Phases(me.EmbeddedDocument):
    name = me.StringField(required=True)
    lenght_week = me.IntField(required=True)
    nb_jeh = me.IntField(required=True)
    price_jeh = me.IntField(required=True)
    phase_number = me.IntField(required=True)
    control_point = me.BooleanField(required=True)
    bill = me.BooleanField(required=True)