# IdéSYS-ERP

> IdéSYS-ERP website

*Using Flask only*


## Development

The code is splited with modules:

 - `auth`
 - `documents`

In these folders, there are at least:
 - a `templates` folder
 - a `models` folder
 - a `views.py` file

There can be:
 - a `forms.py` file, where you define the forms
 - a `static` folder, where you write js or css code specific to that module

### Getting started

clone the repository:

    git clone https://github.com/idesys-dev/idesys-erp.git
    cd idesys-erp
    pip3 install -r dev-requirements.txt
    pre-commit install

Generate the secret key with:

    import secrets
    secrets.token_hex(16)

Run:

    export FLASK_ENV=development
    export FLASK_SECRET_KEY=x
    export GOOGLE_CLIENT_ID=x
    export GOOGLE_CLIENT_SECRET=x
    export GOOGLE_SERVICE_ACCOUNT_INFO={}
    export MONGODB_URI=x
    export SLACK_BOT_TOKEN=x

    python3 app.py

### Tests

Make sure that all your views are tested.

All the test functions are in the `tests` folder. The `conftest.py` define some
usefull helpers, that you use in your test cases.

    pytest -v

### Linter

See http://prospector.landscape.io/en/master/index.html.

    prospector


## TODO

 - Write some tests
 - Set up test coverage
 - POC: electronic signature
 - POC: grab mails
 - Get the document templates from google drive


## Deployment

In the branch named `deploy`, commit your changes and run `git push heroku deploy:master`.

In the heroku panel, set all the enviromnent variables.

To rebuild on heroku, push an empty commit with `git commit --allow-empty -m "Re-build"`.

If you want to clean the cache: `heroku repo:purge_cache -a idesys-erp`.
