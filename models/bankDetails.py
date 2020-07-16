import mongoengine as me

class BankDetails(me.Document):
    rib = me.StringField(required=True)
    domiciliation = me.StringField(required=True)
    iban = me.StringField(required=True)
    bic = me.StringField(required=True)
    





    