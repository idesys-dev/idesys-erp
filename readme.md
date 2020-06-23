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

> Need Docker + Docker Compose, make

    sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    service docker restart
    sudo usermod -aG docker $(whoami)
    # Close and open your desktop user session
    sudo service docker start
    # sudo rm -rf /var/lib/docker
    # sudo docker -d --storage-opt dm.basesize=20G
    # sudo service docker stop
    # sudo rm -rf /var/lib/docker
    # sudo bash -c 'install -vm755 <(curl -L https://github.com/docker/machine/releases/download/v0.5.3/docker-machine_linux-amd64) /usr/local/bin/docker-machine'

```sh
    # clone the repository:
    git clone https://github.com/idesys-dev/idesys-erp.git

    make start
    #  get secret with
    make generate-secret

    # open env file and set var
    make restart

```

Visit the development server at https://localhost:5000.


### Tests

Make sure that all your views are tested.

All the test functions are in the `tests` folder. The `conftest.py` define some
usefull helpers, that you use in your test cases.

    make test

### Linter

See http://prospector.landscape.io/en/master/index.html.


    make lint


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


## Google API

Here is the steps that have been done to set up google API:

 - go in the google cloud platform
 - create a project
 - create a service account
 - download the keys
 - enable domain-wide delegation
 - code:
  - get the delegated credentials
  - make the API call
