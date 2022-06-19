# Django MQTT Service


### Overview

This is an example MQTT service using Djago.

The broker service is a Eclipse Mosquitto broker, which is running inside a Docker container. The Django application serves a UI for users to visualise information about MQTT clients connected to the broker.

The UI does two things:
1. Collects data from clients publishing to restricted topics on the MQTT broker.
2. Django allows users to visualise information through a simple UI about each client connected within the IoT.

### Important Notes
For the purpose of simplicity, this project does not have isolated environments i.e. development, staging, and production.

Ideally, each environment should be in their own AWS account with their own IAM. These accounts should be children of the main account, making it easy to consolidate tasks, billing, permissions, and more.

### How to get it working:

1. Start the Eclipse Mosquitto broker:

`docker run -it -d -p 1883:1883 -p 9001:9001 -v home/dev/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto`

1. If you haven't done so already, create a folder for your logs in your working directory: `mkdir logs`
2. To test the MQTT service, run the "mock" mqtt client: `python3 test_client.py`
3. Configure Django i.e. makemigrations, migrate, createsuperuser.
4. Start the Django server: `python3 manage.py runserver`
5. Ensure logs are working correctly. This can be either seeing output in log files or in the console.
6. Visit 127.0.0.1 and enter the client ID or click "Test Service" to test if the MQTT service is working.

### Important Notes: 
- Further development and configuration is required. Current broker does not have SSL enabled, client authentication, messages are unencrypted, and no data, log, or PID files have been created.

- Django is currently running DEBUG = True. Further configuration required to have it production ready.

- Django running development server only. Production grade server such as Gunicorn or UWSGI is required.

- Server requires configuring for CI/CD with Ansible.

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