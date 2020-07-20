from flask import Blueprint, request, render_template, url_for, redirect
from flask_login import current_user

from studies.forms import TypeCreate, ProspectChoice, CreateStudy
from models import organization, labels, study 

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
    if request.method == 'POST'and form.validate():
        org = organization.Organization(
        name = form.structureName.data,
        adress = form.adresse.data,
        city = form.city.data,
        postal_code = form.postalCode.data)
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
    listCategory = []
    for i in labels.Labels.objects :
        if i.category not in listCategory :
            listCategory.append(i.category)

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
            study=study.Study.objects,
            labels=labels.Labels.objects,
            listCategory=listCategory,
            title=title,
            tab=tab )


@studies_bp.context_processor
def utility_processor():
    def get_info(id_study):
        total_price = 0
        tot_jeh = 0
        if id_study == '':
            return "Id non valide"

        sty = study.Study.get(id_study)

        for i in sty.list_phases:
            total_price += i.price_jeh * i.nb_jeh
            tot_jeh += i.nb_jeh
        
        return {"price":total_price, 
                "tot_jeh": tot_jeh}

    return dict(get_info=get_info)