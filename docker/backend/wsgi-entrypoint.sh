#!/bin/sh


until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

python manage.py compilemessages
python manage.py collectstatic --noinput
python manage.py createsuperuser --noinput

gunicorn src.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4 --capture-output
