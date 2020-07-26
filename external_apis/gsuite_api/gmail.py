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
HEADERS = [TO, FROM, CC, BCC]

def get_mails(creds, contact_mails):
    gmail_service = build('gmail', 'v1', credentials=creds)

    messages_ids = get_mail_ids(gmail_service)

    messages_metadata = get_mail_metadada(
        gmail_service, messages_ids, contact_mails)

    messages_body = get_mail_bodys(gmail_service, messages_metadata)

    return messages_body

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
        print('An error occurred: %s' % error)

    return messages_ids

def get_mail_metadada(gmail_service, messages_ids, contact_mails):
    messages_metadata = []

    try:
        for message in messages_ids[:50]:
            message_metadata = gmail_service.users().messages().get(
                userId="me", id=message['id'], format="metadata",
                metadataHeaders=HEADERS).execute()
            for header in message_metadata['payload']['headers']:
                if header['name'] in HEADERS:
                    mail_to_keep = email_in_header(header['value'],
                        contact_mails)
                    if mail_to_keep:
                        message_metadata['mail_to_keep'] = mail_to_keep
                        messages_metadata.append(message_metadata)
    except errors.HttpError as error:
        print('An error occurred: %s' % error)

    return messages_metadata

def get_mail_bodys(gmail_service, messages_metadata):
    messages_body = []

    try:
        for message in messages_metadata:
            message_body = gmail_service.users().messages().get(
                userId="me", id=message['id'], format="full").execute()

            message_body['mail_to_keep'] = message['mail_to_keep']
            messages_body.append(message_body)
    except errors.HttpError as error:
        print('An error occurred: %s' % error)

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
