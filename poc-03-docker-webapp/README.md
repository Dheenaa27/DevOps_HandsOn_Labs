# POC 03 — Containerize a Web Application

## Objective
Package a Python Flask application into a reproducible Docker image.

## Environment
- Host: macOS (Apple Silicon / ARM64)
- Container platform: Docker Desktop
- Local Python: 3.9.6
- Docker base image: python:3.12-slim
- Framework: Flask 3.1.1

## Application Architecture
MacBook → Flask Application → Docker Image → Container

## Project Structure
- app/main.py — Flask application
- requirements.txt — Python dependencies
- Dockerfile — Container image instructions
- .dockerignore — Docker build exclusions
- .gitignore — Git exclusions
- screenshots/ — Validation evidence
- troubleshooting.md — Issue investigation and RCA

## Session 01 — Application Preparation
- Verified Docker CLI and Engine
- Created a Git feature branch
- Developed a Flask web application
- Created an isolated Python environment
- Installed application dependencies
- Validated HTTP endpoints locally
- Created the initial Dockerfile
- Configured ignore files

## Local Validation

Start the application:

    python app/main.py

Test the home endpoint:

    curl -i http://127.0.0.1:3000/

Test the health endpoint:

    curl -i http://127.0.0.1:3000/health

Both endpoints returned HTTP 200.

## Dockerfile
The initial Dockerfile uses Python 3.12 slim,
installs Flask dependencies, copies application
code, exposes port 3000, and defines startup CMD.

## Validation Evidence
See screenshots/ for terminal outputs and
application validation screenshots.

## Next Steps — Session 02
- Build Docker image
- Tag and inspect image
- Run application container
- Configure port mapping
- Validate HTTP endpoints inside container

## Key Learnings
- Verify the application before containerization.
- Understand Docker CLI vs Docker Engine.
- Understand local vs container environments.
- Use Git branches for isolated development.
- Exclude unnecessary and sensitive files.
- Capture troubleshooting evidence.

## Docker Build Cache Experiment

### Objective
Understand Docker layer caching and selective cache invalidation.

### Experiment 1 - Cache Reuse
Rebuilt the image without modifying application files.

Result:
- WORKDIR: CACHED
- COPY requirements.txt: CACHED
- RUN pip install: CACHED
- COPY application: CACHED

### Experiment 2 - Cache Invalidation
Added a temporary comment to app/main.py and rebuilt.

Result:
- Dependency layers remained cached.
- Application COPY layer was rebuilt.
- Docker image exported successfully.
- Original application code was restored.

### Key Learnings
- Docker caching avoids unnecessary build operations.
- Dockerfile instruction ordering influences cache reuse.
- Application changes need not reinstall dependencies.
- Efficient caching can reduce CI/CD build times.
creenshots/25.docker_cache_reuse.png
- screenshots/26.docker_cache_invalidation.png

## Docker Build Cache Experiment

### Objective
Understand Docker layer caching and selective cache invalidation.

### Experiment 1 - Cache Reuse
Rebuilt the image without modifying application files.

Result:
- WORKDIR: CACHED
- COPY requirements.txt: CACHED
- RUN pip install: CACHED
- COPY application: CACHED

### Experiment 2 - Cache Invalidation
Added a temporary comment to app/main.py and rebuilt.

Result:
- Dependency layers remained cached.
- Application COPY layer was rebuilt.
- Docker image exported successfully.
- Original application code was restored.

### Key Learnings
- Docker caching avoids unnecessary build operations.
- Dockerfile instruction ordering influences cache reuse.
- Application changes need not reinstall dependencies.
- Efficient caching can reduce CI/CD build times.

### Evidence
- screenshots/25.docker_cache_reuse.png
- screenshots/26.docker_cache_invalidation.png
