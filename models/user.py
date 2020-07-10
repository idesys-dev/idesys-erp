from flask_login import UserMixin
import mongoengine as me

class User(UserMixin, me.Document):
    email = me.EmailField(required=True)
    name = me.StringField(required=True)
    profile_pic = me.StringField()
    google_id = me.StringField(required=True)

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
