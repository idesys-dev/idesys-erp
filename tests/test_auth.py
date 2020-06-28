def test_google_login(client):
    response = client.get('auth/google-login')
    assert response.status_code == 302

def test_user_unauthentiated(client):
    assert client.get('auth/user').status_code == 302
