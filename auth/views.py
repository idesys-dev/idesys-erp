# see https://realpython.com/flask-google-login/

import json

from flask import current_app, Blueprint, request, redirect, url_for, render_template, flash

from flask_login import (
    login_required,
    login_user,
    logout_user,
)
import requests
from oauthlib.oauth2 import WebApplicationClient

from auth.models.user import User

GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)
# OAuth 2 client setup
client = WebApplicationClient(current_app.config['GOOGLE_CLIENT_ID'])

# Create the Blueprint
# We set a template_folder, this means that in this Blueprint, the render_template
# function will search for templates in the auth/templates folder
auth_blueprint = Blueprint('auth_bp', __name__, template_folder='templates')


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

@auth_blueprint.route("/login")
def login():
    return render_template('login.html')

@auth_blueprint.route("/google-login")
def google_login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@auth_blueprint.route("/google-login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(current_app.config['GOOGLE_CLIENT_ID'], current_app.config['GOOGLE_CLIENT_SECRET']),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that you have tokens (yay) let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["name"]
    else:
        flash("User email not available or not verified by Google.")
        return redirect(url_for('auth_bp.login'))

    if not users_email.endswith('idesys.org'):
        flash("User email not in GSuite domain.")
        return redirect(url_for('auth_bp.login'))

    user = User.objects(google_id=unique_id).first()
    if not user:
        user = User(
            google_id=unique_id, name=users_name, email=users_email, profile_pic=picture
        )
        user.save()

    # Begin user session by logging the user in
    login_user(user)

    # Send user back to homepage
    return redirect(url_for("index"))

@auth_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@auth_blueprint.route("/user")
@login_required
def user():
    return render_template("user.html")
