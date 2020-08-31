from flask import Blueprint, render_template, url_for, redirect
from flask_login import current_user

from models.organization import Organization
from models.mail import Mail
from external_apis.gsuite_api import credentials, gmail

organizations_bp = Blueprint('organizations_bp', __name__,
    template_folder='templates')

@organizations_bp.before_request
def restrict_bp_to_admins():
    if not current_user.is_authenticated:
        return redirect(url_for('auth_bp.login'))
    return None

@organizations_bp.route('/', methods=['GET'])
def list_organization():
    organisations = Organization.objects
    return render_template('list-organization.html',
        organisations=organisations)

@organizations_bp.route('/fetch-emails', methods=['GET'])
def fetch_emails():
    scopes = ['https://www.googleapis.com/auth/gmail.readonly']
    creds = credentials.get_delegated_credentials(scopes, current_user.email)
    messages_body, gmail_history_id = gmail.get_mails(creds,
        Organization.get_all_mails_contact(), current_user.gmail_history_id)
    for message in messages_body:
        for organization in Organization.objects:
            for contact in organization.list_contacts:
                if contact.email in message['mail_to_keep']:
                    mail = Mail.create_mail_instance(message, current_user.id)
                    mail.save()
                    contact.mails.append(mail.id)
                    organization.save()
    if gmail_history_id != -1:
        current_user.gmail_history_id = gmail_history_id
        current_user.save()

    return redirect(url_for('.list_organization'))
