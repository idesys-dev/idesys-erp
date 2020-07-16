import mongoengine as me

class Documents(me.Document):
    path = me.StringField(required=True)
    doc_type = me.StringField(required=True)
    doc_state = me.StringField(required=True)
    signed = me.BooleanField(required=True)
    signed_date = me.StringField
    tags = listDocuments = me.ListField

