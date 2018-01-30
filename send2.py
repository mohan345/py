#!/usr/bin/python

import socekt
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto("hlw its sender1",("",80))

while True:
        p = str
        p=s.recvfrom(100)
        print "data from client : ",p[0]
        cliaddr = p[1]
        print "---------------------"
        print "---------------------"
        r = raw_input("type ypur reply:  ")
        s.sendto(r,p[1])
