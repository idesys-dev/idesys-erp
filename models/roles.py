import mongoengine as me

class Roles(me.Document):
    name = me.StringField(required=True)
    actions = me.StringField(required=False)