import mongoengine as me

class Labels(me.Document):
    category = me.StringField(required=True)
    label = me.StringField(required=True)

    @staticmethod
    def get(labels_id):
        return Labels.objects(id=labels_id).first()

    @staticmethod 
    def getLabels(typeLabel):
        mesLabels = [("Aucun", "Aucun")]
        for item in Labels.objects:
            if item.category == typeLabel:
                mesLabels.append((item.label, item.label))
        return mesLabels
