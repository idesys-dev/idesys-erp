import mongoengine as me
from models.settings import Settings
from models.bank_details import BankDetails
from models.coordinates import Coordinates
from models.contributions import Contributions

class InfoJunior(me.Document):
    settings = me.ReferenceField(Settings)(required=True)
    coordinates = me.ReferenceField(Coordinates)(required=True)
    bank_details = me.ReferenceField(BankDetails)(required=True)
    contributions = me.ReferenceField(Contributions)(required=True)