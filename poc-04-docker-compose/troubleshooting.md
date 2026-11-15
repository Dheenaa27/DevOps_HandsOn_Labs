# POC 04 — Troubleshooting and Root Cause Analysis

## Incident 01: PostgreSQL Dependency Failure

### Scenario

PostgreSQL was intentionally stopped while the
Flask application remained running.

### Failure Injection

    docker compose stop db

### Observed Symptoms

- /health returned HTTP 200.
- /db-health returned HTTP 503.
- Flask remained running.
- PostgreSQL became unavailable.

### Application Log Evidence

Database health check failed:
[Errno -2] Name or service not known

GET /db-health HTTP/1.1 returned 503.

### Root Cause

The PostgreSQL service was intentionally stopped.

During the failure, the Flask application could not
resolve the configured database service hostname.

This prevented database connectivity while the
Flask process itself remained responsive.

### Recovery Action

    docker compose start db

### Recovery Validation

Checked service status:

    docker compose ps

Validated application responsiveness:

    curl -i http://127.0.0.1:3004/health

Validated database connectivity:

    curl -i http://127.0.0.1:3004/db-health

Queried the poc04_evidence table after recovery.

### Result

- PostgreSQL returned to healthy status.
- Flask remained operational.
- Database connectivity was restored.
- The original test record was preserved.

### Key Learnings

- A running application can have an unavailable dependency.
- HTTP 503 can communicate dependency failure.
- Application logs provide incident evidence.
- Restarting the failed service can restore connectivity.
- Recovery validation must include data integrity.

## Incident 02: Container Recreation and Persistence

### Scenario

The PostgreSQL container was recreated while
retaining its named Docker volume.

### Command

    docker compose up -d --force-recreate --no-deps db

### Validation

The original POC04_DATA_PERSISTENCE_TEST record
was retrieved after recreation.

### Result

Database data persisted because it was stored in
the named volume rather than only in the container's
writable filesystem.

### Operational Note

Docker volumes are not substitutes for database
backups or high-availability solutions.
