
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

## Failure Drill 01 — Docker Port Mismatch

### Scenario
A Flask application was running inside a Docker
container on port 3000, published on host port 3001.

### Failure
Attempted to access localhost:3002/health.

Observed:
curl: (7) Failed to connect to server

### Root Cause
The request targeted an unpublished host port.
The correct mapping was 127.0.0.1:3001 -> 3000/tcp.

### Investigation
docker port poc03-port-drill
docker ps --filter "name=poc03-port-drill"

### Recovery
Accessed the correct published host port:
curl -i http://127.0.0.1:3001/health

### Validation
HTTP/1.1 200 OK
{"status":"healthy"}

Container runtime state: running

### Key Learning
A running container does not guarantee that an
application is accessible through every host port.
Correct port mapping and application health must
be validated independently.

### Production Implication
Incorrect port mappings or routing configurations
can make healthy applications unreachable.
---

## Session 01 Summary

Both issues were resolved during local
environment preparation and validation.

Docker image build and container runtime
testing are planned for Session 02.
