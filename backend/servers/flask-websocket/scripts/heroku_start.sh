#!/bin/sh
gunicorn --config config/heroku_guwsgi.ini --bind 0.0.0.0:$PORT app:app
