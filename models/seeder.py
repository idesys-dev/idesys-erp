import models as mo
from datetime import date

def starter_db():
    
    #----------- Définition Users ---------#
    ug = mo.user.User(
        email = "ulysse.guyon@idesys.org",
        name = "Ulysse Guyon",
        google_id="0",
        adress = "Quelque Part",
        postal_code = "99999",
        city = "Trouville",
        graduation_classes = "5A",
        mandate = True
    ).save()

    pt = mo.user.User(
        email = "paul.terrassin@idesys.org",
        name = "Paul Terrassin",
        google_id="0",
        adress = "Quelque Part Autre",
        postal_code = "505050",
        city = "Deauville",
        graduation_classes = "4A",
        mandate = True
    ).save()


    sr = mo.user.User(
        email = "simon.rousseau@gmail.com",
        name = "Simon Rousseau",
        google_id="0",
        adress = "Quelque Part Autre",
        postal_code = "505050",
        city = "Deauville",
        graduation_classes = "5A",
        mandate = False
    ).save()

    am = mo.user.User(
        email = "alex.machin4@gmail.com",
        name = "Alex Machin",
        google_id="0",
        adress = "Quelque Part Autre",
        postal_code = "505050",
        city = "Deauville",
        graduation_classes = "5A",
        mandate = False,
    ).save()

    #---------- Définition des labels -----------#
    a20 = mo.labels.Labels (
        category="Année",
        label="2020"
    ).save()

    mo.labels.Labels (
        category="Année",
        label="2019"
    ).save()

    mo.labels.Labels (
        category="Année",
        label="2018"
    ).save()

    mo.labels.Labels (
        category="Filière",
        label="Matériaux"
    ).save()

    fInfo = mo.labels.Labels (
        category="Filière",
        label="Informatique"
    ).save()

    mo.labels.Labels (
        category="Filière",
        label="Electronique"
    ).save()

    mo.labels.Labels (
        category="Filière",
        label="Thermique"
    ).save()

    pDe = mo.labels.Labels (
        category="Prospection",
        label="Demande Spontannée"
    ).save()

    mo.labels.Labels (
        category="Prospection",
        label="Contact direct"
    ).save()

    sEsn = mo.labels.Labels (
        category="Secteur",
        label="Entreprise du Numérique"
    ).save()

    #----------- Definition d'une étude -------------#

    #Définitions des phases
    phase_bonnefon_1 = mo.phases.Phases(
        name = "Maquettage",
        lenght_week = 8,
        nb_jeh = 8,
        price_jeh = 400,
        phase_number = 1,
        control_point = False,
        bill = False
    ).save()

    phase_bonnefon_2 = mo.phases.Phases(
        name = "Maquettage 2",
        lenght_week = 8,
        nb_jeh = 5,
        price_jeh = 300,
        phase_number = 1,
        control_point = False,
        bill = False
    ).save()

    phase_bonnefon_3 = mo.phases.Phases(
        name = "Maquettage 3",
        lenght_week = 8,
        nb_jeh = 3,
        price_jeh = 330,
        phase_number = 1,
        control_point = False,
        bill = False
    ).save()

    #Définitions des missions
    mis_bonnefon_1 = mo.missions.Missions(
        id_intervener = sr.id,
        name = "Mission Simon",
        begin_date = date(2020,6,15),
        end_date= date(2020,7,20),
        list_documents = [],
        list_phases = [phase_bonnefon_1.id,phase_bonnefon_2.id]
    )

    mis_bonnefon_2 = mo.missions.Missions(
        id_intervener = am.id,
        name = "Mission Alex",
        begin_date = date(2020,6,15),
        end_date= date(2020,7,20),
        list_documents = [],
        list_phases = [phase_bonnefon_3.id]
    )

   


    #Création de l'étude
    mo.study.Study(
        number=150,
        name="[WEB] - Bonnefon",
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

    #Contact et organisme 
    celine = mo.contacts.Contacts(
        first_name = "Céline",
        last_name = "Baudoin",
        job="Travail",
        email="celine.baudoin@grbonnefon.com",
        tel="0699999999"
    )

    mo.organization.Organization(
        name = "Groupe Bonnefon",
        adress="Adresse du groupe",
        city= "Nantes",
        postal_code="202020",
        list_labels = [],
        list_contacts = [celine]
    ).save() 