import mongoengine as me

class Documents(me.Document):
    chemin = me.StringField(required=True)
    typeDoc = me.StringField(required=True)
    etatDoc = me.StringField(required=True)
    signature = me.BooleanField(required=True)
    dateSignature = me.StringField
    dateSignature = me.StringField(required=True)
    tags = listDocuments = me.ListField

