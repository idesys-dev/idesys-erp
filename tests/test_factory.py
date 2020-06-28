import pytest

def test_index_not_auth(client):
    response = client.get('/')
    assert response.status_code == 302 # redirect to login

@pytest.mark.usefixtures("authenticated_request")
def test_index_auth(client):
    response = client.get('/')
    assert response.status_code == 200
