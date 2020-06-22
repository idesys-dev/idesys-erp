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

Run:

    export FLASK_ENV=development
    export SECRET_KEY=x
    export GOOGLE_CLIENT_ID=x
    export GOOGLE_CLIENT_SECRET=x
    export MONGODB_URI=x
    export SLACK_TOKEN=x
    export GOOGLE_SERVICE_ACCOUNT_INFO={}
    python3 app.py


Generate the secret key with:

    import secrets
    secrets.token_hex(16)


### Tests

Make sure that all your views are tested.

All the test functions are in the `tests` folder. The `conftest.py` define some
usefull helpers, that you use in your test cases.

    pytest -v


## Deployment

In the branch named `deploy`, commit your changes and run `git push heroku deploy:master`.

In the heroku panel, set all the enviromnent variables.

## TODO

 - Set up prospector
 - Write some tests
 - Set up test coverage
