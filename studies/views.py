import base64 as b64
import json
from urllib.parse import urlparse
from os.path import basename
import os

from flask import Blueprint, request, render_template, url_for, redirect, flash

from flask_login import current_user

#Import for jeh -> phase
from studies.forms import CreatePhases, TypeCreate, ProspectChoice, CreateStudy, CreateProspect, CreateContact, LabelsForm
import models as mo

#pylint: disable=too-many-statements
#pylint: disable=too-many-locals

from models.contact import Contact
from models.company import Company

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

    def check_number_phase(list_phases):
        error = False
        list_number = []
        for i in list_phases:
            list_number.append(i.phase_number)

        num = 1
        while num < len(list_phases)+1 :
            if num not in list_number:
                error = True
            num +=1
        return error

    return dict(get_info=get_info, check_number_phase = check_number_phase)

@studies_bp.route('/create-study', methods=['GET', 'POST'])
def create_study():
    # We declare all forms we describe in the forms.py
    formLabel = LabelsForm(request.form)
    formCreateStudy = CreateStudy(request.form)
    formSubmit = TypeCreate(request.form)


    #Edit prospect
    list_prospect = Contact.get_all()
    formProspectChoice = ProspectChoice(request.form, obj=list_prospect)
    formProspectChoice.prospect_choice.choices = [(g.id, g.get_name()) for g in list_prospect]


    if request.method == 'POST':
        if request.form['btn'] == 'Valider' and formSubmit.structure_save.data == 'Non':
            # If the prospect doesn't exist, we create it
            return redirect(url_for(".create_prospect"))

        if request.form['btn'] ==  'Enregistrer':
            etu = mo.study.Study(
                number = 12, #change needed
                name = formCreateStudy.study_name.data,
                id_hubspot = formProspectChoice.prospect_choice.data,
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

#Study - Phases
@studies_bp.route('/<num_study>/phases', methods=['GET', 'POST'])
def phases(num_study=None):
    study = mo.study.Study.objects(number=num_study).first()

    #Form to create new phases
    form_create_phase = CreatePhases()

    #Sort phases by phase_number attribute
    study.list_phases.sort( key = lambda x : x.phase_number)

    #Initiate forms to edit phases
    list_form = []
    for i in study.list_phases :
        form = CreatePhases()
        list_form.append(form)


    #Forms to edit phases
    if request.method == 'GET':
        for j in range(len(study.list_phases)) :
            i = study.list_phases[j]
            form = list_form[j]

            form.name.data = i.name
            form.description.data = i.description
            form.lenght_week.data = i.lenght_week
            form.nb_jeh.data = i.nb_jeh
            form.price_jeh.data = i.price_jeh
            form.phase_number.data = i.phase_number
            form.control_point.data = i.control_point
            form.bill.data = i.bill



    if request.method == 'POST':

        #Request to create a phase
        if request.form['btn'] ==  'Enregistrer':
            if form_create_phase.validate_on_submit():
                phs = mo.phases.Phases(
                    name = form_create_phase.name.data,
                    description = form_create_phase.description.data,
                    lenght_week = form_create_phase.lenght_week.data,
                    nb_jeh = form_create_phase.nb_jeh.data,
                    price_jeh = form_create_phase.price_jeh.data,
                    phase_number = form_create_phase.phase_number.data,
                    control_point = form_create_phase.control_point.data,
                    bill = form_create_phase.bill.data,
                    ).save()
                #add link to mission
                study.list_phases.append(phs.id)
                study.save()

                flash("Phase created !")
            else:
                flash("Impossible to create phase, wrong data")

            return redirect(url_for('studies_bp.phases', num_study = study.number))

        #Request to delete a phase
        if request.form['btn'] ==  'Supprimer':
            id_delete = request.form['hidden']
            phs_del = mo.phases.Phases.get(id_delete)
            study.list_phases.remove(phs_del)
            study.save()
            phs_del.delete()

            return redirect(url_for('studies_bp.phases', num_study = study.number))

        #Request to edit a phase
        if request.form['btn'] ==  'Modifier':
            id_edit = request.form['hidden2']
            phs_edit = mo.phases.Phases.get(id_edit)
            form = list_form[int(request.form['hidden3'])]

            if form.validate_on_submit():
                phs_edit.name = form.name.data
                phs_edit.description = form.description.data
                phs_edit.lenght_week = form.lenght_week.data
                phs_edit.nb_jeh = form.nb_jeh.data
                phs_edit.price_jeh = form.price_jeh.data
                phs_edit.phase_number = form.phase_number.data
                phs_edit.control_point = form.control_point.data
                phs_edit.bill = form.bill.data

                phs_edit.save()
                flash("Phase edited !")

            else:
                flash("Impossible to edit phase, wrong data")

            return redirect(url_for('studies_bp.phases', num_study = study.number))

        #Request to add a JEH Maker link
        if request.form['btn'] ==  'Ajouter JEH':
            link = request.form['link-jeh']
            study.link_jeh = link
            study.save()

            #JSON from JEh
            obj = jeh_link_to_json(link)
            list_phase_json = obj['phases']

            #Drop current phase
            for phase in study.list_phases :
                phase.delete()

            study.list_phases = []

            #Create new phases
            for i in list_phase_json :
                phs = mo.phases.Phases(
                    phase_number = i["id"],
                    name = i["title"],
                    nb_jeh = i["nbJeh"],
                    price_jeh = i["jeh"],
                    lenght_week = 1
                ).save()

                study.list_phases.append(phs)
                study.save()

            return redirect(url_for('studies_bp.phases', num_study = study.number))


    return render_template('phases.html', study = study,
                        form_create_phase = form_create_phase,
                        list_form = list_form )

#Convert JEH Maker link to json objects
def jeh_link_to_json(link_jeh):
    #First clean up link
    code_b64 = basename(urlparse(link_jeh).fragment)

    #Then decode and convert
    obj = json.loads(b64.b64decode(code_b64))
    return obj

@studies_bp.route('/<num_study>/summary/<vision>', methods=['GET', 'POST'])
def summary_study(num_study=None, vision="planning"):
    study = mo.study.Study.objects(number=num_study).first()

    contact = Contact.get(study.id_hubspot)

    if contact.company_id:
        company = Company.get(contact.company_id)
    else:
        company = Company("00", "")
    return render_template('recapStudy.html', study=study, vision=vision, contact=contact, company=company, hubspot_id=os.environ['HUBSPOT_ID'])
