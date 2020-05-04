import cherrypy
import json

@cherrypy.expose
class WebService:

    def PUT(self, *uri, **params):
        self.content = json.loads(cherrypy.request.body.read()) 

        return f'The keys are {self.content.keys()} and the values are {self.content.values()}'

if __name__ == "__main__":

    conf = {
        "/": {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tool.session.on': True
        }
    }

    cherrypy.tree.mount(WebService(), "/web", conf)

    cherrypy.engine.start()
    cherrypy.engine.block()
