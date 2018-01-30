#!/usr/bin/python

import socket
def localhostinfo():
        h = socket.gethostname()
        i = socket.gethostbyname(h)
        print "host name :",h
        print "ip address :", i


localhostinfo()
