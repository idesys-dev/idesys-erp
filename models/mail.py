import base64


import mongoengine as me
from models.user import User

class Mail(me.Document):
    id_user = me.ReferenceField(User)
    body = me.StringField(required=True)

    @staticmethod
    def decode_body(message):
        if 'body' in message['payload']:
            return message['snippet']

        raw = message['payload']['parts'][-1]['body']['data']

        return base64.urlsafe_b64decode(raw.encode()).decode()
