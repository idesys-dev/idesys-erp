import mongoengine as me

class Labels(me.Document):
    category = me.StringField(required=True)
    label = me.StringField(required=True)
