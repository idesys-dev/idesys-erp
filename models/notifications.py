import mongoengine as me
from models.user import User

class Notifications(me.Document):
    id_user = me.ReferenceField(User)
    title = me.StringField
    content = me.StringField
    date = me.DateTimeField

    