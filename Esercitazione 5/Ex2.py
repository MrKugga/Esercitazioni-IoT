import cherrypy, json, time
from Ex1pub import Publisher
from datetime import datetime



@cherrypy.expose
class WebLamp:

    def GET(self, *uri, **params):
        with open("index.html", "r") as f:
            output = f.read()

        return output

    def PUT(self, *uri, **params):

        if uri[0] == "On":
            ledOn = True
            sendMessage(ledOn)
        elif uri[0] == "Off":
            ledOn = False
            sendMessage(ledOn)
        else:
            raise cherrypy.HTTPError(400, "Bad Request")

def sendMessage(ledOn):
    global pub

    instructions = {
    "led_on": ledOn,
    "date": str(datetime.now()),
    "clientID": publisherID
    }
    pub.myPublish(json.dumps(instructions))

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
publisherID = clientID+"p"
pub = Publisher(publisherID, topic, broker)
time.sleep(1)

if __name__ == "__main__":

    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        }
    }

    pub.start()

    try:
        cherrypy.tree.mount(WebLamp(), "/", conf)
        cherrypy.engine.start()
        cherrypy.engine.block()

    except KeyboardInterrupt:
        pub.stop()
        print("Exiting")
