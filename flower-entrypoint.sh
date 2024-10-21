#!/bin/bash

set -o errexit
set -o nounset

celery_worker_ready() {
    celery -A config inspect ping
}

until celery_worker_ready; do
  >&2 echo 'Celery worker is still not ready'
  sleep 1
done
>&2 echo 'Celery worker is ready'

celery -A config --broker="${REDIS_CONNECTION}" flower
