# POC 01 - Linux Server Administration

## Objective
Provision and administer an Ubuntu Linux server on AWS EC2.

## Environment
- Platform: AWS EC2
- OS: Ubuntu 26.04.1 LTS
- CPU: 1 vCPU
- Memory: 951 MiB
- Root filesystem: 6.7 GiB
- Authentication: SSH private key

## Completed Exercises

### 1. Server Verification
- Verified login identity and hostname
- Checked operating system and kernel
- Confirmed SSH connectivity

### 2. System Exploration
- Inspected CPU and memory
- Examined disks and filesystems
- Verified network interfaces
- Investigated running processes

### 3. Users and Permissions
- Created group: appteam
- Created service account: appsvc
- Created directory: /opt/demoapp
- Configured ownership: appsvc:appteam
- Applied directory permissions: 750

## Validation
- Service account created successfully
- Owner successfully created a test file
- Unauthorized ubuntu user was denied access
- Test file removed after validation

## Key Learnings
- Linux ownership and permission management
- Least-privilege access
- Service accounts versus interactive users
- Basic infrastructure troubleshooting

## Status
Initial Linux administration exercises completed.
Service management and networking labs pending.
