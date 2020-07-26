from models import phases, study, roles, organization, labels, user, missions, contacts, mail
from datetime import date
# pylint:disable=too-many-locals
def starter_db():
    print("Begin seeder")
    #---------- Drop Collections -----------#
    user.User.drop_collection()
    labels.Labels.drop_collection()
    roles.Roles.drop_collection()
    organization.Organization.drop_collection()

    study.Study.drop_collection()
    phases.Phases.drop_collection()
    mail.Mail.drop_collection()

    #-----------  Role ---------#
    rq = roles.Roles(
        name="Responsable Qualité"
    ).save()

    rs = roles.Roles(
        name="Responsable Etude"
    ).save()

    ri = roles.Roles(
        name="Intervenant"
    ).save()


    #-----------  Users ---------#
    ug = user.User(
        email = "ulysse.guyon@idesys.org",
        name = "Ulysse Guyon",
        google_id="01",
        adress = "Quelque Part",
        postal_code = "99999",
        city = "Trouville",
        graduation_classes = "5A",
        mandate = True,
        role = rq.id
    ).save()

    user.User(
        email = "antoine.zuber@idesys.org",
        name = "Antoine ZUBER",
        google_id="",
        adress = "Quelque Part",
        postal_code = "99999",
        city = "",
        graduation_classes = "5A",
        mandate = True,
        role = rq.id
    ).save()

    pt = user.User(
        email = "paul.terrassin@idesys.org",
        name = "Paul Terrassin",
        google_id="02",
        adress = "Quelque Part Autre",
        postal_code = "505050",
        city = "Deauville",
        graduation_classes = "4A",
        mandate = True,
        role = rs.id
    ).save()


    sr = user.User(
        email = "simon.rousseau@gmail.com",
        name = "Simon Rousseau",
        google_id="04",
        adress = "Quelque Part Autre",
        postal_code = "505050",
        city = "Deauville",
        graduation_classes = "5A",
        mandate = False,
        role = ri.id
    ).save()

    am = user.User(
        email = "alex.machin4@gmail.com",
        name = "Alex Machin",
        google_id="03",
        adress = "Quelque Part Autre",
        postal_code = "505050",
        city = "Deauville",
        graduation_classes = "5A",
        mandate = False,
        role = ri.id
    ).save()

    #---------- Labels -----------#
    a20 = labels.Labels (
        category="Année",
        label="2020"
    ).save()

    labels.Labels (
        category="Année",
        label="2019"
    ).save()

    labels.Labels (
        category="Année",
        label="2018"
    ).save()

    labels.Labels (
        category="Filière",
        label="Matériaux"
    ).save()

    fInfo = labels.Labels (
        category="Filière",
        label="Informatique"
    ).save()

    labels.Labels (
        category="Filière",
        label="Electronique"
    ).save()

    labels.Labels (
        category="Filière",
        label="Thermique"
    ).save()

    pDe = labels.Labels (
        category="Prospection",
        label="Demande Spontannée"
    ).save()

    labels.Labels (
        category="Prospection",
        label="Contact direct"
    ).save()

    sEsn = labels.Labels (
        category="Secteur",
        label="Entreprise du Numérique"
    ).save()

    #----------- Study-------------#

    #Phases
    phase_bonnefon_1 = phases.Phases(
        name = "Maquettage",
        lenght_week = 8,
        nb_jeh = 8,
        price_jeh = 400,
        phase_number = 1,
        control_point = False,
        bill = False
    ).save()

    phase_bonnefon_2 = phases.Phases(
        name = "Maquettage 2",
        lenght_week = 8,
        nb_jeh = 5,
        price_jeh = 300,
        phase_number = 1,
        control_point = False,
        bill = False
    ).save()

    phase_bonnefon_3 = phases.Phases(
        name = "Maquettage 3",
        lenght_week = 8,
        nb_jeh = 3,
        price_jeh = 330,
        phase_number = 1,
        control_point = False,
        bill = False
    ).save()

    #Missions
    mis_bonnefon_1 = missions.Missions(
        id_intervener = sr.id,
        name = "Mission Simon",
        begin_date = date(2020,6,15),
        end_date= date(2020,7,20),
        list_documents = [],
        list_phases = [phase_bonnefon_1.id,phase_bonnefon_2.id]
    )

    mis_bonnefon_2 = missions.Missions(
        id_intervener = am.id,
        name = "Mission Alex",
        begin_date = date(2020,6,15),
        end_date= date(2020,7,20),
        list_documents = [],
        list_phases = [phase_bonnefon_3.id]
    )

    # Mails
    mail1 = mail.Mail(
        id_user=ug.id,
        subject="hello (subject :) )",
        from_="ulysse.guyon@idesys.org",
        to="r.dal@some.think",
        body="this is the body of my email",
        date="Sun, 26 Jul 2020 07:31:24 +0000",
    ).save()

    #Contact & organization
    celine = contacts.Contacts(
        first_name = "Céline",
        last_name = "Baudoin",
        job="Travail",
        email="celine.baudoin@grbonnefon.com",
        phone="0699999999"
    )

    john = contacts.Contacts(
        first_name = "John",
        last_name = "Doe",
        job="remote working",
        email="j.doe98@yopmail.com",
        phone="0699999991"
    )

    elon = contacts.Contacts(
        first_name = "Elon",
        last_name = "Musk",
        job="thinker",
        email="e.musk@yopmail.com",
        phone="0699999999",
        mails=[mail1.id]
    )

    bnf = organization.Organization(
        name = "Groupe Bonnefon",
        adress="Adresse du groupe",
        city= "Nantes",
        postal_code="202020",
        list_labels = [],
        list_contacts = [celine, john]
    ).save()

    organization.Organization(
        name = "Tesla",
        adress="space",
        city= "Nantes",
        postal_code="202020",
        list_labels = [],
        list_contacts = [elon]
    ).save()

    #Create Study
    study.Study(
        number=150,
        name="[WEB] - Bonnefon",
        id_organization = bnf.id,
        id_follower_study=pt.id,
        id_follower_quality=ug.id,
        description="Refonte de 6 sites web en WordPress",
        application_fees=100,
        state="progressing",
        list_documents=[],
        list_labels=[a20.id,fInfo.id,pDe.id,sEsn],
        list_missions=[mis_bonnefon_1, mis_bonnefon_2],
        list_phases=[phase_bonnefon_1.id,phase_bonnefon_2.id,phase_bonnefon_3.id]
    ).save()
