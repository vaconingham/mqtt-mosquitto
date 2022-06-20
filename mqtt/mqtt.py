import logging
import paho.mqtt.client as mqtt
from datetime import datetime
from .models import Client, DataOutput


logging.basicConfig(filename='logs/mqtt.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')


CLIENT_NAME = 'test' # For testing only. Requires configuring.
client_instance = Client.objects.get(client_name=CLIENT_NAME)


message_log = {}

def averages(min):
    window = int(datetime.now().strftime("%H%M%S%f")) - min
    history = {}
    for i in message_log.items():
        if i[0] >= window:
            history.update({i})
    for i in list(history):
        if i < window:
            history.pop(i)
    if sum(history.values()) == 0 or len(list(history)) == 0:
        return 0
    else:
        return sum(history.values()) / len(list(history))


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe('site/in/solar')
        print("Started MQTT Service")
    elif rc ==1:
        print("MQTT Connection failed – Incorrect protocol version | RESULT CODE: " + str(rc))
    elif rc ==2:
        print("MQTT Connection failed – Invalid client identifier | RESULT CODE: " + str(rc))
    elif rc ==3:
        print("MQTT Connection failed – Server error | RESULT CODE: " + str(rc))
    elif rc ==4:
        print("MQTT Connection failed – Bad username or password | RESULT CODE: " + str(rc))
    elif rc ==5:
        print("MQTT Connection failed – Not authorised | RESULT CODE: " + str(rc))
    else:
        print("MQTT Connection failed - Unknown | RESULT CODE: Undefined")

def on_publish(client, userdata, mid):
    logging.info('PUBLISHED DATA: ' + str(mid))

def on_log(client, userdata, level, buf):
    logging.info('LOG: ' + str(buf))

def on_message(client, userdata, msg):
    message_log[int(datetime.now().strftime("%H%M%S%f"))] = int(msg.payload)
    data = DataOutput(
        client_id = client_instance,
        data_timestamp = datetime.now().strftime("%H:%M:%S:%f"),
        current_value = list(message_log.values())[-1],
        one_minute_average = averages(100000000),
        five_minute_average = averages(500000000),
        thirty_minute_average = averages(3000000000),
    )
    data.save()


client = mqtt.Client(
    client_id='data-service',
    clean_session=False,
    userdata=None,
    protocol=mqtt.MQTTv311,
    transport='tcp'
    )

client.connect('localhost', 1883)

client.on_connect = on_connect
client.on_log = on_log
client.on_message = on_message
client.on_publish = on_publish

client.loop_start()
