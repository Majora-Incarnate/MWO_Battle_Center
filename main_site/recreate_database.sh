#!/bin/bash
rm db.sqlite3
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py loaddata main_data.yaml