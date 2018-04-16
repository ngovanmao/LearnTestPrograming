#!/usr/bin/python

import socket
import binascii
from threading import Thread


UDP_IP = ""
UDP_PORT= 9999

i = 0

def client_thread(conn, ip, port):
    global i
    print("open a new connection from {}:{}".format(ip, str(port)))
    while True:
        img_size = conn.recv(8)
        #print("img_size = {}".format(str(img_size)))
        if img_size == '': break
        start_time = time.time()
        (length,) = unpack('>Q', img_size)
        i += 1
        fname = str(i) + '.jpg'
        fp = open(fname, 'wb')
        data = b''
        while len(data) < length:
            to_read = length - len(data)
            data += conn.recv(
                4096 if to_read > 4096 else to_read)
        fp.write(data)
        fp.close()
        transfer_time = time.time() - start_time
        start_time = time.time()
        r = infer([fname])
        str_r = str(i) + ' ' + str(r) + ' transfer ' + str(transfer_time) + ' process ' + str(time.time() -start_time)
        #print(str_r)
        conn.send(str_r + '\n' )
        os.remove(fname)
        #print("OK ")
    conn.close()




def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((UDP_IP, UDP_PORT))
    server.listen(4)
    while True:
        print("Multithreaded Python server: waiting for connections from TCP clients...")
        (conn, (ip, port)) = server.accept()
        Thread(target=client_thread, args=(conn, ip, port)).start()
        

main()

