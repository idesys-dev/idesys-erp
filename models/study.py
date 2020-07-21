import mongoengine as me

from models.labels import Labels
from models.documents import Documents
from models.missions import Missions
from models.phases import Phases
from models.user import User
from models.organization import Organization


class Study(me.Document):
    number = me.IntField(required=True)
    name = me.StringField(required=True)
    id_organization = me.ReferenceField(Organization)
    id_follower_quality = me.ReferenceField(User)
    id_follower_study = me.ReferenceField(User)
    description = me.StringField(required=True)
    application_fees = me.IntField(required=True)
    state = me.StringField(required=True)
    list_documents = me.ListField(me.ReferenceField(Documents))
    list_labels = me.ListField(me.ReferenceField(Labels))
    list_missions = me.EmbeddedDocumentListField(Missions)
    list_phases = me.ListField(me.ReferenceField(Phases))

    @staticmethod
    def get(study_id):
        return Study.objects(id=study_id).first()
