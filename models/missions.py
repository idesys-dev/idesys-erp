import mongoengine as me
from models.documents import Documents
from models.phases import Phases
from models.user import User

class Missions(me.EmbeddedDocument):
    id_intervener = me.ReferenceField(User)
    name = me.StringField(required=True)
    begin_date = me.DateTimeField(required=True)
    end_date= me.DateTimeField(required=True)
    list_documents = me.ListField(me.ReferenceField(Documents))
    list_phases = me.ListField(me.ReferenceField(Phases))
