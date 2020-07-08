import mongoengine as me

class Label(me.Document):
    category = me.StringField(required=True)
    label = me.StringField(required=True)
