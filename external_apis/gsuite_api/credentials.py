# See https://developers.google.com/identity/protocols/oauth2/service-account

import os

from google.oauth2 import service_account


DEFAULT_USER_EMAIL = 'contactclient@idesys.org'


SERVICE_ACCOUNT_FILE = 'idesys-erp-7323070a412e.json'
if not os.path.exists(SERVICE_ACCOUNT_FILE):
    try:
        GOOGLE_SERVICE_ACCOUNT_INFO = os.environ['GOOGLE_SERVICE_ACCOUNT_INFO']
    except KeyError:
        raise Exception('Provide Google API json file')
    else:
        with open(SERVICE_ACCOUNT_FILE, 'w') as my_file:
            my_file.write(GOOGLE_SERVICE_ACCOUNT_INFO)


def get_delegated_credentials(scopes, user_email=None):
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=scopes)

    return credentials.with_subject(user_email or DEFAULT_USER_EMAIL)
