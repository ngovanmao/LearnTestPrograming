#!/usr/bin/python
import sys
if sys.version_info[0] >= 3:
    import socketserver as skServer
else:
    import SocketServer as skServer
i = 0
class MyTCPHandler(skServer.BaseRequestHandler):
    
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        global i 
        # self.request is the TCP socket connected to the client
        i += 1
        self.data = self.request.recv(1024).strip() + ' ' + str(i)
        #print("i = {}, {} wrote:".format(i, self.client_address[0]))
        #print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "", 9999

    #print("server open at port = ", PORT)
    # Create the server, binding to localhost on port 9999
    server = skServer.TCPServer((HOST, PORT), MyTCPHandler)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
