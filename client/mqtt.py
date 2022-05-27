import topics, time, random, test, logging
import paho.mqtt.client as mqtt


# Root log handler. Good practice would be to push any logs from the 
# client to a specific log files. Further configuration required. 
logging.basicConfig(filename='logs/mqtt.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info("Connected | RESULT CODE:"+str(rc))
    elif rc ==1:
        logging.info("Connection failed – Incorrect protocol version | RESULT CODE: " + str(rc))
    elif rc ==2:
        logging.info("Connection failed – Invalid client identifier | RESULT CODE: " + str(rc))
    elif rc ==3:
        logging.info("Connection failed – Server error | RESULT CODE: " + str(rc))
    elif rc ==4:
        logging.info("Connection failed – Bad username or password | RESULT CODE: " + str(rc))
    elif rc ==5:
        logging.info("Connection failed – Not authorised | RESULT CODE: " + str(rc))
    else:
        logging.info("Connection failed - Unknown | RESULT CODE: Undefined")

def on_log(client, userdata, level, buf):
    logging.info(str(buf))

def on_publish(client, userdata, mid):
    logging.info(str(mid))

client = mqtt.Client(
    client_id=test.client1,
    clean_session=True,
    userdata=None,
    protocol=mqtt.MQTTv311,
    transport='tcp'
    )

client.connect(test.broker, 1883)

client.on_connect = on_connect
# client.on_log = on_log
# client.on_publish = on_publish

# This is here to give time to for the client to connect before tryying to process data.
# The more efficient way would be to use a flag on_connect.
time.sleep(4)

# Publish random values between 1-100 to the broker at random intervals between 1-30 seconds.
while True:
    client.publish(
        topics.energy[1],
        payload=str(random.randint(1,100)),
        qos=0,
        retain=True
        )
    time.sleep(random.randint(1,30))
