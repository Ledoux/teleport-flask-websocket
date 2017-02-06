#!/bin/sh
if [ "$VIRTUAL_ENV" != "" ] ; then
  VIRTUAL_ENV_OPTION="-H $VIRTUAL_ENV"
else
  VIRTUAL_ENV_OPTION=""
fi
if [ "$MODE" != "localhost" ] ; then
  $[manageExtraConfig] export URL=$[run.url] && gunicorn $VIRTUAL_ENV_OPTION --config config/localhost_guwsgi.ini app:app
else
  $[manageExtraConfig] export URL=$[run.url] && python scripts/manage.py
fi
