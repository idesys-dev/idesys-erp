from flask import Blueprint, request, render_template, url_for, redirect
from flask_login import current_user

from studies.forms import TypeCreate, ProspectChoice, CreateStudy, CreateProspect, CreateContact, LabelsForm, CreateMission
import models as mo

studies_bp = Blueprint('studies_bp', __name__, template_folder='templates')

@studies_bp.before_request
def restrict_bp_to_admins():
    if not current_user.is_authenticated:
        return redirect(url_for('auth_bp.login'))
    return None

#Study dashboard
#Tabs
@studies_bp.route('/dashboard', methods=['GET', 'POST'])
@studies_bp.route('/dashboard/<tab>', methods=['GET', 'POST'])
def dashboard(tab='all'):
    list_category = []
    for i in mo.labels.Labels.objects :
        if i.category not in list_category :
            list_category.append(i.category)

    if tab == 'all' :
        title = "Toutes les études"

    elif tab == 'progressing':
        title = "En cours"

    elif tab == 'finished':
        title = "Terminees"

    elif tab == 'failed':
        title = "Avortees"

    return render_template('dashboard.html',
            study=mo.study.Study.objects,
            labels=mo.labels.Labels.objects,
            list_category=list_category,
            title=title,
            tab=tab )

#Context function
@studies_bp.context_processor
def utility_processor():
    def get_info(id_study):
        total_price = 0
        tot_jeh = 0
        total_length = 0
        if id_study == '':
            return "Id non valide"

        sty = mo.study.Study.get(id_study)

        for i in sty.list_phases:
            total_price += i.price_jeh * i.nb_jeh
            tot_jeh += i.nb_jeh
            total_length += i.lenght_week

        return {"price":total_price,
                "tot_jeh": tot_jeh,
                "tot_weeks": total_length}

    return dict(get_info=get_info)

@studies_bp.route('/create-study', methods=['GET', 'POST'])
def create_study():
    # We declare all forms we describe in the forms.py
    formLabel = LabelsForm(request.form)
    formCreateStudy = CreateStudy(request.form)
    formSubmit = TypeCreate(request.form)

    #Edit prospect
    list_prospect = mo.organization.Organization.objects
    formProspectChoice = ProspectChoice(request.form, obj=list_prospect)
    formProspectChoice.prospect_choice.choices = [(g.id, g.name) for g in list_prospect.order_by('name')]


    if request.method == 'POST':
        if request.form['btn'] == 'Valider' and formSubmit.structure_save.data == 'Non':
            # If the prospect doesn't exist, we create it
            return redirect(url_for(".create_prospect"))

        if request.form['btn'] ==  'Enregistrer':
            etu = mo.study.Study(
                number = 12, #change needed
                name = formCreateStudy.study_name.data,
                id_organization = formProspectChoice.prospect_choice.data,
                id_follower_quality = formCreateStudy.follower_quality.data,
                id_follower_study = formCreateStudy.follower_study.data,
                description = formCreateStudy.description.data,
                application_fees = 100,
                state = "Début",
                list_labels = [formLabel.year.data, formLabel.sector.data, formLabel.prospection.data] )
            etu.save()

            return redirect(url_for("index"))

    # If the prospect already exist, we have to choose it
    return render_template('createStudy.html',
    formCreateStudy=formCreateStudy,
    formLabel=formLabel,
    formSubmit=formSubmit,
    formProspectChoice=formProspectChoice )

@studies_bp.route('/create-prospect', methods=['GET', 'POST'])
def create_prospect():
    formCreateProspect = CreateProspect(request.form)
    formCreateContact = CreateContact(request.form)

    if request.method == 'POST':
        if request.form['btn'] ==  'Enregistrer':
            cont = mo.contacts.Contacts(
                first_name = formCreateContact.first_name.data,
                last_name = formCreateContact.name.data,
                job = formCreateContact.position.data,
                email = formCreateContact.email.data,
                phone = formCreateContact.phone.data )

            org = mo.organization.Organization(
                name = formCreateProspect.structure_name.data,
                adress = formCreateProspect.adresse.data,
                city = formCreateProspect.city.data,
                postal_code = formCreateProspect.postal_code.data,
                list_labels = [formCreateProspect.sector.data],
                list_contacts=[cont])
            org.save()

            return redirect(url_for(".create_study"))

    return render_template('createProspect.html',
    formCreateProspect=formCreateProspect,
    formCreateContact=formCreateContact )

@studies_bp.route('/<num_study>/summary/<vision>', methods=['GET', 'POST'])
def summary_study(num_study=None, vision="planning"):
    study = mo.study.Study.objects(number=num_study).first()

    return render_template('recapStudy.html',
    study=study,
    vision=vision)

@studies_bp.route('/<num_study>/missions', methods=['GET', 'POST'])
def missions(num_study=None):
    sty = mo.study.Study.objects(number=num_study).first()
    form_create_mission = CreateMission(request.form)

    alert = [0, 0]
    for x in sty.list_phases:
        alert[0] += x.nb_jeh

    list_form = []
    list_dates = [ [] for a in range(len(sty.list_missions)) ]
    for index, element in enumerate(sty.list_missions):
        # Change date format to dd/mm/yyyy to display
        list_dates[index].append(element.begin_date.strftime("%d/%m/%Y"))
        list_dates[index].append(element.end_date.strftime("%d/%m/%Y"))
        list_dates[index].append(int((element.end_date - element.begin_date).days / 7))

        # Initiate forms to edit missions
        form = CreateMission(request.form)
        list_form.append(form)

        # Get information of number of JEH attached and display an alert
        for y in element.list_nb_jeh:
            alert[1] += y

    if request.method == 'GET':
        # Get data from database to fill mission's edit form
        for j in range(len(sty.list_missions)) :
            i = sty.list_missions[j]
            my_form = list_form[j]

            my_form.intervenant.data = (i.id_intervener.id, i.id_intervener.name)
            my_form.mission_name.data = i.name
            my_form.description.data = i.description

    if request.method == 'POST':

        if request.form['btn'] ==  'Modifier':
            # Request to edit a mission, we update database with form's data
            id_mission_edit = int(request.form['hidden2'])
            my_form = list_form[int(request.form['hidden3'])]

            list_phases_jeh = [ [], [] ]
            for my_phase in sty.list_phases:
                # We store the phase object and the number of jeh enter by the user
                list_phases_jeh[0].append(my_phase)
                list_phases_jeh[1].append(int(request.form[str(my_phase.name)]))

            sty.list_missions[id_mission_edit-1].name = my_form.mission_name.data
            sty.list_missions[id_mission_edit-1].description = my_form.description.data
            sty.list_missions[id_mission_edit-1].begin_date = request.form['date_start']
            sty.list_missions[id_mission_edit-1].end_date = request.form['date_end']
            sty.list_missions[id_mission_edit-1].list_phases = list_phases_jeh[0]
            sty.list_missions[id_mission_edit-1].list_nb_jeh = list_phases_jeh[1]

            sty.save()
            return redirect(url_for('studies_bp.missions', num_study=num_study)) # We force the page to refresh

        if request.form['btn'] ==  'Supprimer':
            # Request to delete a mission from database
            sty.update(pull__list_missions__id_mission = int(request.form['hidden']))
            return redirect(url_for('studies_bp.missions', num_study=num_study)) # We force the page to refresh

        if request.form['btn'] ==  'Enregistrer':
            # Request to register a new mission in database
            list_phases_jeh = [ [], [] ]
            for my_phase in sty.list_phases:
                # We store the phase object and the number of jeh enter by the user
                list_phases_jeh[0].append(my_phase)
                list_phases_jeh[1].append(int(request.form[str(my_phase.name)]))

            if len(sty.list_missions) == 0:
                my_id_mission = 1
            else:
                my_id_mission = len(sty.list_missions) + 1

            my_mission = mo.missions.Missions(
                    id_mission = my_id_mission,
                    id_intervener = form_create_mission.intervenant.data,
                    name = form_create_mission.mission_name.data,
                    description = form_create_mission.description.data,
                    begin_date = request.form['date_start'],
                    end_date = request.form['date_end'],
                    list_phases = list_phases_jeh[0],
                    list_nb_jeh = list_phases_jeh[1] )

            sty.list_missions.append(my_mission)
            sty.save()
            return redirect(url_for('studies_bp.missions', num_study=num_study)) # We force the page to refresh

    return render_template('missions.html',
    study=sty,
    form_create_mission=form_create_mission,
    list_dates=list_dates,
    list_form = list_form,
    alert = alert)
