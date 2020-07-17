import mongoengine as me

class Labels(me.Document):
    category = me.StringField(required=True)
    label = me.StringField(required=True)

    @staticmethod
    def get(labels_id):
        return Labels.objects(id=labels_id).first()