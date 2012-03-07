#!/bin/bash

python manage.py reset_db --router=default
python manage.py syncdb --noinput
python manage.py createsuperuser --username=root --email=root@root.com
