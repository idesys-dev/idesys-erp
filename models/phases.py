import mongoengine as me
from models.etude import Etude


class Phases(me.Document):
    idEtude = me.ReferenceField(Etude)(required=True)
    duréeSemaine = me.IntField(required=True)
    nbJEH = me.IntField(required=True)
    prixJEH = me.IntField(required=True)
    numPhase = me.IntField(required=True)
    ptControle = me.BooleanField(required=True)
    facture = me.BooleanField(required=True)