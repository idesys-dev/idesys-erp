import os
import tempfile

import pytest
from flask_login import login_user, current_user

from app import create_app
from auth.models.user import User


@pytest.fixture
def app():
    app = create_app('test_config.py')
    test_user = User.objects(email='test@idesys.org').first()
    if test_user is None:
        test_user = User(email='test@idesys.org', name='test', google_id='test_google_id')
    test_user.save()

    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def authenticated_request(app):
    with app.test_request_context():
        # Here we're not overloading the login manager, we're just directly logging in a user
        # with whatever parameters we want. The user should only be logged in for the test,
        # so you're not polluting the other tests.
        test_user = User(email='test@idesys.org', name='test', google_id='test_google_id')
        yield login_user(test_user)
