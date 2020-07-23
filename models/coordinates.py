import mongoengine as me

class Coordinates(me.Document):
    address_1 = me.StringField(required=True)
    address_2 = me.StringField(required=True)
    postal_code = me.IntField(required=True)
    city = me.StringField(required=True)
    tel = me.StringField(required=True)
    mail_contact = me.StringField(required=True)
    web_site = me.StringField(required=True)
    school = me.StringField(required=True)
    siret = me.StringField(required=True)
    code_ape = me.StringField(required=True)
    num_urssaf = me.StringField(required=True)
    vat_number = me.StringField(required=True)
    check = me.StringField(required=True)