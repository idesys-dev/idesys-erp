from flask_login import UserMixin
import mongoengine as me

from models.roles import Roles
from models.documents import Documents
from models.labels import Labels

class User(UserMixin, me.Document):
    email = me.EmailField(required=True)
    name = me.StringField(required=True)
    profile_pic = me.StringField()
    google_id = me.StringField(required=True)

    #Ajout pour la db 
    adress = me.StringField(required=False)
    postal_code = me.StringField(required=False)
    city = me.StringField(required=False)
    graduation_classes = me.StringField(required=False)
    mandate = me.BooleanField(required=False)
    role = me.ReferenceField(Roles)
    list_label = me.ListField(me.ReferenceField(Labels))
    list_documents = me.ListField(me.ReferenceField(Documents))

    gmail_history_id = me.StringField()

    #pylint: disable=invalid-overridden-method
    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False
    #pylint: enable=invalid-overridden-method

    def get_id(self):
        return self.google_id

    @staticmethod
    def get(user_id):
        return User.objects(google_id=user_id).first()
    
    @staticmethod
    #Get admin(True) or intervener(False) 
    def get_admin_intervener(type_user):
        print("get_admin_intervener")
        users = [("Aucun", "Aucun")]
        for i in User.objects:
            if i.role is not None : 
                #Case of interverner
                if not type_user and i.role.name == "Intervenant":
                    users.append((i.id, i.name))
                #Case of admins    
                elif type_user and i.role.name != "Intervenant":
                    users.append((i.id, i.name))
        return users