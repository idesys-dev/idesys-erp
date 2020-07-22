from flask import Blueprint, request, render_template, url_for, redirect
from flask_login import current_user

from studies.forms import TypeCreate, ProspectChoice, CreateStudy, CreateProspect, Labels, CreateContact
from models import organization, study, contact

studies_bp = Blueprint('studies_bp', __name__, template_folder='templates')

@studies_bp.before_request
def restrict_bp_to_admins():
    if not current_user.is_authenticated:
        return redirect(url_for('auth_bp.login'))
    return None

@studies_bp.route('/create-study', methods=['GET', 'POST'])
def createStudy():
    # We declare all forms we describe in the forms.py
    formCreateStudy = CreateStudy(request.form)
    formSubmit = TypeCreate(request.form)
    formProspectChoice = ProspectChoice(request.form)
    formLabel = Labels(request.form)

    if request.method == 'POST':
        if request.form['btn'] == 'Valider' and formSubmit.structure_save.data == 'Non':
            # If the prospect doesn't exist, we create it
            return redirect(url_for(".createProspect"))

        if request.form['btn'] ==  'Enregistrer':
            etu = study.Study(
                number = 1,
                organisme = formProspectChoice.prospect_choice.data,
                name = formCreateStudy.study_name.data,
                follower_quality = formCreateStudy.follower_quality.data,
                follower_study = formCreateStudy.follower_study.data,
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
def createProspect():
    formCreateProspect = CreateProspect(request.form)
    formCreateContact = CreateContact(request.form)

    if request.method == 'POST':
        if request.form['btn'] ==  'Enregistrer':
            org = organization.Organization(
                name = formCreateProspect.structure_name.data,
                type_structure = formCreateProspect.structure_type.data,
                adresse = formCreateProspect.adresse.data,
                city = formCreateProspect.city.data,
                postal_code = formCreateProspect.postal_code.data,
                sector = formCreateProspect.sector.data )
            org.save()

            cont = contact.Contact(
                id_organisme = org,
                first_name = formCreateContact.first_name.data,
                name = formCreateContact.name.data,
                job = formCreateContact.position.data,
                email = formCreateContact.email.data,
                phone = formCreateContact.phone.data )
            cont.save()

            return redirect(url_for(".createStudy"))

    return render_template('createProspect.html',
    formCreateProspect=formCreateProspect,
    formCreateContact=formCreateContact )

@studies_bp.route('/recap-study', methods=['GET', 'POST'])
def recapStudy():
    
    return render_template('recapStudy.html')
