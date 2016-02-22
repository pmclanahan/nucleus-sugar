#!/bin/sh

venv/bin/urlwait
./bin/run-common.sh
venv/bin/python manage.py runserver 0.0.0.0:8000
