from distutils.log import INFO
import paho.mqtt.client as mqtt
import test, topics, time, json, logging
from prettytable import PrettyTable

# Root log handler. Good practice would be to push any logs from the 
# client to a specific log files. Further configuration required. 
logging.basicConfig(filename='logs/client3.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')

table = PrettyTable()
message_log = {}

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(topics.energy[2])
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

def on_log(client, userdata, level, buf):
    print('log: ' + str(buf))

def on_message(client, userdata, msg):
    payload = msg.payload
    message = json.loads(payload.decode('utf_8'))
    for i in message.items():
        message_log.append({i})
    logging.info(message)

client = mqtt.Client(
    client_id=test.client3,
    clean_session=False,
    userdata=None,
    protocol=mqtt.MQTTv311,
    transport='tcp'
    )

client.connect(test.broker, 1883, 5)

# Comment out callbacks as necessary.
client.on_connect = on_connect
client.on_log = on_log
client.on_message = on_message

# This is here to give time to for the client to connect before tryying to process data.
# The more efficient way would be to use a flag on_connect.
time.sleep(4)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()