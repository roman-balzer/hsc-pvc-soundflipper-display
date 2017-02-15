from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import display

## RequestHandler is used to restrict RPC calls to a specific path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

## Represents the functionality used to register RPC functions
class ServerHandler:
    ## Member variables score and mulipliator ar set to default values.
    # Functions are registered. 
    # Standard text is written to display.
    # Server starts and runs forever.
    def __init__(self):
        self.score = 0
        self.muliplicator = 1

        # Create server
        self.server = SimpleXMLRPCServer(("0.0.0.0", 4000),
                                    requestHandler=RequestHandler, allow_none=True)
        self.server.register_introspection_functions()
        self.server.register_function(self.setMultiplicator, 'setMultiplicator')
        self.server.register_function(self.addPoints, 'addPoints')
        self.server.register_function(newGame, 'newGame')

        display.writeScore(score)
        display.writeText('Score: ')

        # Run the server's main loop
        server.serve_forever()

    ## Sets the Multiplicator. 
    def setMultiplicator(self, mult):
        self.muliplicator = mult

    ## Adds newpoints to current score. 
    # Newpoints are muliplied with muliplicator.
    # The new score is sent to the display.
    def addPoints(newpoints):
        self.score = self.score + (newpoints * self.muliplicator)
        display.writeScore(self.score)
    
    ## Starts a new game. Score is set to zero.
    # Multiplicator is set to 1.
    # Score is sent to display.
    def newGame():
        self.score = 0
        self.multiplicator = 1
        display.writeScore(score)

#Initialize Server
server = ServerHandler()

