#!/bin/bash
python manage.py migrate --check
status=$?
if [[ $status != 0 ]]; then
  python manage.py flush --no-input
  python manage.py migrate
fi
exec "$@"
