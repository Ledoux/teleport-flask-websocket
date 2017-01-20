#!/bin/sh
gunicorn --config config/$[type.name]_guwsgi.ini app:app
