import mongoengine as me

class Etude(me.Document):
    number = me.IntField(required=True)
    organisme= me.ReferenceField('Organisme')
    name = me.StringField(required=True)
    follower_quality= me.ReferenceField('User')
    follower_study= me.ReferenceField('User')
    description = me.StringField(required=True)
    application_fees = me.IntField(required=True)
    state = me.StringField(required=True)
    list_documents = me.ListField()
    list_labels = me.ListField(required=True)
