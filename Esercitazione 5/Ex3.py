from Ex1sub import Subscriber
import time, json

def startSubscription(topic, sub):
    sub.topic = topic
    sub.start()
    time.sleep(1)
    while True:
        user_input = input().casefold()
        if user_input == "c":
            sub.stop()
            break
        else:
            print("Comando non riconosciuto, premi c per tornare al menu principale.")
            continue

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

    root_topic = f"/{clientID}/IoT s.p.a./"
    broker = "mqtt.eclipse.org"
    sub = Subscriber(clientID, root_topic, broker)
    while True:
        user_input = input("""What kind of data do you want to retrieve?
        a: data from the building
        f: data from a particular floor
        r: data from a particular room
        c: to go back to this menu
        q: to quit

>>>""").casefold()

        if user_input == "a":
            topic = root_topic + "#"
            startSubscription(topic, sub)
            continue

        elif user_input == "f":
            floor = int(input("Type the floor [0-->4]"))
            if floor >= 0 and floor <= 4:
                topic = root_topic + str(floor)+"/#"
                startSubscription(topic, sub)
                continue
            else:
                print("Input non valido, riprova.")
                continue

        elif user_input == "r":
            floor = int(input("Type the floor [0-->4]"))
            if floor >= 0 and floor <= 4:
                room = int(input("Type the room [1-->3]"))
                if room >= 1 and floor <= 3:
                    topic = root_topic + str(floor) + "/" + str(room) + "/#"
                    startSubscription(topic, sub)
                    continue
            else:
                print("Input non valido, riprova.")
                continue
        elif user_input == "c":
            continue

        elif user_input == "q":
            break

        else:
            print("Input non valudo, riprova.")
            continue
