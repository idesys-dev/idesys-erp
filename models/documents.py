import mongoengine as me

class Documents(me.Document):
    path = me.StringField(required=True)
    doc_type = me.StringField(required=True)
    doc_state = me.StringField(required=True)
    signed = me.BooleanField(required=True)
    signed_date = me.StringField(required=False)
    tags = me.ListField(required=False)

    @staticmethod
    def get(doc_id):
        return Documents.objects(id=doc_id).first()
