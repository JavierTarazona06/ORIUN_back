# ORIUN Backend

ORIUN is a Django REST API for managing academic exchange calls, student applications, application documents, reports, and traceability for the Office of Interinstitutional Relations at Universidad Nacional de Colombia.

This repository is backend-only. The previously hosted demo site is not the source of truth anymore; the project now ships with a self-contained local Docker environment so reviewers and contributors can run the API without external services.

## Features

- JWT authentication for students and administrative staff.
- CRUD workflows for exchange calls, universities, students, employees, and applications.
- Student eligibility checks for academic exchange calls.
- Application document upload, download, validation, and generated form support.
- Reports and ordering helpers for applications, winners, historical data, and population statistics.
- Local demo mode with seeded users, seeded calls, PostgreSQL, local file storage, and console email output.

## Architecture

- **Framework:** Django 5 and Django REST Framework.
- **Database:** PostgreSQL in Docker Compose. SQLite is available only as a lightweight fallback when no database environment variables are set.
- **Authentication:** Simple JWT.
- **Storage:** Local filesystem by default for Docker development; Google Cloud Storage can be enabled for production.
- **Email:** Console output by default for Docker development; SMTP can be enabled for production.

## Quick Start With Docker

Requirements:

- Docker
- Docker Compose v2

Run the API:

```bash
git clone https://github.com/JavierTarazona06/ORIUN_back.git
cd ORIUN_back
docker compose up --build
```

The API will be available at:

```text
http://localhost:8080
```

On first startup, the container waits for PostgreSQL, runs migrations, loads demo data, creates guest users, and starts Django.

Useful local endpoints:

```text
GET http://localhost:8080/
GET http://localhost:8080/health/
POST http://localhost:8080/api-token/
POST http://localhost:8080/api-token/refresh/
```

## Guest Credentials

Use these accounts after `docker compose up --build` finishes:

| Role | Username | Password |
| --- | --- | --- |
| Student | `guest.student@unal.edu.co` | `GuestStudent123!` |
| Employee | `guest.employee@unal.edu.co` | `GuestEmployee123!` |
| Local admin | `admin@oriun.local` | `Admin123!` |

The local admin is created only when `ORIUN_CREATE_DEMO_ADMIN=true`, which is enabled in `docker-compose.yml`.

## JWT Login Example

```bash
curl -X POST http://localhost:8080/api-token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"guest.student@unal.edu.co","password":"GuestStudent123!"}'
```

Use the returned `access` token as a bearer token:

```bash
curl http://localhost:8080/student/eligible/?call=1 \
  -H "Authorization: Bearer <access-token>"
```

## Local Development Commands

Run Django checks:

```bash
docker compose exec web python manage.py check
```

Run tests:

```bash
docker compose exec web python manage.py test --noinput
```

Open a shell in the API container:

```bash
docker compose exec web sh
```

Reset the local Docker database and storage:

```bash
docker compose down -v
docker compose up --build
```

## Environment Variables

Docker Compose already provides working local defaults. Copy `.env.example` to `.env` only when you want to override values.

| Variable | Local default | Purpose |
| --- | --- | --- |
| `ORIUN_DEBUG` | `true` | Docker Compose override mapped to Django `DEBUG`. Set to `false` in production. |
| `DJANGO_SECRET_KEY` | Local unsafe key | Django secret key. Must be replaced in production. |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1,0.0.0.0,web` | Hosts accepted by Django. |
| `DATABASE_ENGINE` | `django.db.backends.postgresql` | Database backend used by Docker. |
| `DATABASE_NAME` | `oriun` | PostgreSQL database name. |
| `DATABASE_USER` | `oriun` | PostgreSQL user. |
| `DATABASE_PASSWORD` | `oriun` | PostgreSQL password. |
| `DATABASE_HOST` | `db` | Docker Compose PostgreSQL service name. |
| `DATABASE_PORT` | `5432` | PostgreSQL port. |
| `STORAGE_BACKEND` | `local` | Use `local` for filesystem storage or `gcs` for Google Cloud Storage. |
| `LOCAL_STORAGE_ROOT` | `/app/django_project/data/local_storage` | Local document storage path inside the container. |
| `ORIUN_FRONTEND_URL` | `http://localhost:8080` | URL used in generated email/footer links. |
| `ORIUN_MAIL_BACKEND` | `console` | Use `console` locally or `smtp` in production. |
| `ORIUN_BOOTSTRAP_DEMO_DATA` | `true` | Loads demo data and guest users during Docker startup. |
| `ORIUN_CREATE_DEMO_ADMIN` | `true` | Creates the local admin user during Docker startup. |
| `GOOGLE_APPLICATION_CREDENTIALS` | Empty | Required only when `STORAGE_BACKEND=gcs`. |
| `MAIL_PASSWORD` | Empty | Required only when `ORIUN_MAIL_BACKEND=smtp`. |

## Local Storage Mode

The default Docker setup does not require Google Cloud credentials. Uploaded files and generated forms are stored in the `oriun_local_storage` Docker volume and served under:

```text
http://localhost:8080/local-storage/
```

This route is enabled only when `STORAGE_BACKEND=local`.

## Production Notes

Before deploying this backend outside local development:

- Set `ORIUN_DEBUG=false` in Docker Compose, or `DEBUG=false` in a non-Compose runtime.
- Use a strong `DJANGO_SECRET_KEY`.
- Set precise `ALLOWED_HOSTS` and CORS origins.
- Use real database credentials.
- Set `ORIUN_BOOTSTRAP_DEMO_DATA=false`.
- Set `ORIUN_CREATE_DEMO_ADMIN=false`.
- Use `STORAGE_BACKEND=gcs` with a valid service account if documents must live in Google Cloud Storage.
- Use `ORIUN_MAIL_BACKEND=smtp` with valid SMTP credentials if the system must send real email.

## Troubleshooting

If the API does not start, check logs:

```bash
docker compose logs -f web
```

If PostgreSQL or demo data looks stale, reset volumes:

```bash
docker compose down -v
docker compose up --build
```

If port `8080` is already in use, change the port mapping in `docker-compose.yml`.
