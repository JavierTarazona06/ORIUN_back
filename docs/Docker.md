# Docker Setup

The canonical local setup is documented in the root `README.md`.

For a clean local run:

```bash
docker compose up --build
```

The API will be available at:

```text
http://localhost:8080
```

Docker Compose starts PostgreSQL, runs migrations, loads demo data, creates guest users, and uses local filesystem storage. No Google Cloud credentials, SMTP credentials, or external database are required for local evaluation.

Common commands:

```bash
docker compose exec web python manage.py check
docker compose exec web python manage.py test --noinput
docker compose down -v
```

Guest credentials and environment variables are listed in the root `README.md`.
