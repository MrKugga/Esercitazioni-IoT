import cherrypy

@cherrypy.expose
class HelloWorld(object):
    def GET(self, *uri, **params):
        output = "Hello World!"

        if len(uri) != 0:
            output += '<br>uri: '+','.join(uri) #String.join(iterable) concatena l'iterabile con la stringa separatore

        if params != {}:
            output += '<br>params: ' +str(params)

        return output

if __name__ == "__main__":
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tool.session.on': True
        }
    }
    cherrypy.quickstart(HelloWorld(), '/', conf)
