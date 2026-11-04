
# POC 03 — Troubleshooting and Root Cause Analysis

## Incident 01 — Docker Engine Connection Failure

### Symptom
The Docker CLI was installed, but `docker info`
failed with a Docker API connection error.

### Root Cause
The Docker Engine was not accessible through
the configured Docker socket.

### Resolution
Started Docker Desktop and verified that
the Docker Engine became accessible.

### Validation
`docker info` successfully displayed server
information, running containers, and images.

### Production Learning
Docker CLI availability does not guarantee
Docker Engine availability.

---

## Incident 02 — Flask HTTP Connection Failure

### Symptom
A curl request to localhost:3000 failed
with connection error 7.

### Root Cause
The Flask application had been stopped
using Ctrl+C before executing curl.

### Resolution
Restarted the Flask application and kept
it running in Terminal 1.

Executed curl from a separate Terminal 2.

### Validation
GET / returned HTTP 200.
GET /health returned HTTP 200.

### Production Learning
A failed connection does not necessarily
indicate an application code defect.

Verify process availability, listening ports,
and service state before changing code.

---

## Session 01 Summary

Both issues were resolved during local
environment preparation and validation.

Docker image build and container runtime
testing are planned for Session 02.
