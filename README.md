# Django MQTT Service


### Overview

This is an example MQTT service using Django and a Eclipse Mosquitto MQTT broker.

The application serves a UI for users to visualise information about MQTT clients connected to their network.

The UI does two primary things:
1. Lists all devices connected to a network (broker).
2. Collects data from clients on restricted topics on the MQTT broker.
3. Displays data about each client.

### How to get it working:

1. Start the Eclipse Mosquitto broker using Docker:

`docker run -it -d -p 1883:1883 -p 9001:9001 -v home/mqtt-mosquitto/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto`

2. If you haven't done so already, create a folder for your logs in your working directory: `mkdir logs`
3. To test the MQTT service, run the test client: `python3 test_client.py`
4. Configure Django i.e. makemigrations, migrate, createsuperuser.
5. Start the Django server: `python3 manage.py runserver`
8. Visit 127.0.0.1 and enter the client ID or click "Test Service" to test if the MQTT service is working.

### Important Notes: 
- Further development and configuration is required. Current broker does not have SSL enabled, client authentication, messages are unencrypted, and no data, log, or PID files have been created.

- User accounts and services have not yet been deveeloped. This would be necessary so that users can easily register and view all clients connected to the service.

- MQTT service requires configuring to allow for dynamic client detection.

- Django is currently running DEBUG = True. Further configuration required to have it production ready.

- Django running development server only. Production grade server such as Gunicorn or UWSGI is required.

- Server requires configuring for CI/CD with Ansible.

### Contributing

1. Clone the `prod` branch.
2. Make a pull request to the `dev` branch.