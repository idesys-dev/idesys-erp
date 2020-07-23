import mongoengine as me
from models.user import User

class Settings(me.Document):
    social_reason = me.StringField(required=True)
    legal_status = me.StringField(required=True)
    structure = me.StringField(required=True)
    court = me.StringField(required=True)
    begin_mandate_date = me.DateTimeField(required=True)

    num_next_study = me.IntField(required=True)
    num_next_bill = me.IntField(required=True)
    num_next_mission = me.IntField(required=True)
    num_next_payment_slip = me.IntField(required=True) #BV
    num_next_amendment = me.IntField(required=True) #Avenants

    id_president = me.ReferenceField(User)(required=True)
    id_vp = me.ReferenceField(User)(required=True)
    id_treasurer = me.ReferenceField(User)(required=True)
    id_secretary = me.ReferenceField(User)(required=True)
    id_human_ressources = me.ReferenceField(User)(required=True)
    id_resp_quality = me.ReferenceField(User)(required=True)

    application_fees = me.IntField(required=True)
    percentage_offset_default = me.IntField(required=True) #Frais de dossier
    percentage_pay_default = me.IntField(required=True) #Paiment intervenant