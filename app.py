# Python standard libraries
import os
from dotenv import load_dotenv
# Third-party libraries
from flask import Flask, render_template
from flask_login import LoginManager, login_required
from flask_mongoengine import MongoEngine

# Internal imports
import models as mo
from models.seeder import starter_db

def create_app(config_filename=None):
    load_dotenv()
    # Flask app setup
    app = Flask(__name__)
    if config_filename is None:
        app.config['MONGODB_SETTINGS'] = {
            'host': os.environ['MONGODB_URI']
        }
        app.config['SECRET_KEY'] = os.environ['FLASK_SECRET_KEY']
        app.config['SLACK_BOT_TOKEN'] = os.environ['SLACK_BOT_TOKEN']
        app.config['GOOGLE_CLIENT_SECRET'] = os.environ['GOOGLE_CLIENT_SECRET']
        app.config['GOOGLE_CLIENT_ID'] = os.environ['GOOGLE_CLIENT_ID']
    else:
        app.config.from_pyfile(config_filename)

    MongoEngine(app)
   

    with app.app_context():
        from auth.views import auth_blueprint
        from documents.views import documents_bp
        from studies.views import studies_bp
    from models.user import User
    from admin import create_admin

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(documents_bp, url_prefix='/documents')
    app.register_blueprint(studies_bp, url_prefix='/etudes')

    # User session management setup
    # https://flask-login.readthedocs.io/en/latest
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth_bp.login'

    create_admin(app)

    #Launch seeder
    if app.config['FLASK_ENV'] == 'development':
        starter_db()

    # pylint: disable=unused-variable
    # Flask-Login helper to retrieve a user from our db
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    @app.route("/")
    @login_required
    def index():
        return render_template('pages/index.html')
    # pylint: enable=unused-variable

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host=os.environ['FLASK_RUN_HOST'], ssl_context='adhoc')