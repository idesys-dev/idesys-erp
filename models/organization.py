import mongoengine as me

class Organization(me.Document):
    name = me.StringField(required=True)
    type_structure = me.StringField(required=True)
    adresse = me.StringField(required=True)
    city = me.StringField(required=True)
    postal_code = me.IntField(required=True)
    sector = me.StringField(required=True)

    @staticmethod
    def getOrganization():
        prospect = [("Aucun", "Aucun")]
        for item in Organization.objects:
            prospect.append((item.name, item.name))
        return prospect
