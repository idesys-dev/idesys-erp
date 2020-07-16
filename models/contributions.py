import mongoengine as me

class Contributions(me.Document):
    name = me.StringField(required=True)
    base = me.StringField(required=True)
    junior_rate = me.IntField(required=True)
    student_rate = me.IntField(required=True)
    info = me.StringField





    