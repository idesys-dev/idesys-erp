import mongoengine as me

class Contacts(me.EmbeddedDocument):
    first_name = me.StringField(required=True)
    last_name = me.StringField(required=True)
    job = me.StringField(required=True)
    email = me.EmailField(required=True)
    tel = me.StringField(required=True)