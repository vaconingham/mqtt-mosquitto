
from distutils.log import INFO
from datetime import datetime
import json, topics, test, time, logging
import paho.mqtt.client as mqtt





# Root log handler. Good practice would be to push any logs from the 
# client to a specific log files. Further configuration required. 
logging.basicConfig(filename='logs/info.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')

message_log = {}

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


def task2_mqtt_client():
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
            print('Published: ' + str(mid))
            logging.info(str(str(mid)))

    def on_log(client, userdata, level, buf):
        print('log: ' + str(buf))
        logging.info(str(buf))

    # Encryption and decryption required.
    # Client ID requires configuration so that subscriber knows which
    # device the message is coming from.
    def on_message(client, userdata, msg):
        message_log[int(datetime.now().strftime("%H%M%S%f"))] = int(msg.payload)
        averages = {
            'client': test.client1,
            'timestamp': datetime.now().strftime("%H%M%S%f"),
            '1-minute-average': one_minute_averages(),
            '5-minute-average': five_minute_averages(),
            '30-minute-average': thirty_minute_averages()
        }
        client.publish(
            topics.energy[2],
            payload=json.dumps(averages, indent=4),
            qos=0,
            retain=True
            )
    
    client = mqtt.Client(
        client_id=test.client2,
        clean_session=False,
        userdata=None,
        protocol=mqtt.MQTTv311,
        transport='tcp'
        )

    client.connect(test.broker, 1883)

    client.on_connect = on_connect
    client.on_log = on_log
    client.on_message = on_message
    client.on_publish = on_publish

    # This is here to give time to for the client to connect before tryying to process data.
    # The more efficient way would be to use a flag on_connect.
    time.sleep(4)

    return client



message_log_2 = {}

def task3_mqtt_client():
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
            message_log_2.append({i})
        logging.info(message)

    client = mqtt.Client(
        client_id=test.client3,
        clean_session=False,
        userdata=None,
        protocol=mqtt.MQTTv311,
        transport='tcp'
        )

    client.connect(test.broker, 1883, 5)

    client.on_connect = on_connect
    # client.on_log = on_log
    client.on_message = on_message

    # This is here to give time to for the client to connect before tryying to process data.
    # The more efficient way would be to use a flag on_connect.
    time.sleep(4)
