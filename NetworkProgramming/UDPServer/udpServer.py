#!/usr/bin/python

import socket
import binascii

UDP_IP = ""
UDP_PORT= 8888

print("Open a UDP server with port = ",UDP_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((UDP_IP, UDP_PORT))


def main():
    running = True
    while running:
        print("Open a UDP server with port = ",UDP_PORT)
        try:
            data, client_addr = sock.recvfrom(1024) 
        except KeyboardInterrupt:
            running = False
            sock.shutdown(socket.SHUT_RDWR) 
            sock.close()
        if data:
            print("received message from {} with {}".format(client_addr, data))
            sent = sock.sendto(data.upper(), client_addr)
        elif data == "close":             
            print("received message from {} with {}".format(client_addr, data))
            sent = sock.sendto(data.upper(), client_addr)
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            running = False   
        

main()

