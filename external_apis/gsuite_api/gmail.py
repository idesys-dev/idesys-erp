"""
See https://developers.google.com/gmail/api/quickstart/python
"""


from googleapiclient.discovery import build
# from googleapiclient.http import BatchHttpRequest
from apiclient import errors

TO = 'To'
FROM = 'From'
CC = "Cc"
BCC = "Bcc"
HEADERS_EMAIL_ADDRESS = [TO, FROM, CC, BCC]

SENT = 'SENT'
INBOX = 'INBOX'
HEADER_LABELS = [SENT, INBOX]

def get_mails(creds, contact_mails, start_history_id):
    if not start_history_id:
        start_history_id = '1'
    gmail_service = build('gmail', 'v1', credentials=creds)

    messages_body, gmail_history_id = partial_sync(
        gmail_service, contact_mails, start_history_id)

    if messages_body is False:
        return full_sync(gmail_service, contact_mails)

    return messages_body, gmail_history_id

def partial_sync(gmail_service, contact_mails, start_history_id='1'):
    try:
        history = gmail_service.users().history().list(userId="me",
            startHistoryId=start_history_id,
            historyTypes="messageAdded").execute()
        changes = history['history'] if 'history' in history else []
        while 'nextPageToken' in history:
            page_token = history['nextPageToken']
            history = (gmail_service.users().history().list(userId="me",
                startHistoryId=start_history_id,
                pageToken=page_token).execute())
            changes.extend(history['history'])
    except errors.HttpError as error:
        print('partial_sync: An error occurred: %s' % error)
        return False, '1'
    else:
        changes_message = []
        for history_item in changes:
            for message in history_item['messagesAdded']:
                changes_message.append(message['message'])
        return get_bodys_from_ids(gmail_service, changes_message, contact_mails)


def full_sync(gmail_service, contact_mails):
    messages_ids = get_mail_ids(gmail_service)
    return get_bodys_from_ids(gmail_service, messages_ids, contact_mails)


def get_bodys_from_ids(gmail_service, messages_ids, contact_mails):
    messages_metadata = get_mail_metadada(
        gmail_service, messages_ids, contact_mails)

    messages_body = get_mail_bodys(gmail_service, messages_metadata)

    if messages_metadata:
        # messages_metadata is not empty
        history_id = messages_metadata[0]['historyId']
    else:
        history_id = -1

    return messages_body, history_id

def get_mail_ids(gmail_service):
    messages_ids = []
    try:
        response = gmail_service.users().messages().list(userId="me").execute()

        if 'messages' in response:
            messages_ids.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = gmail_service.users().messages().list(userId="me",
                pageToken=page_token).execute()
            messages_ids.extend(response['messages'])

    except errors.HttpError as error:
        print('get_mail_ids: An error occurred: %s' % error)

    return messages_ids

def get_mail_metadada(gmail_service, messages_ids, contact_mails):
    messages_metadata = []

    for message in messages_ids:
        try:
            message_metadata = gmail_service.users().messages().get(
                userId="me", id=message['id'], format="metadata",
                # metadataHeaders=HEADERS_EMAIL_ADDRESS
                ).execute()
        except errors.HttpError as error:
            print('get_mail_metadada: An error occurred: %s' % error)
        else:
            message_metadata = process_metadata(message_metadata, contact_mails)
            if message_metadata:
                messages_metadata.append(message_metadata)

    return messages_metadata

def process_metadata(message_metadata, contact_mails):
    if SENT in message_metadata['labelIds'] or \
        INBOX in message_metadata['labelIds']:
        for header in message_metadata['payload']['headers']:
            if header['name'] in HEADERS_EMAIL_ADDRESS:
                mail_to_keep = email_in_header(header['value'],
                    contact_mails)
                if mail_to_keep:
                    message_metadata['mail_to_keep'] = mail_to_keep
                    return message_metadata
    return None

def get_mail_bodys(gmail_service, messages_metadata):
    messages_body = []

    for message in messages_metadata:
        try:
            message_body = gmail_service.users().messages().get(
                userId="me", id=message['id'], format="full").execute()
        except errors.HttpError as error:
            print('get_mail_bodys: An error occurred: %s' % error)
        else:
            message_body['mail_to_keep'] = message['mail_to_keep']
            messages_body.append(message_body)

    return messages_body

def email_in_header(header_value, contact_mails):
    if isinstance(header_value, str):
        header_value = [header_value]

    email_list = parse_email_list(header_value)
    mail_to_keep = []
    for email in email_list:
        if email in contact_mails:
            mail_to_keep.append(email)
    return mail_to_keep

def parse_email_str(email):
    if '<' in email and '>' in email:
        email = email[email.find('<')+1:email.find('>')]
    return email

def parse_email_list(emails):
    email_list = []
    for email in emails:
        email_list.append(parse_email_str(email))
    return email_list


# def get_mail_bodyss_(gmail_service, messages_ids, contacts):
#     messages_metadata = []
#
#     def message_callback(request_id, response, exception):
#         if exception is not None:
#             # Do something with the exception.
#             pass
#         else:
#             # Do something with the response.
#             print(response)
#
#
#     length = len(messages_ids)
#     k = 0
#     while k < length:
#         batch = BatchHttpRequest()
#         i = 0
#         while i < 1000:
#             batch.add(gmail_service.users().messages().get(
#                 userId="me", id=messages_ids[k]['id'], format="metadata"),
#                 message_callback)
#             k += 1
#             i += 1
#         batch.execute()
#
#     return messages_metadata
