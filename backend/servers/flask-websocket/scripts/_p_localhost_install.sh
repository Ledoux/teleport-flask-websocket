#!/bin/sh
if [ -d "../../../$(project.config.venv)" ] ; then
  source ../../../$(project.config.venv)/bin/activate
fi
sh scripts/install.sh
