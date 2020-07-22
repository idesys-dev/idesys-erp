import pytest

@pytest.mark.usefixtures("authenticated_request")
def test_dashboard_auth(client):
    url = 'studies/dashboard'
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.usefixtures("authenticated_request")
def test_dashoard_title(client):
    url = 'studies/dashboard/progressing'
    response = client.get(url)
    assert response.status_code == 200
    assert b'En cours' in response.data
