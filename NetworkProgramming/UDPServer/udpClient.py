
import socket
import time 

UDP_IP = "192.168.1.95"
UDP_PORT = 8888
server_address = (UDP_IP, UDP_PORT)
message = input("Input>")


sock = socket.socket(socket.AF_INET,   #IPv6
                    socket.SOCK_DGRAM) # UDP
print("message = ", message)
sock.sendto(message, server_address)
data, fromaddr = sock.recvfrom(1024)
print("return message {} from {}".format(data, fromaddr))


