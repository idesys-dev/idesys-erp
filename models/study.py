import mongoengine as me
from models.labels import Labels
from models.documents import Documents
from models.missions import Missions
from models.user import User


class Study(me.Document):
    number = me.IntField(required=True)
    name = me.StringField(required=True)
    id_follower_quality = me.ReferenceField(User)
    id_follower_study = me.ReferenceField(User)
    description = me.StringField(required=True)
    application_fees = me.IntField(required=True)
    state = me.StringField(required=True)
    list_documents = me.ListField(me.ReferenceField(Documents))
    list_labels = me.ListField(me.ReferenceField(Labels))
    list_missions = me.EmbeddedDocumentListField(Missions)

