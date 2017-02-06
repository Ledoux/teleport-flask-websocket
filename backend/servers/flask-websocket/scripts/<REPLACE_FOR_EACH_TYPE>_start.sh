#!/bin/sh
$[manageExtraConfig] export URL=$[run.url] && gunicorn --config config/$[type.name]_guwsgi.ini app:app
