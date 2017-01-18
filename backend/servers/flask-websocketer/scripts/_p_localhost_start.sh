#!/bin/sh
if [ -d "../../../$(project.config.venv)" ] ; then
  source ../../../$(project.config.venv)/bin/activate
fi
if [ "$MODE" != "localhost" ] ; then
  $(manageExtraConfig) gunicorn -H ../../../$(project.config.venv)  --config config/localhost_guwsgi.ini app:app
else
  $(manageExtraConfig) python scripts/manage.py
fi
