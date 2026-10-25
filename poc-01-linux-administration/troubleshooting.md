# Troubleshooting Log

## Case 01: Directory Execution Error

Command:
sudo /opt/demoapp/

Observed error:
Permission denied

Explanation:
A directory cannot be executed as a program.
Directory execute permission controls traversal.

Correct approach:
sudo ls /opt/demoapp

## Case 02: Access Denied to Application Directory

Command:
ls /opt/demoapp

Observed error:
Permission denied

Root cause:
The ubuntu user is not the directory owner
or a member of appteam. Directory mode is 750.

Resolution:
No change required. Access restriction is intentional.

Validation:
sudo -u appsvc ls /opt/demoapp

