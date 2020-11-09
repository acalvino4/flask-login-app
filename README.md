This project provides a skeleton for a flask app that needs login capability. Feel free to clone and modify for your projects.

## Running locally

This skeleton uses pipenv to manage your python environment and dependencies, so to use, you will have to [install pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today).

```bash
git clone https://github.com/acalvino4/flask-login-app.git
pipenv install
```

Because flask will then be installed only within your virtual environment, you won't be able to `flask run` from the command line (unless you configure your IDE to set your interpreter to that of the environment, which is very helpful). Instead, run such commands through pipenv:
```bash
pipenv run flask run
```
or set shortcut scripts in `Pipfile` such as `dev = "flask run"` so you can just type
```bash
pipenv run dev
```

Also, make sure you set the following environment variables. For development, put them in a file called `.env`, which will be automatically loaded, and for production set them on your server.
```bash
FLASK_ENV=your_environment # defaults to production
SQLALCHEMY_DATABASE_URI='db_connection_string'
SECRET_KEY='my_secret_key'
SERVER_NAME='your.dns.name'
```

Make sure you initialize the database schema. I've set up a couple pipenv scripts to help with this:
```
pipenv run migrate
pipenv run upgrade
```
As you modify your schema, you will have to repeat these commands.


From here, modify any files as needed for your app!
