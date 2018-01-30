#!/usr/bin/python_

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",80))
while True:
        data = s.recvfrom(100)
        print "data from client : ",data[0]
        cliaddr = data[1]
        x = os.system('' +str(data[0]))
        print "--------------------------"
        if x == True:
                j = os.system('' +str(data[0]))
                s.sendto(j,cliaddr[1])
        else:
                r = raw_input()
                s.sendto(r,cliaddr[1])

        print "-------------------------------"
