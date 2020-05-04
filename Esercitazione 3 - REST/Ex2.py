import cherrypy
import json

@cherrypy.expose
class ReverseStringParams:

    def GET(self, *uri, **params):

        output = {}
        if params != {}:
            for key, value in params.items():
                output[key] = value[::-1]

            return json.dumps(output)
        else:
            raise cherrypy.HTTPError(400, "I don't know what you want me to do.")


if __name__ == "__main__":

    conf = {
    "/": {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'tool.session.on': True
        }
    }

    cherrypy.tree.mount(ReverseStringParams(), "/", conf)

    cherrypy.engine.start()
    cherrypy.engine.block()
