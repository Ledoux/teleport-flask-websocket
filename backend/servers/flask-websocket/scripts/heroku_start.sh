#!/bin/sh
gunicorn --config config/heroku_guwsgi.ini app:app
