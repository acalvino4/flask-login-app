This project provides a skeleton for a flask app that needs login capability. Feel free to clone and use for your projects.

## Running locally

This skeleton uses pipenv to manage your python environment and dependencies, so to use, you will have to [install pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today).

```bash
git clone https://github.com/acalvino4/flask-login-app.git
pipenv install
```

Because flask will then be installed only within your virtual environment, you won't be able to `flask run` from the command line (unless you configure your IDE to set your interpreter to that of the environment). Instead, run such commands through pipenv:
```bash
pipenv run flask run
```
or set shortcut scripts in `Pipfile` such as `dev = "flask run"` so you can just type
```bash
pipenv run dev
```

From there, modify any files as needed for your app!
