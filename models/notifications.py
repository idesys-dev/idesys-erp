import mongoengine as me
from models.user import User

class Notifications(me.Document):
    id_user = me.ReferenceField(User)(required=True)
    title = me.StringField(required=True)
    content = me.StringField(required=True)
    date = me.DateTimeField(required=True)