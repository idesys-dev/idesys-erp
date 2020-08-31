import pytest
import models as mo

def get_infos():
    study = mo.study.Study.objects.first()
    infos = [0, 0, 0]
    for i in study.list_phases:
        infos[0] += i.price_jeh * i.nb_jeh
        infos[1] += i.nb_jeh
        infos[2] += i.lenght_week
    return infos

@pytest.mark.usefixtures("authenticated_request")
def test_summary_planning(client):
    study = mo.study.Study.objects.first()
    summary_planning = client.get('studies/' + str(study.number) + '/summary/planning')
    infos = get_infos()

    assert summary_planning.status_code == 200
    assert b'<p> Affichage du planning </p>' in summary_planning.data
    assert str(study.number).encode() in summary_planning.data
    assert study.description.encode() in summary_planning.data
    assert str(infos[0]).encode() in summary_planning.data
    assert str(infos[1]).encode() in summary_planning.data
    print(infos)
    print()
    print(summary_planning.data)
    assert str(infos[2]).encode() in summary_planning.data

@pytest.mark.usefixtures("authenticated_request")
def test_summary_budget(client):
    study = mo.study.Study.objects.first()
    summary_budget = client.get('studies/' + str(study.number) + '/summary/budget')
    infos = get_infos()

    assert summary_budget.status_code == 200
    assert b'<table class="table table-bordered table-striped text-center">' in summary_budget.data
    assert str(study.number).encode() in summary_budget.data
    assert str(infos[0]).encode() in summary_budget.data
    assert str(infos[1]).encode() in summary_budget.data
    assert str(infos[2]).encode() in summary_budget.data
