
import pytest
from flask_login import login_user
from flask import make_response

from app import create_app
from auth.models.user import User


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    app.config['DEVELOPMENT'] = True
    test_user = User.objects(email='test@idesys.org').first()
    if test_user is None:
        test_user = User(email='test@idesys.org', name='test',
            google_id='test_google_id')
    test_user.save()

    # pylint: disable=unused-variable
    @app.route('/test/login', methods=['POST'])
    def test_login():
        response = make_response()
        login_user(test_user)
        return response
    # pylint: enable=unused-variable

    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def authenticated_request(app, client):
    with app.test_request_context():
        client.post("/test/login")
