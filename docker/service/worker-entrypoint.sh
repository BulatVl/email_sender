#!/bin/sh

until cd /app/service
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A service worker --loglevel=info --concurrency 1 -E