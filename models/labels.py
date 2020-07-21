import mongoengine as me

class Label(me.Document):
    category = me.StringField(required=True)
    label = me.StringField(required=True)

    @staticmethod
    def get_labels(typeLabel):
        mesLabels = [("Aucun", "Aucun")]
        for item in Label.objects:
            if item.category == typeLabel:
                mesLabels.append((item.label, item.label))
        return mesLabels
