#!/usr/bin/python

import socket
import binascii
import numpy as np
import time

#UDP_IP = "aaaa::1"
UDP_IP = "fd00::1"
UDP_PORT= 5688

sock = socket.socket(socket.AF_INET6,  #both ipv6 and ipv4 INET6,   #IPv4
                    socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

# Data format: systemtime, node_id, sensors..., sensortime
def parserData(data, addr):
    #length = len(data) - 4 
    ipv6Addr = addr[0]
    lastIpv6Addr = (int(ipv6Addr[-4 : -2], 16) & 0xff) +\
                    ((int(ipv6Addr[-2 : ], 16) & 0xff) << 8)
    payload = binascii.hexlify(data)
    outData = np.array([], dtype=int)
    outData = np.append(outData, time.time() * 1000)
    outData = np.append(outData, lastIpv6Addr)
    i = 0
    while i < len(payload) - 4:
        d = (int(payload[i+4 : i+6], 16) & 0xff) + ((int(payload[i+6 : i+8], 16) & 0xff) << 8)
        outData = np.append(outData, d)
        i += 4
    return outData 

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #payload = data.encode('hex')
    print "received message from ", addr, "with ", binascii.hexlify(data)
    #outData = parserData(data, addr)
    #print "received from ", addr, "with ", outData
    #print "received message from ", addr, "with ", repr(data)
