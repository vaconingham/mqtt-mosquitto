# Django MQTT Service

### Overview

This is a work in progress of a Django MQTT Service using a Mosquitto broker and Django Channels.

### Important Notes
For the purpose of simplicity, this project does not have isolated environments i.e. development, staging, and production.

Ideally, each environment should be in their own AWS account with their own IAM. These accounts should be children of the main account, making it easy to consolidate tasks, billing, permissions, and more.

### Setup (Current)

1. Start the Eclipse Mosquitto broker:

`docker run -it -d -p 1883:1883 -p 9001:9001 -v home/dev/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto`

2. If you haven't done so already, create a folder for your logs in your working directory: `mkdir logs`
2. Run files manually: `python3 client1.py, client2.py, and client3.py`
3. Ensure logs are working correctly. This can be either seeing output in log files or in the console.

### Important Notes: 
Further development and configuration is required. Current broker does not have SSL enabled, client authentication, messages are unencrypted, and no data, log, or PID files have been created.

Server requires configuring for CI/CD with Ansible.

### Bugs

- Missing exception handling in moving functions. If it returns zero, the code will break.
- Moving averages functions divide by zero. As there is no exception handling, the code breaks.
- Broker requires user authentication and SSL.
- Files should be imported as modules and called from one main file.
- Logs need configured properly.

### Contributing

1. Clone the `prod` branch.
2. Make a pull request to the `dev` branch.
3. Be verbose, specific, and generous with your commentary.