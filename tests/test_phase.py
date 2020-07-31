import pytest

@pytest.mark.usefixtures("authenticated_request")
def test_phase_auth(client):
    url = 'studies/150/phases'
    response = client.get(url)
    assert response.status_code == 200

def test_phase_not_auth(client):
    url = 'studies/150/phases'
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.usefixtures("authenticated_request")
def test_post_edit_phase(client):
    url = 'studies/150/phases'
    #Create
    create = client.post(url, data=dict(
            name = "test",
            description = "test",
            lenght_week = 1,
            nb_jeh = 1,
            price_jeh = 300,
            phase_number = 1,
            control_point = False,
            bill = False,
            btn = 'Enregistrer'
        ))
    assert create.status_code == 302
