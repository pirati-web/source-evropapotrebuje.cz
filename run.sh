#!/bin/bash

if [[ "x$1" == "x+" ]]; then
  ./manage.py runserver_plus 127.0.0.1:8011
else
  ./manage.py runserver --insecure 127.0.0.1:8011
fi
