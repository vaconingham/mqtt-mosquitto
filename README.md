# MQTT Service

## Overview

This is an example of a production ready MQTT service written in Python with a Eclipse Mosquitto broker running inside a Docker cotainer.

### Important Notes: 
For the purpose of simplicity, this project does not have isolated environments i.e. development, staging, and production.

Ideally, each environment should be in their own AWS account with their own IAM. These accounts should be children of the main account, making it easy to consolidate tasks, billing, permissions, and more.

## Setup (Current):

1. Start the Eclipse Mosquitto broker:

`docker run -it -d -p 1883:1883 -p 9001:9001 -v home/dev/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto`

2. Run files manually: `python3 client1.py, client2.py, and client3.py`
3. Ensure logs are working correctly. This can be either seeing output in log files or in the console.

### Notes: 
Further development and configuration is required. Current broker does not have SSL enabled, client authentication, messages are unencrypted, and no data, log, or PID files have been created.

Server requires configuring for CI/CD with Ansible.