#!/bin/sh

until cd /app/service
do
    echo "Waiting for server volume..."
done

celery -A service worker --uid=nobody --gid=nogroup --loglevel=info --concurrency 1 -E