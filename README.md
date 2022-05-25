# MQTT Service

## Overview

This is an example of a production ready MQTT service. 

Client 1: Broker=broker, publishTopic = whatever/the/topic, Payload = (Rand), sendInterval = 1:30 seconds
Client 2: Broker=broker, subscribeTopic = whatever/the/topic, payload.json.load(60 second avg, 5min avg, 30min avg), publishTopic = different/topic
Client 3: Broker=broker, subscribeTopic = different/topic, print to pretty tabular, DB

Access and configure broker log


## Requirements



## Broker

To start the RabbitMQ broker:

`docker run rabbitmq`


## Notes

For the purpose of simplicity, this project does not have isolated environments i.e. development, staging, and production.

Ideally, each environment should be in their own AWS account with their own IAM. These accounts should be children of the main account, making it easy to consolidate tasks, billing, permissions, and more.