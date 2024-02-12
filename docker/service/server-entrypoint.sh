#!/bin/sh

until cd /app/service
do
    echo "Waiting for server volume..."
done


until python manage.py makemigrations
do
    echo "Waiting for db to be ready..."
done


until python manage.py migrate
do
    echo "Waiting for db to be ready..."
done


python manage.py collectstatic --noinput

# python manage.py createsuperuser --noinput

gunicorn service.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

# for debug
#python manage.py runserver 0.0.0.0:8000