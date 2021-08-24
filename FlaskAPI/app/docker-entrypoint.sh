#!/bin/sh
set -e
# flask initdb
# bind to 5000 port
gunicorn  --bind=0.0.0.0:5000 app.main:app 