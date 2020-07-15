from flask import Blueprint, request, render_template, url_for, redirect
from flask_login import current_user

from studies.forms import TypeCreate, ProspectChoice, CreateStudy, CreateProspect, Labels, CreateContact
from models import organisme, etude, contact

studies_bp = Blueprint('studies_bp', __name__, template_folder='templates')

@studies_bp.before_request
def restrict_bp_to_admins():
    if not current_user.is_authenticated:
        return redirect(url_for('auth_bp.login'))
    return None

@studies_bp.route('/consultStudies', methods=['GET', 'POST'])
def consultStudies():
    return render_template('studies.html')

@studies_bp.route('/createStudy', methods=['GET', 'POST'])
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
            etu = etude.Etude(
            number = 1,
            name = formCreateStudy.study_name.data,
            idFollowerQuality = formCreateStudy.follower_quality.data,
            idFollowerStudy = formCreateStudy.follower_study.data,
            description = formCreateStudy.description.data,
            applicationFees = 100,
            state = "Début",
            listLabels = [formLabel.year.data, formLabel.sector.data, formLabel.prospection.data] )
            etu.save()

            return redirect(url_for(".consultStudies"))

        if request.form['btn'] == 'Annuler':
            return redirect(url_for(".consultStudies"))

    # If the prospect already exist, we have to choose it
    return render_template('createStudy.html',
    formCreateStudy=formCreateStudy,
    formLabel=formLabel,
    formSubmit=formSubmit,
    formProspectChoice=formProspectChoice )

@studies_bp.route('/createProspect', methods=['GET', 'POST'])
def createProspect():
    formCreateProspect = CreateProspect(request.form)
    formCreateContact = CreateContact(request.form)

    if request.method == 'POST':
        if request.form['btn'] == 'Annuler':
            return redirect(url_for(".createStudy"))

        org = organisme.Organisme(
        name = formCreateProspect.structure_name.data,
        typeStructure = formCreateProspect.structure_type.data,
        adresse = formCreateProspect.adresse.data,
        city = formCreateProspect.city.data,
        postalCode = formCreateProspect.postal_code.data,
        sector = formCreateProspect.sector.data )
        org.save()

        cont = contact.Contact(
        idOrganisme = org.id,
        firstName = formCreateContact.first_name.data,
        name = formCreateContact.name.data,
        job = formCreateContact.position.data,
        email = formCreateContact.email.data,
        phone = formCreateContact.phone.data )
        cont.save()

        return redirect(url_for(".createStudy"))

    return render_template('createProspect.html',
    formCreateProspect=formCreateProspect,
    formCreateContact=formCreateContact )
