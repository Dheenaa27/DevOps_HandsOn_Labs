# POC 04 — Multi-Container Application with Docker Compose

## Mission Objective

Design, deploy, validate, and troubleshoot a multi-container
Flask and PostgreSQL application using Docker Compose.

Demonstrate service discovery, health-aware startup,
persistent storage, dependency failure isolation,
and controlled recovery.

## Architecture

MacBook / curl
      |
      | localhost:3004
      v
Flask Web Container (web:3000)
      |
      | Docker Compose bridge network
      | db:5432
      v
PostgreSQL Container (db)
      |
      v
Docker Named Volume (poc04_postgres-data)

PostgreSQL is accessible only through the internal
Compose network; its port is not published to the host.

## Technology Stack

- Docker Engine and Docker Compose
- Python 3.12
- Flask 3.1.1
- psycopg 3.2.9
- PostgreSQL 17
- Docker bridge networking
- Docker named volumes
- Git and GitHub

## Project Structure

- app/main.py — Flask application
- requirements.txt — Python dependencies
- Dockerfile — Flask image definition
- .dockerignore — Docker build exclusions
- compose.yaml — Multi-container configuration
- .env.example — Local environment template
- .gitignore — Git exclusions
- screenshots/ — Validation evidence
- troubleshooting.md — Incident and recovery documentation

## Deployment

Copy the example configuration:

    cp .env.example .env

Replace the placeholder password in .env with a unique
local password before the first database initialization.

Validate Compose configuration:

    docker compose config --quiet
    docker compose config --services

Build and deploy:

    docker compose up --build -d

Inspect services:

    docker compose ps

## Application Endpoints

GET / — Application information

GET /health — Flask process responsiveness

GET /db-health — PostgreSQL connectivity validation

Example validation:

    curl -i http://127.0.0.1:3004/health
    curl -i http://127.0.0.1:3004/db-health

Expected: Both endpoints return HTTP 200 when
the application and database are functioning.

## Docker Networking

The Flask application connects to PostgreSQL using
the Compose service hostname db on port 5432.

Service-name resolution avoids dependence on
container IP addresses, which can change.

## Health-Aware Startup

PostgreSQL uses pg_isready as a readiness check.

The web service uses depends_on with
condition: service_healthy.

This coordinates initial startup but does not
guarantee continuous database availability.

## Persistent Storage Experiment

Created the poc04_evidence table and inserted:

    POC04_DATA_PERSISTENCE_TEST

Recreated the PostgreSQL container using:

    docker compose up -d --force-recreate --no-deps db

Queried the database after recreation.

Result: The original record remained available.

The named volume separates persistent database files
from the lifecycle of the database container.

## Failure and Recovery Experiment

Stopped PostgreSQL:

    docker compose stop db

Observed:

- Flask /health returned HTTP 200.
- Flask /db-health returned HTTP 503.
- Application logs reported a database resolution failure.

Recovered PostgreSQL:

    docker compose start db

Validated:

- PostgreSQL returned to healthy status.
- /db-health returned HTTP 200.
- The original SQL record remained available.

See troubleshooting.md for the incident report.

## Evidence

Screenshots 01–13 document environment setup,
application configuration, deployment, health checks,
database connectivity, persistent storage,
failure simulation, recovery, and documentation checks.

## Key Learnings

1. Docker Compose manages multi-container applications.
2. Service names enable internal container discovery.
3. Environment variables separate code from configuration.
4. Health checks help coordinate initial service startup.
5. Named volumes retain data across container recreation.
6. Application health and dependency health are different.
7. Logs support root cause analysis.
8. Recovery requires functional and data-integrity checks.

## Limitations

This is a hands-on learning environment, not a
production deployment.

The Flask development server is used for the lab.
Production systems require an appropriate WSGI server,
stronger secret management, monitoring, backup,
and additional security and reliability controls.
