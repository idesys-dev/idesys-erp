# See https://flask-admin.readthedocs.io/en/latest/introduction/#getting-started

from flask import redirect, url_for, request
from flask_admin import Admin
from flask_admin.contrib.mongoengine import ModelView
from flask_login import current_user

from auth.models import user
from documents.models import document

class BaseAdminView(ModelView):
    """Base class for admin views.
    Restrict access to authenticated users.
    """
    # WARNING: VERY IMPORTANT: only authenticated users can access the admin panel!!!
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth_bp.login', next=request.url))

class UserAdminView(BaseAdminView):
    can_create = False

def create_admin(app):
    # WARNING: only use UserAdminView to add a view
    admin = Admin(app, name='IdéSYS-ERP Admin', template_mode='bootstrap3')
    admin.add_view(BaseAdminView(document.Document))
    admin.add_view(UserAdminView(user.User))
