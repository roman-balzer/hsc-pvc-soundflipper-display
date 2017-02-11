from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import display

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

score = 0


# Create server
server = SimpleXMLRPCServer(("0.0.0.0", 4000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()


# Register a function under a different name
def addPoints(newpoints):
    global score
    score = score + newpoints
    display.writeScore(score)
    return score
server.register_function(addPoints, 'addPoints')

def newGame():
    global score
    score = 0
    display.writeScore(score)
    return score
server.register_function(newGame, 'newGame')

def init():
    global score
    score = 0
    display.writeScore(score)
    display.writeText('Score: ')

init()

# Run the server's main loop
server.serve_forever()