import mongoengine as me

class Contact(me.Document):
    id_organisme = me.ReferenceField('Organization')
    first_name = me.StringField(required=True)
    name = me.StringField(required=True)
    job = me.StringField(required=True)
    email = me.EmailField(required=True)
    phone = me.StringField(required=True)
