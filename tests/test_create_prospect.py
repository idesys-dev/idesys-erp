import pytest

@pytest.mark.usefixtures("authenticated_request")
def test_get_create_study(client):
    url = 'studies/create-prospect'
    response = client.get(url)
    assert response.status_code == 200
    assert b'<form method="post" class="prospect">' in response.data

@pytest.mark.usefixtures("authenticated_request")
def test_post_create_study(client):
    url = 'studies/create-prospect'
    response = client.post(url, data=dict(
            structure_name = "test",
            structure_type = "entreprise",
            adresse = "rue test",
            city = "nantes",
            postal_code = "44000",
            sector = "plomberie",
            name = 'roberto',
            first_name = 'michel',
            position = 'communication',
            email = 'robert@michel.com',
            phone = '0688345262',
            btn = "Enregistrer"
        ))

    assert response.status_code == 302
