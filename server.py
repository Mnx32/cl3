from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    if n<=1:
        return n
    return n*factorial(n-1)

server = SimpleXMLRPCServer(("localhost",8000))

server.register_function(factorial,"compute_factorial")

server.serve_forever()
