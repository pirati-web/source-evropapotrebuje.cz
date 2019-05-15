#!/bin/bash

if [[ "x$1" == "x+" ]]; then
  python3 ./manage.py runserver_plus 127.0.0.1:8011
else
  python3 ./manage.py runserver --insecure 127.0.0.1:8011
fi
