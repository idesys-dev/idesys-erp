import pytest

@pytest.mark.usefixtures("authenticated_request")
def test_dashboard_auth(client):
    url = 'studies/dashboard'
    response = client.get(url)
    assert response.status_code == 200
