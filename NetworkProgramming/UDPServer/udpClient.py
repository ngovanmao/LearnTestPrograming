#!/usr/bin/python

import socket
import time 
#UDP_IP = "aaaa::12:4b00:060d:9ef7"
#UDP_IP = "aaaa::12:4b00:0615:a59e"
#For command trigger
#UDP_IP = "aaaa::9999"
UDP_IP = "fd00::9999"
#UDP_IP = "aaaa::1"
#UDP_PORT= 5688
#UDP_PORT= 8775
#UDP_IP = "localhost"
UDP_PORT = 9997
# syntax: "tg <traffic_scale> <extra_timeslots> <duration> <scheduler_type> <node>"
# Scheduler_type = 1 MITA - equally spaced extra timeslots
# Scheduler_type = 2 CONCAT - concatenated extra timeslots
# Scheduler_type = 3 RANDOM - random extra timeslots
# Node = {0, 1, 2} are equivalent to {ECG, ACC, TEM}
# Ex: Increase 4 times, 2 timeslots, 120 seconds, scheduler = 1, node=ecg.
MESSAGE = "tg 4 2 120 1 0"

ms = ["tg 1 0 120 1 0", "tg 1 0 120 2 1", "tg 1 0 120 3 2", \
      "tg 1 1 120 1 0", "tg 1 1 120 2 1", "tg 1 1 120 3 2", \
      "tg 1 2 120 1 0", "tg 1 2 120 2 1", "tg 1 2 120 3 2", \
      "tg 1 3 120 1 0", "tg 1 3 120 2 1", "tg 1 3 120 3 2", \
      "tg 2 0 120 1 0", "tg 2 0 120 2 1", "tg 2 0 120 3 2", \
      "tg 2 1 120 1 0", "tg 2 1 120 2 1", "tg 2 1 120 3 2", \
      "tg 2 2 120 1 0", "tg 2 2 120 2 1", "tg 2 2 120 3 2", \
      "tg 2 3 120 1 0", "tg 2 3 120 2 1", "tg 2 3 120 3 2", \
      "tg 4 0 120 1 0", "tg 4 0 120 2 1", "tg 4 0 120 3 2", \
      "tg 4 1 120 1 0", "tg 4 1 120 2 1", "tg 4 1 120 3 2", \
      "tg 4 2 120 1 0", "tg 4 2 120 2 1", "tg 4 2 120 3 2", \
      "tg 4 3 120 1 0", "tg 4 3 120 2 1", "tg 4 3 120 3 2"]
   
# 15 minutes
#MESSAGE = "tg 4 2 900"
# Increase 4 times, 0 timeslots, 120 seconds.
#MESSAGE = "tg 4 0 300"
#MESSAGE = "ter2 2 40"


sock = socket.socket(socket.AF_INET6,   #IPv6
                    socket.SOCK_DGRAM) # UDP
# we send each triggered command every 3 minutes. Each command last 2 minutes
# A minute in between is to stabilize the system.
for m in ms:
    sock.sendto(m, (UDP_IP, UDP_PORT))
    print m
    print 'st=',time.time()*1000 
    print time.ctime()
    time.sleep(3*60)


