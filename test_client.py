"""This is a 'mock' client that we can use to test our MQTT service. The client 
publishes random values between 1-100 to the broker at random intervals between 1-30 seconds.

The print functions have been left in place so that in development you can easily check if the test_client
is working."""

import time
import random
import logging
import datetime
import paho.mqtt.client as mqtt


logging.basicConfig(filename='logs/test_client.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected | RESULT CODE:"+str(rc))
        logging.info("Connected | RESULT CODE:"+str(rc))
    elif rc ==1:
        print("Connection failed – Incorrect protocol version | RESULT CODE: " + str(rc))
        logging.error("Connection failed – Incorrect protocol version | RESULT CODE: " + str(rc))
    elif rc ==2:
        print("Connection failed – Invalid client identifier | RESULT CODE: " + str(rc))
        logging.error("Connection failed – Invalid client identifier | RESULT CODE: " + str(rc))
    elif rc ==3:
        print("Connection failed – Server error | RESULT CODE: " + str(rc))
        logging.error("Connection failed – Server error | RESULT CODE: " + str(rc))
    elif rc ==4:
        print("Connection failed – Bad username or password | RESULT CODE: " + str(rc))
        logging.error("Connection failed – Bad username or password | RESULT CODE: " + str(rc))
    elif rc ==5:
        print("Connection failed – Not authorised | RESULT CODE: " + str(rc))
        logging.error("Connection failed – Not authorised | RESULT CODE: " + str(rc))
    else:
        print("Connection failed - Unknown | RESULT CODE: Undefined")
        logging.error("Connection failed - Unknown | RESULT CODE: Undefined")

def on_publish(client, userdata, mid):
    print('TEST_CLIENT Published: RANDINT at ' + datetime.datetime.now().strftime("%H:%M:%S:%f"))
    logging.info('Published: RANDINT at ' + datetime.datetime.now().strftime("%H:%M:%S:%f") + ' | mid: ' + str(mid))

client = mqtt.Client(
    client_id='test',
    clean_session=True,
    userdata=None,
    protocol=mqtt.MQTTv311,
    transport='tcp'
    )

client.connect('localhost', 1883)

client.on_connect = on_connect
client.on_publish = on_publish

client.loop_start()

while True:
    client.publish(
        'site/in/solar',
        payload=str(random.randint(1,100)),
        qos=0,
        retain=True
        )
    time.sleep(random.randint(1,30))
