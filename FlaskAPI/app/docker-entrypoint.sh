#!/bin/sh
set -e
flask db migrate 
flask db upgrade
# run tests
python app/test_api.py
# bind to 5000 port
gunicorn  --bind=0.0.0.0:5000 app.main:app 