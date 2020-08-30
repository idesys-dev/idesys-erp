import base64


import mongoengine as me
from models.user import User
from external_apis.gsuite_api.gmail import TO, FROM, CC, BCC

DATE = "Date"
SUBJECT = "Subject"

class Mail(me.Document):
    id_user = me.ReferenceField(User)
    subject = me.StringField(required=True)
    from_ = me.StringField(required=True)
    to = me.StringField(required=True)
    cc = me.StringField()
    bcc = me.StringField()
    date = me.StringField(required=True)
    body = me.StringField(required=True)

    @staticmethod
    def create_mail_instance(message, user_id):
        date = ""
        subject = ""
        to = ""
        from_ = ""
        cc = ""
        bcc = ""
        for header in message['payload']['headers']:
            if header['name'] == DATE:
                date = header['value']
            if header['name'] == SUBJECT:
                subject = header['value']
            if header['name'] == TO:
                to = header['value']
            if header['name'] == FROM:
                from_ = header['value']
            if header['name'] == CC:
                cc = header['value']
            if header['name'] == BCC:
                bcc = header['value']

        return Mail(id_user=user_id,
            subject=subject,
            from_=from_,
            to=to,
            cc=cc,
            bcc=bcc,
            date=date,
            body=Mail.decode_body(message))

    @staticmethod
    def decode_body(message):
        if 'body' not in message['payload']:
            return message['snippet']

        raw = message['payload']['parts'][-1]['body']['data']

        return base64.urlsafe_b64decode(raw.encode()).decode()
