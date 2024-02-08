#!/bin/sh

until cd /app/service
do
    echo "Waiting for server volume..."
done

celery -A service beat --loglevel=INFO