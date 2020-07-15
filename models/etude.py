import mongoengine as me

class Etude(me.Document):
    number = me.IntField(required=True)
    organisme = me.StringField(required=True)
    name = me.StringField(required=True)
    id_follower_quality = me.StringField(required=True)
    id_follower_study = me.StringField(required=True)
    description = me.StringField(required=True)
    application_fees = me.IntField(required=True)
    state = me.StringField(required=True)
    list_documents = me.ListField()
    list_labels = me.ListField(required=True)
