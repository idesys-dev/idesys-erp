import mongoengine as me
from models.organisme import Organisme

class Contacts(me.Document):
    idOrganisme = me.ReferenceField(Organisme)(required=True)
    prenom = me.StringField(required=True)
    nom = me.StringField(required=True)
    poste = me.StringField(required=True)
    email = me.StringField(required=True)
    tel = me.StringField