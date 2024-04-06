ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Copy local code to container
WORKDIR /app
COPY . /app

# Install dependencies
# RUN apt update && apt install libpq-dev -y
RUN pip3 install --no-cache-dir -r requirements.txt && pip3 cache purge

# Expose the port that the application listens on.
EXPOSE 8080

# Run the application.
CMD python django_project/manage.py runserver 0.0.0.0:8080 --noreload