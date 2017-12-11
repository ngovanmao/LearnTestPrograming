#!/usr/bin/python

import SocketServer
from struct import unpack

i = 0
class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        global i
        i += 1
        fname = str(i) + '.jpg'
        fp = open(fname, 'wb')
        img_size = self.request.recv(8)
        (length,) = unpack('>Q', img_size)
        data = b''
        while len(data) < length:
            to_read = length - len(data)
            data += self.request.recv(
                4096 if to_read > 4096 else to_read)
        fp.write(data)
        fp.close()

        print "{} wrote:".format(self.client_address[0])
        print("Image received successfully.") 
        self.request.sendall('OK '+str(i) + '\n')
        print("ACK OK "+ str(i))
        # just send back the same data, but upper-cased

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
