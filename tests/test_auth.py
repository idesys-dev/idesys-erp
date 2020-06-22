import pytest
from flask import session, g
from flask_login import current_user

from auth.models.user import User

def test_google_login(client):
    response = client.get('auth/google-login')
    assert response.status_code == 302

@pytest.mark.usefixtures("authenticated_request")
def test_login(client):
    print(current_user)
    print(current_user.google_id)
    assert current_user.google_id == 'test_google_id'

def test_user_unauthentiated(client):
    assert client.get('auth/user').status_code == 302
