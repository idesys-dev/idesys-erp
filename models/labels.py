import mongoengine as me

class Labels(me.Document):
    category = me.StringField(required=True)
    label = me.StringField(required=True)

    @staticmethod
    def get(labels_id):
        return Labels.objects(id=labels_id).first()

    @staticmethod
    #Gets functions
    def get_labels(typeLabel):
        my_labels = []
        for item in Labels.objects:
            if item.category == typeLabel:
                my_labels.append((item.id, item.label))
        return my_labels