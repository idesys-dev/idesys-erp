import pytest
from models.contact import Contact

@pytest.mark.usefixtures("authenticated_request")
def test_get_create_study(client, mocker):
    mocker.patch(
        'models.contact.Contact.get_all',
        return_value=[Contact("1")]
    )
    url = 'studies/create-study'
    response = client.get(url)
    assert response.status_code == 200
    assert b'<form method="post" class="etude">' in response.data
    assert b'<form method="post" class="submitButton">' in response.data

@pytest.mark.usefixtures("authenticated_request")
def test_post_create_study(client, mocker):
    mocker.patch(
        'models.contact.Contact.get_all',
        return_value=[Contact("1")]
    )
    url = 'studies/create-study'
    response = client.post(url, data=dict(
            study_name = "test",
            follower_study = "robert",
            follower_quality = "michel",
            description = "description test",
            btn = "Enregistrer"
        ))

    assert response.status_code == 302
