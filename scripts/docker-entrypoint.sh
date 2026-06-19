#!/bin/sh
set -e

cd /app/django_project

if [ "${DATABASE_ENGINE:-}" = "django.db.backends.postgresql" ]; then
  python - <<'PY'
import os
import socket
import time

host = os.getenv("DATABASE_HOST", "db")
port = int(os.getenv("DATABASE_PORT", "5432"))
deadline = time.time() + int(os.getenv("DATABASE_WAIT_TIMEOUT", "60"))

while True:
    try:
        with socket.create_connection((host, port), timeout=2):
            print(f"PostgreSQL is available at {host}:{port}")
            break
    except OSError as exc:
        if time.time() > deadline:
            raise RuntimeError(f"Timed out waiting for PostgreSQL at {host}:{port}") from exc
        print(f"Waiting for PostgreSQL at {host}:{port}...")
        time.sleep(2)
PY
fi

python manage.py migrate --noinput

if [ "${ORIUN_BOOTSTRAP_DEMO_DATA:-false}" = "true" ]; then
  python manage.py bootstrap_local --path data/data_csv
fi

exec "$@"
