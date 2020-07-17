import mongoengine as me

class Study(me.Document):
    number = me.IntField(required=True)
    organisme= me.ReferenceField('Organization')
    name = me.StringField(required=True)
    follower_quality= me.ReferenceField('User')
    follower_study= me.ReferenceField('User')
    description = me.StringField(required=True)
    application_fees = me.IntField(required=True)
    state = me.StringField(required=True)
    list_documents = me.ListField()
    list_labels = me.ListField(required=True)
