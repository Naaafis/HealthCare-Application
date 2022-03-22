#!/bin/sh
export FLASK_APP=./threadsAPI/index.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0