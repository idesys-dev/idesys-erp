import mongoengine as me

class Etude(me.Document):
    number = me.IntField(required=True)
    name = me.StringField(required=True)
    idFollowerQuality = me.StringField(required=True)
    idFollowerStudy = me.StringField(required=True)
    description = me.StringField(required=True)
    applicationFees = me.IntField(required=True)
    state = me.StringField(required=True)
    listDocuments = me.ListField()
    listLabels = me.ListField(required=True)
