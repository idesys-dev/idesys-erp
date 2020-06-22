from flask import Blueprint, request, render_template, g, url_for, redirect
from flask_login import login_required, current_user

from .document_rendering.render_document import render_document
from documents import forms

documents_bp = Blueprint('documents_bp', __name__, template_folder='templates')

@documents_bp.before_request
def restrict_bp_to_admins():
    if not current_user.is_authenticated:
        return redirect(url_for('auth_bp.login'))

@documents_bp.route('/rm', methods=['GET', 'POST'])
def rm():
    form = forms.GenerateRM(request.form)
    if request.method == 'POST' and form.validate():

        data = {
            'consultant_name': form.consultant_name.data
        }
        link = render_document('rm', 'docx', data, form.ref.data)
    else:
        link = None

    return render_template('documents.html', form=form, link=link, _type="RM")

@documents_bp.route('/bv', methods=['GET', 'POST'])
def bv():
    form = forms.GenerateBV(request.form)
    if request.method == 'POST' and form.validate():

        data = {
            'pay': str(form.pay.data).replace('.', ','),
            'jeh': str(form.jeh.data).replace('.', ',')
        }
        link = render_document('bv', 'xlsx', data, form.ref.data)
    else:
        link = None

    return render_template('documents.html', form=form, link=link, _type="BV")

@documents_bp.route('/pp', methods=['GET', 'POST'])
def pp():
    form = forms.GeneratePP(request.form)
    if request.method == 'POST' and form.validate():

        data = {
            "model": {
                'client_name': form.client_name.data
            }
        }
        link = render_document('pp', 'pptx', data, form.ref.data)
    else:
        link = None

    return render_template('documents.html', form=form, link=link, _type="Propale")


# Legacy code: from the previous Rest API for IdéSYS-ERP:

# @documents_bp.route('/documents/<_type>', methods=['GET'])
# def documents(_type):
#     docs = Document.objects(_type=_type)
#     return render_template('documents.html', docs)
#
#
# @documents_bp.route('/documents/validate', methods=['PUT'])
# def validate():
#     post_data = request.get_json()
#     doc_id = post_data['id']
#     doc = Document.get_document_by_id(doc_id)
#     if g.user.can_validate:
#         doc.status = "validated"
#         doc.save()
#         response_object = {
#             'ok': True,
#             'data': {
#                 'document': doc,
#             }
#         }
#         return make_response(jsonify(response_object))
#     response_object = {
#         'ok': False,
#         'error': "User can't validate document"
#     }
#     return make_response(jsonify(response_object), 403)
