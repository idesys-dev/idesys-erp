from app import create_app

def test_index(client):
    response = client.get('/')
    assert response.status_code == 302
