import mongoengine as me

class Organisme(me.Document):
    name = me.StringField(required=True)
    type_structure = me.StringField(required=True)
    adresse = me.StringField(required=True)
    city = me.StringField(required=True)
    postal_code = me.IntField(required=True)
    sector = me.StringField(required=True)

    @staticmethod
    def getOrganisme():
        prospect = [("Aucun", "Aucun")]
        for item in Organisme.objects:
            prospect.append((item.name, item.name))
        return prospect
