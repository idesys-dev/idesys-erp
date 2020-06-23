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
clone the repository:
```sh
    git clone https://github.com/idesys-dev/idesys-erp.git

    make start
    #  get secret with
    make generate-secret

    # open env file and set var
    make restart

```



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
