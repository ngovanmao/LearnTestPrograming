#!/usr/bin/python

import socket
import binascii
import time
from struct import unpack

UDP_IP = ""
UDP_PORT= 9999

i = 0




def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((UDP_IP, UDP_PORT))
    print("Python UDP server: Port {}".format(UDP_PORT))
    global i
    while True:        
        img_size, client_addr = server.recvfrom(1024)
        print("img_size = {}".format(str(img_size)))
        if img_size == '': break
        start_time = time.time()
        #(length,) = unpack('>Q', img_size)
        length = int(img_size[2:])
        print("length = {}".format(length))
        i += 1
        fname = str(i) + '.jpg'
        fp = open(fname, 'wb')
        data = b''        
        while len(data) < length:
            to_read = length - len(data)            
            temdata, client_addr = server.recvfrom(
                1024 if to_read > 1024 else to_read)
            print(temdata)
            data += temdata
            print("data={}, length data={}".format(data, len(data)))
        fp.write(data)
        fp.close()
        transfer_time = time.time() - start_time
        start_time = time.time()
        r = infer([fname])
        str_r = str(i) + ' ' + str(r) + ' transfer ' + str(transfer_time) + ' process ' + str(time.time() -start_time)
        #print(str_r)
        server.sendto(str_r + '\n' , client_addr)
        os.remove(fname)
        #print("OK ")
        server.close()
    
        

main()

