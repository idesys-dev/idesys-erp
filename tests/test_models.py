import models as mo

#---------- Tests getters ----------#
def test_user_get():
    unique_id = "1010"
    user = mo.user.User(
        google_id=unique_id,
        name="nathan",
        email="nathan.seva@idesys.org",
        profile_pic=""
    ).save()
    user = mo.user.User.get(unique_id)
    assert user.email == "nathan.seva@idesys.org"

def test_labels_get():
    var_temp = "Test"
    lbl= mo.labels.Labels(
        label=var_temp,
        category = "Cat"
    ).save()
    lbl2 = mo.labels.Labels.get(lbl.id)
    assert lbl2.category == "Cat"

def test_phases_get():
    var_temp = "Test"
    test = mo.phases.Phases(
        name = var_temp,
        lenght_week = 8,
        nb_jeh = 5,
        price_jeh = 300,
        phase_number = 1,
        control_point = False,
        bill = False
    ).save()
    test2 = mo.phases.Phases.get(test.id)
    assert test2.name == var_temp

def test_documents_get():
    test = mo.documents.Documents(
        path = "Test",
        doc_type = "",
        doc_state = "",
        signed = False,
    ).save()
    test2 = mo.documents.Documents.get(test.id)
    assert test2.path == "Test"

def test_study_get():
    test = mo.study.Study(
        number = 0,
        name = "",
        description = "",
        application_fees = False,
        state = ""
    ).save()
    test2 = mo.study.Study.get(test.id)
    assert test2.number == 0

def test_organization_get():
    test = mo.organization.Organization(
        name="test",
        adress="",
        city="",
        postal_code=0
    ).save()

    test2 = mo.organization.Organization.get(test.id)
    assert test2.name == "test"

def test_organization_get_organization():
    mo.organization.Organization.drop_collection()
    o1 = mo.organization.Organization(
        name="o1",
        adress="",
        city="",
        postal_code=0
    ).save()

    o2 = mo.organization.Organization(
        name="o2",
        adress="",
        city="",
        postal_code=0
    ).save()

    test2 = mo.organization.Organization.get_organization()
    assert test2 == [(o1.id,"o1"),(o2.id,"o2")]