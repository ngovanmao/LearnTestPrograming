#!/usr/bin/python

import socket
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--ipaddr',
        type=str,
        help='IP address of the requesting server',
        default='localhost')
    parser.add_argument(
        '--port',
        type=int,
        help='Listenning port in the requesting server',
        default=9999)
    parser.add_argument(
        '--msg',
        type=str,
        help='Message will be sent to the server',
        default='hello world')
    args = parser.parse_args()
    HOST = args.ipaddr
    PORT = args.port
    data = args.msg
    print('Requesting to:', HOST, ":", PORT)


    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n"))
    
        # Receive data from the server and shut down
        received = sock.recv(1024)
    finally:
        sock.close()
    
    print("Sent:     {}".format(data))
    print("Received: {}".format(received))

if __name__ == '__main__':
    main()
