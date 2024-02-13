#!/bin/sh

until cd /app/service
do
    echo "Waiting for server volume..."
done


#echo 'Waiting for postgres...'
#
#while ! nc -z $DB_HOSTNAME $DB_PORT; do
#    sleep 0.1
#done
#
#echo 'PostgreSQL started'


python manage.py makemigrations


python manage.py migrate


python manage.py collectstatic --noinput

# python manage.py createsuperuser --noinput

gunicorn service.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

# for debug
#python manage.py runserver 0.0.0.0:8000