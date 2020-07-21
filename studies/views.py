from flask import Blueprint, request, render_template, url_for, redirect
from flask_login import current_user

from studies.forms import TypeCreate, ProspectChoice, CreateStudy, CreateProspect, Labels, CreateContact
import models as mo

studies_bp = Blueprint('studies_bp', __name__, template_folder='templates')

@studies_bp.before_request
def restrict_bp_to_admins():
    if not current_user.is_authenticated:
        return redirect(url_for('auth_bp.login'))
    return None

@studies_bp.route('/create', methods=['GET', 'POST'])
def create():
    form = TypeCreate(request.form)
    if request.method == 'POST'and form.validate():
        if form.structureSave.data == 'Non':
            return redirect(url_for('.nouveau'))

        return redirect(url_for('.prospect'))

    return render_template('createStudy.html', form=form)

@studies_bp.route('/nouveau', methods=['GET', 'POST'])
def nouveau():
    form = CreateStudy(request.form)
    if request.method == 'POST' and form.validate():
        org = mo.organization.Organization(
            name = form.structureName.data,
            adress = form.adresse.data,
            city = form.city.data,
            postal_code = form.postalCode.data
            )
        print(org)
        org.save()
    return render_template('createStudy.html', form=form)

@studies_bp.route('/prospect', methods=['GET', 'POST'])
def prospect():
    form = ProspectChoice(request.form)
    return render_template('createStudy.html', form=form)

#Study dashboard
#Tabs
@studies_bp.route('/dashboard', methods=['GET', 'POST'])
@studies_bp.route('/dashboard?tab=<string:tab>', methods=['GET', 'POST'])
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
        title = "Terminées"

    elif tab == 'failed':
        title = "Avortées"
    else :
        title = "Error 404 : tab not found"    
    
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
        if id_study == '':
            return "Id non valide"

        sty = mo.study.Study.get(id_study)

        for i in sty.list_phases:
            total_price += i.price_jeh * i.nb_jeh
            tot_jeh += i.nb_jeh
        
        return {"price":total_price, 
                "tot_jeh": tot_jeh}

    return dict(get_info=get_info)


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
            etu = mo.study.Study(
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
            org = mo.organization.Organization(
                name = formCreateProspect.structure_name.data,
                type_structure = formCreateProspect.structure_type.data,
                adresse = formCreateProspect.adresse.data,
                city = formCreateProspect.city.data,
                postal_code = formCreateProspect.postal_code.data,
                sector = formCreateProspect.sector.data )
            org.save()

            cont = mo.contact.Contact(
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
