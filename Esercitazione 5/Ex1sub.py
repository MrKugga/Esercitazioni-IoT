import paho.mqtt.client as PahoMQTT
import random, string, json, time

class Subscriber:
    def __init__(self, clientID, topic, broker):
        self._paho_mqtt = PahoMQTT.Client(clientID, clean_session= True)
        self.messageBroker = broker
        self.topic = topic
        self._paho_mqtt.on_connect = self.onConnect
        self._paho_mqtt.on_message = self.onMessageRecived

    def start(self):
        self._paho_mqtt.connect(self.messageBroker, port=1883)
        self._paho_mqtt.loop_start()
        self._paho_mqtt.subscribe(self.topic, 2)
        print("Subscribed at topic %s" %self.topic)

    def stop(self):
        self._paho_mqtt.unsubscribe(self.topic)
        self._paho_mqtt.loop_stop()
        self._paho_mqtt.disconnect()

    def onConnect(self, paho_mqtt, userdata, flags, rc):
        print(f"Connected to {self.messageBroker} with result code: {rc}")

    def onMessageRecived(self, client, userdata, message):
        instructions = json.loads(message.payload)
        ledOn = True if instructions["led_on"] else False

        if ledOn:
            print("Led turned on")
        else:
            print("Led turned off")

if __name__ == "__main__":

    try:
        with open("files/ID.json", "rb") as f:
            content = json.load(f)
            clientID = content["clientID"]

    except FileNotFoundError:
        lenght = 5
        clientID = "".join(random.choices(string.ascii_letters + string.digits, k=lenght)) #genera un ID random
        with open("files/ID.json", "w") as f:
            dict = {"clientID": clientID}
            json.dump(dict, f)


    topic = "/iot/led/this/better/be/unique/%s" %clientID
    broker = "mqtt.eclipse.org"
    sub = Subscriber(clientID, topic, broker)

    sub.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sub.stop()
        print("\nSubscriber stopped")

    finally:
        sub.stop()
