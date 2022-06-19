# Django MQTT Service

### News

This project was recently created using Django. Visit the `django-implementation` branch for more information.

### Overview

This is a work in progress of a Django MQTT Service using a Mosquitto broker and Django Channels.

The broker service is a Eclipse Mosquitto broker, which is running inside a Docker container. The Django application serves gives users a UI to visualise MQTT clients connected to the broker.

The UI does two things:
1. Collects data from clients publishing to restricted topics on the MQTT broker.
2. Django allows users to visualise information through a simple UI about each client connected within the IoT.

### Important Notes
For the purpose of simplicity, this project does not have isolated environments i.e. development, staging, and production.

Ideally, each environment should be in their own AWS account with their own IAM. These accounts should be children of the main account, making it easy to consolidate tasks, billing, permissions, and more.

### How to get it working:

1. Start the Eclipse Mosquitto broker:

`docker run -it -d -p 1883:1883 -p 9001:9001 -v home/dev/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto`

2. If you haven't done so already, create a folder for your logs in your working directory: `mkdir logs`
2. Run the "mock" MQTT client: `python3 test_client.py`
3. Start the Django server: `python3 manage.py runserver`
4. Ensure logs are working correctly. This can be either seeing output in log files or in the console.
5. Visit 127.0.0.1/client and enter the client_name, which can be found in the Django admin console or in the test_client.py file.

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