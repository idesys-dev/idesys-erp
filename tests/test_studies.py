import pytest

@pytest.mark.usefixtures("authenticated_request")
def test_dashboard_auth(client):
    url = 'studies/dashboard'
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.usefixtures("authenticated_request")
def test_dashoard_tabs(client):
    progressing = client.get('studies/dashboard/progressing')
    failed = client.get('studies/dashboard/failed')
    finished = client.get('studies/dashboard/finished')

    assert progressing.status_code == 200
    assert b'En cours' in progressing.data
    assert failed.status_code == 200
    assert b'Avortees' in failed.data
    assert finished.status_code == 200
    assert b'Terminees' in finished.data

    
def test_dashoard_tabs_unauth(client):
    progressing = client.get('studies/dashboard/progressing')
    assert progressing.status_code == 302
  
