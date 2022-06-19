from django.apps import AppConfig
# from threading import Thread
# import paho.mqtt.client as mqtt


# class MqttClient(Thread):
#     def __init__(self, broker, port, timeout, topics):
#         super(MqttClient, self).__init__()
#         self.client = mqtt.Client()
#         self.broker = broker
#         self.port = port
#         self.timeout = timeout
#         self.topics = topics
#         self.total_messages = 0

# #  run method override from Thread class
# def run(self):
#     self.connect_to_broker()

# def connect_to_broker(self):
#     self.client.on_connect = self.on_connect
#     self.client.on_message = self.on_message
#     self.client.connect(self.broker, self.port, self.timeout)
#     self.client.loop_forever()

# # The callback for when a PUBLISH message is received from the server.
# def on_message(self, client, userdata, msg):
#     self.total_messages = self.total_messages + 1
#     print(str(msg.payload) + "Total: {}".format(self.total_messages))

# # The callback for when the client receives a CONNACK response from the server.
# def on_connect(self, client, userdata, flags, rc):
#     #  Subscribe to a list of topics using a lock to guarantee that a topic is only subscribed once
#     for topic in self.topics:
#         client.subscribe(topic)


class ClientConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'client'

# def ready(self):
#     MqttClient("192.168.0.165", 1883, 60, ["teste/01"]).start()