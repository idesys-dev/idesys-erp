import pytest

@pytest.mark.usefixtures("authenticated_request")
def test_dashboard_auth(client):
    response = client.get('/etudes/dashboard')
    assert response.status_code == 200
