#!/usr/bin/env python
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("192.168.10.65",8888))

while True:
    s.sendto("hellosir",("192.168.10.65",8888))


