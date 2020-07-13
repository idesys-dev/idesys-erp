import mongoengine as me

class Contact(me.Document):
    idOrganisme = me.ObjectIdField(required=True)
    firstName = me.StringField(required=True)
    name = me.StringField(required=True)
    job = me.StringField(required=True)
    email = me.EmailField(required=True)
    phone = me.StringField(required=True)
