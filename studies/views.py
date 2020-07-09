from flask import Blueprint, request, render_template, url_for, redirect
from flask_login import current_user

from studies.forms import TypeCreate, ProspectChoice, CreateStudy
from models import organisme

from models.etude import Etude

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
        org = organisme.Organisme(
        name = form.structureName.data,
        adresse = form.adresse.data,
        city = form.city.data,
        postalCode = form.postalCode.data)
        print(org)
        org.save()
    return render_template('createStudy.html', form=form)

@studies_bp.route('/prospect', methods=['GET', 'POST'])
def prospect():
    form = ProspectChoice(request.form)
    return render_template('createStudy.html', form=form)

#Tableau de bord des études 
@studies_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html',etude=Etude.objects)
