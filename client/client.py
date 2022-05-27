import paho.mqtt.client as mqtt
import logging, time, random


logging.basicConfig(filename='logs/client.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')

def connect():
    topic = 'site/in/solar'
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            client.connected_flag = True
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

    mqtt.Client.connected_flag = False

    client = mqtt.Client(
        client_id='test-client-1',
        clean_session=True,
        userdata=None,
        protocol=mqtt.MQTTv311,
        transport='tcp'
        )

    client.connect('localhost', 1883, 60)
    client.on_connect = on_connect

    client.loop_start()

    while not client.connected_flag:
        time.sleep(1)
    else:
        client.publish(
            topic=topic,
            payload=str(random.randint(1,100)),
            qos=0,
            retain=True
            )
        time.sleep(random.randint(1,30))


def main():
    connect()


if __name__ == '__main__':
    main()