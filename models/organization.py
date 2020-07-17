import mongoengine as me
from models.labels import Labels
from models.contacts import Contacts

class Organization(me.Document):
    name = me.StringField(required=True)
    adress = me.StringField(required=True)
    city = me.StringField(required=True)
    postal_code = me.IntField(required=True)
    list_labels = me.ListField(me.ReferenceField(Labels))
    list_contacts = me.EmbeddedDocumentListField(Contacts)

    @staticmethod
    def get(orga_id):
        return Organization.objects(id=orga_id).first()