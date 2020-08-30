import mongoengine as me

from models.mail import Mail

class Contacts(me.EmbeddedDocument):
    first_name = me.StringField(required=True)
    last_name = me.StringField(required=True)
    job = me.StringField(required=True)
    email = me.EmailField(required=True)
    phone = me.StringField(required=False)
    mails = me.ListField(me.ReferenceField(Mail))
