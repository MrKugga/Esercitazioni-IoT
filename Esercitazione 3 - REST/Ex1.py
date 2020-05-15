import cherrypy

@cherrypy.expose
class ReverseString:

    def GET(self, *uri, **params):
        if len(uri) != 0:
            output = []
            for uro in uri:
                output.append(uro[::-1])
            return output
        else:
            raise cherrypy.HTTPError(404, "Uri not found. That's all we know.")

if __name__ == "__main__":
    conf = {
    "/": {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'tool.session.on': True
        }
    }

    cherrypy.tree.mount(ReverseString(), "/", conf)

    cherrypy.engine.start()
    cherrypy.engine.block()
