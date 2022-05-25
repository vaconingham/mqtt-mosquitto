# MQTT Service

## Overview

This is an example of a production ready MQTT service written in Python with a Eclipse Mosquitto broker running inside a Docker cotainer.

### Notes: 
For the purpose of simplicity, this project does not have isolated environments i.e. development, staging, and production.

Ideally, each environment should be in their own AWS account with their own IAM. These accounts should be children of the main account, making it easy to consolidate tasks, billing, permissions, and more.

## Broker

To start the Eclipse Mosquitto broker run:

`docker run -it -p 1883:1883 -p 9001:9001 -v mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto`

### Notes: 
Further development and configuration is required. Current broker does not have authentication, messages are unencrypted, and no data, log, or PID files have been created.