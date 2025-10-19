#!/usr/bin/env/bash

set -o errexit

pip install  -r requirements.txt

python manage.py collectstaic --no input

python manage.py migrate