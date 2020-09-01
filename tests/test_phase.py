import pytest
import models as mo

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
def test_post_create_phase(client):
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

@pytest.mark.usefixtures("authenticated_request")
def test_post_delete_phase(client):
    url = 'studies/150/phases'
    #Delete
    phs = mo.phases.Phases.objects(phase_number=1).first()
    delete = client.post(url, data=dict(
            btn = 'Supprimer',
            hidden = phs.id
        ))
    assert delete.status_code == 302

@pytest.mark.usefixtures("authenticated_request")
def test_post_edit_phase(client):
    url = 'studies/150/phases'
    #Create
    phs = mo.phases.Phases.objects(phase_number=1).first()

    edit = client.post(url, data=dict(
            name = "test",
            description = "test",
            lenght_week = 1,
            nb_jeh = 1,
            price_jeh = 300,
            phase_number = 1,
            control_point = False,
            bill = False,
            btn = 'Modifier',
            hidden2 = phs.id,
            hidden3 = 0
        ))
    assert edit.status_code == 302