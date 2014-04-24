import json
import cherrypy

class Notifications(object):
	exposed = True
	def GET(self, id=None):
		return "hello world"

if __name__ == '__main__':
    
    
    #cherrypy.config.update('conf.ini')
    #cherrypy.config.update('app.conf')

    app = cherrypy.tree.mount(Notifications(), '/api/notifications', 
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    #app.merge('app.conf')
    if hasattr(cherrypy.engine, 'block'):
        # 3.1 syntax
        cherrypy.engine.start()
        cherrypy.engine.block()
    else:
        # 3.0 syntax
        cherrypy.server.quickstart()
        cherrypy.engine.start()
