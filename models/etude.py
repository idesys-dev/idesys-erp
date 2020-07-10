import mongoengine as me
from models.labels import Labels
from documents.models.document import Document

class Etude(me.Document):
    number = me.IntField(required=True)
    name = me.StringField(required=True)
    idFollowerQuality = me.StringField(required=True)
    idFollowerStudy = me.StringField(required=True)
    description = me.StringField(required=True)
    applicationFees = me.IntField(required=True)
    state = me.StringField(required=True)
    listDocuments = me.ListField(me.ReferenceField(Document))
    listLabels = me.ListField(me.ReferenceField(Labels))

