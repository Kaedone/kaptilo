#!/usr/bin/env bash

args=("$@")

case "${1}" in
    "bash")
        shift
        exec bash -c "${args[@]:1}"
        ;;
    "sleep")
        exec bash -c "while true; do sleep 2; done"
        ;;
    "migrate")
        ./manage.py migrate
        ;;
    "collectstatic")
        ./manage.py collectstatic --noinput
        ;;
    "run")
        ./wait-for-it.sh pg:5432 --timeout=30 --strict -- echo "Postgres is up"
        exec gunicorn project.wsgi:application -w 4 --log-level=info --bind=0.0.0.0:8000
        ;;
esac
