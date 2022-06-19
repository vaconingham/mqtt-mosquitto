import time, random, logging, datetime
import paho.mqtt.client as mqtt


# Root log handler. Good practice would be to push any logs from the 
# client to a specific log files. Further configuration required. 
logging.basicConfig(filename='logs/test_client.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')

# The callback for when the client receives a CONNACK response from the server.
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

# Log published data.
def on_publish(client, userdata, mid):
    print('Published: RANDINT at ' + datetime.datetime.now().strftime("%H:%M:%S:%f"))
    logging.info('Published: RANDINT at ' + datetime.datetime.now().strftime("%H:%M:%S:%f") + ' | mid: ' + str(mid))

# Define the client instance.
client = mqtt.Client(
    client_id='c80dd6b0-e459-4609-90dd-05341ef5ad4c',
    clean_session=True,
    userdata=None,
    protocol=mqtt.MQTTv311,
    transport='tcp'
    )

# Connect the client to the broker.
client.connect('localhost', 1883)

client.on_connect = on_connect
client.on_publish = on_publish

# This is here to give time to for the client to connect before tryying to process data.
# The more efficient way would be to use a flag on_connect.
time.sleep(4)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()

# Publish random values between 1-100 to the broker at random intervals between 1-30 seconds.
while True:
    client.publish(
        'site/in/solar',
        payload=str(random.randint(1,100)),
        qos=0,
        retain=True
        )
    time.sleep(random.randint(1,30))
