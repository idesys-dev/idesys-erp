import mongoengine as me
from models.documents import Documents
from models.phases import Phases
from models.user import User
from models.labels import Labels

class Missions(me.EmbeddedDocument):
    id_intervener = me.ReferenceField(User)
    name = me.StringField(required=True)
    description = me.StringField(required=True)
    begin_date = me.DateField(required=True)
    end_date = me.DateField(required=True)
    list_competences = me.ListField(me.ReferenceField(Labels))
    list_documents = me.ListField(me.ReferenceField(Documents))
    list_phases = me.ListField(me.ReferenceField(Phases))
