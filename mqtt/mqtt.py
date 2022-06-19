import time
import logging
import paho.mqtt.client as mqtt
from datetime import datetime
from .models import Client, DataOutput


# Root log handler. Good practice would be to push any logs from the 
# client to a specific log files. Further configuration required. 
logging.basicConfig(filename='logs/mqtt.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')

message_log = {}


CLIENT_NAME = 'test'
client_instance = Client.objects.get(client_name=CLIENT_NAME)


# Division by zero is still a problem.
def averages(min):
    window = int(datetime.now().strftime("%H%M%S%f")) - min
    history = {}
    for i in message_log.items():
        if i[0] >= window:
            history.update({i})
    for i in list(history):
        if i < window:
            history.pop(i)
    avg = sum(history.values()) / len(list(history))
    if avg == 0:
        return 0
    else:
        return avg


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
    logging.info('PUBLISHED PAYLOAD: ' + str(mid))

def on_log(client, userdata, level, buf):
    logging.info('LOG: ' + str(buf))

# Encryption and decryption required.
# Client ID requires configuration so that subscriber knows which
# device the message is coming from.
def on_message(client, userdata, msg):
    message_log[int(datetime.now().strftime("%H%M%S%f"))] = int(msg.payload)
    data = DataOutput(
        client_id = client_instance,
        timestamp = datetime.now().strftime("%H%M%S%f"),
        current_value = list(message_log.values())[-1],
        one_minute_average = averages(100000000),
        five_minute_average = averages(500000000),
        thirty_minute_average = averages(3000000000),
    )
    data.save()
    # averages = {
    #     'client': madeup.client1,
    #     'timestamp': datetime.now().strftime("%H%M%S%f"),
    #     'current': list(message_log.values())[-1],
    #     '1-minute-average': one_minute_averages(),
    #     '5-minute-average': five_minute_averages(),
    #     '30-minute-average': thirty_minute_averages()
    # }
    # client.publish(
    #     topics.energy[2],
    #     payload=json.dumps(averages, indent=4),
    #     qos=0,
    #     retain=True
    #     )
   

client = mqtt.Client(
    client_id='test-service',
    clean_session=False,
    userdata=None,
    protocol=mqtt.MQTTv311,
    transport='tcp'
    )

client.connect('localhost', 1883)

# Activate callbacks - Comment out as necessary.
client.on_connect = on_connect
# client.on_log = on_log
client.on_message = on_message
client.on_publish = on_publish

# This is here to give time to for the client to connect before tryying to process data.
# The more efficient way would be to use a flag on_connect.
time.sleep(4)

client.loop_start()
