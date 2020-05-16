import paho.mqtt.client as PahoMQTT
import random, time, string, json
from datetime import datetime

class Client:

    def __init__(self, clientID, broker, topic, name, first):
        self._paho_mqtt = PahoMQTT.Client(clientID, clean_session= True)
        self.messageBroker = broker
        self.topic = topic
        self._paho_mqtt.on_connect = self.onConnect
        self._paho_mqtt.on_message = self.onMessageRecived
        self.name = name
        self.clientID = clientID
        self.wait = not first # serve a "passare" il turno

    def start(self):
        self._paho_mqtt.connect(self.messageBroker, port=1883)
        self._paho_mqtt.subscribe(self.topic)
        self._paho_mqtt.loop_start()
        print(f"Sottoscritto alla chat.")

    def stop(self):
        self._paho_mqtt.unsubscribe(self.topic)
        self._paho_mqtt.loop_stop()
        self._paho_mqtt.disconnect()
        print("\nDisconnesso.")

    def myUnsubscribe(self):
        self._paho_mqtt.unsubscribe(self.topic)

    def mySubscribe(self):
        self._paho_mqtt.subscribe(self.topic)

    def onConnect(self, paho_mqtt, userdata, flags, rc):
        print("Connesso al broker con result code %s" %rc)

    def myPublish(self, message):
        self._paho_mqtt.publish(self.topic, message, 2)

    def onMessageRecived(self, client, userdata, message):
        payload = json.loads(message.payload)
        sender = payload["sender"]

        msg = payload["message"]
        print(f"{sender}: {msg}")
        self.wait = False


if __name__ == "__main__":
    name = input("Qual è il tuo nome?\n>>> ")
    while True:
        user_choise = input("Vuoi creare una nuova chat (1) o unirti ad una chat esistente? (2)\n>>> ")
        if user_choise == "1":
            chatID = "".join(random.choices(string.ascii_letters + string.digits, k= 5))
            first = True
            print(f"Chat ID: {chatID}")
            break

        elif user_choise == "2":
            chatID = input("Digita l'ID della chat (5 caratteri)\n>>> ")
            if len(chatID) != 5:
                print("ID non valido, riprova.")
                continue
            first = False
            break

        else:
            print("Comando non riconosciuto, riprova.")
            continue

    clientID = name + "".join(random.choices(string.ascii_letters + string.digits, k= 5))
    broker = "mqtt.eclipse.org"

    topic = "/prova/chat/mqtt/iot/" + chatID

    client = Client(clientID, broker, topic, name, first)

    client.start()
    time.sleep(1)
    try:
        while True:
            while client.wait:
                print(" Attendo...\r", end= "")
                time.sleep(0.5)
            client.myUnsubscribe() # per evitare di ricevere un messaggio mandato da sè stessi
            message = input(f"{name}: ")
            payload = {
                "clientID": clientID,
                "sender": name,
                "message": message,
                "time": str(datetime.now()),
                "torch": True
            }
            client.myPublish(json.dumps(payload))
            client.wait = True
            time.sleep(0.5) # necessario altrimenti non ha tempo di inviare il messaggio
            client.mySubscribe()

    except KeyboardInterrupt:
        client.stop()
