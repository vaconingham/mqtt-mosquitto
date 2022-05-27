import json, topics, madeup, time, logging
import paho.mqtt.client as mqtt
from datetime import datetime
from .models import Client, DataOutput


# Root log handler. Good practice would be to push any logs from the 
# client to a specific log files. Further configuration required. 
logging.basicConfig(filename='logs/client2.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')

message_log = {}


CLIENT_NAME = 'c80dd6b0-e459-4609-90dd-05341ef5ad4c'
client_instance = Client.objects.get(client_name=CLIENT_NAME)

# Here are the functions for calculating the average value
# from a client over 1 minute, 5 minutes, and 30 minutes.
# With a little more effort you could reduce these down to make
# the them more flexible and easier to use.
# Division by zero is still a problem.
def one_minute_averages():
    window = int(datetime.now().strftime("%H%M%S%f")) - 100000000
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

def five_minute_averages():
    window = int(datetime.now().strftime("%H%M%S%f")) - 500000000
    history = {k:v for k,v in message_log.items() if k >= window}
    for i in list(history):
        if i < window:
            history.pop(i)
    avg = sum(history.values()) / len(list(history))
    if avg == 0:
        return 0
    else:
        return avg

def thirty_minute_averages():
    window = int(datetime.now().strftime("%H%M%S%f")) - 3000000000
    history = {k:v for k,v in message_log.items() if k >= window}
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
        client.subscribe(topics.energy[1])
        print("Connected | RESULT CODE:"+str(rc))
    elif rc ==1:
        print("Connection failed – Incorrect protocol version | RESULT CODE: " + str(rc))
    elif rc ==2:
        print("Connection failed – Invalid client identifier | RESULT CODE: " + str(rc))
    elif rc ==3:
        print("Connection failed – Server error | RESULT CODE: " + str(rc))
    elif rc ==4:
        print("Connection failed – Bad username or password | RESULT CODE: " + str(rc))
    elif rc ==5:
        print("Connection failed – Not authorised | RESULT CODE: " + str(rc))
    else:
        print("Connection failed - Unknown | RESULT CODE: Undefined")

def on_publish(client, userdata, mid):
        logging.info('PUBLISHED PAYLOAD: ' + str(mid))

# The callback for when a LOG message is received from the server.
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
        one_minute_average = one_minute_averages(),
        five_minute_average = five_minute_averages(),
        thirty_minute_average = thirty_minute_averages()
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
   
# Define the client instance.
client = mqtt.Client(
    client_id=madeup.client2,
    clean_session=False,
    userdata=None,
    protocol=mqtt.MQTTv311,
    transport='tcp'
    )

# Connect the client to the broker.
client.connect(madeup.broker, 1883)

# Activate callbacks - Comment out as necessary.
client.on_connect = on_connect
# client.on_log = on_log
client.on_message = on_message
client.on_publish = on_publish

# This is here to give time to for the client to connect before tryying to process data.
# The more efficient way would be to use a flag on_connect.
time.sleep(4)

client.loop_forever()
