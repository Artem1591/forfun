from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from sql_insert import insert
from sql_delete import deleteID
from sql_select import selectAll, selectByID

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler, allow_none=1)

server.register_function(selectByID)
server.register_function(selectAll)
server.register_function(insert)
server.register_function(deleteID)

# Run the server's main loop
server.serve_forever()