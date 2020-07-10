import mongoengine as me
from models.etude import Etude
from models.documents import Documents
from models.phases import Phases
from models.user import User



class Mission(me.Document):
    idEtude = me.ReferenceField(Etude)(required=True)
    idIntervenant = me.ReferenceField(User)(required=True)
    nom = me.StringField(required=True)
    dateDebut = me.StringField(required=True)
    dateFin= me.StringField(required=True)
    listDocuments = me.ListField(me.ReferenceField(Documents))
    listPhases = me.ListField(me.ReferenceField(Phases))