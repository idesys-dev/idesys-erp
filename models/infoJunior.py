import mongoengine as me
from models.parametres import Parametres
from models.bankDetails import BankDetails
from models.coordinates import Coordinates
from models.contributions import Contributions

class InfoJunior(me.Document):
    parametre = me.ReferenceField(Parametres)(required=True)
    coordinates = me.ReferenceField(Coordinates)(required=True)
    bankDetails = me.ReferenceField(BankDetails)(required=True)
    contributions = me.ReferenceField(Contributions)(required=True)

    


    