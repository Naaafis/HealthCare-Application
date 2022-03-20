#!/bin/sh
export FLASK_APP=./threads/index.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0