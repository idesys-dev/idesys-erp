import mongoengine as me
from models.user import User

class Parametres(me.Document):
    raisonSocial = me.StringField(required=True)
    statutJuridique = me.StringField(required=True)
    structure = me.StringField(required=True)
    tribunal = me.StringField(required=True)
    dateDebMandat = me.StringField(required=True)

    numProchaineEtude = me.IntField(required=True)
    numProchaineFacture = me.IntField(required=True)
    numProchaineMission = me.IntField(required=True)
    numProchaineBV = me.IntField(required=True)
    numProchaineAvenant = me.IntField(required=True)

    idPresident = me.ReferenceField(User)(required=True)
    idVicePresident = me.ReferenceField(User)(required=True)
    idTresorier = me.ReferenceField(User)(required=True)
    idSecGen= me.ReferenceField(User)(required=True)
    idRespoRH = me.ReferenceField(User)(required=True)
    idRespoQualite = me.ReferenceField(User)(required=True)

    fraisDeDossier = me.IntField(required=True)
    pourcentageAcompteDef = me.IntField(required=True)
    pourcentageRemuDef = me.IntField(required=True)





    