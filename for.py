#!/usr/bin/evn python

import time
x=raw_input()
y=raw_input()
z=raw_input()
w=raw_input()

t=(x,y,z,w)

for i in t:
    if i==x:
        print x
        
    if i==y:
        print int(y)+int(x)
        
    if i==z:
        print int(x)+int(y)+int(z)
        
    if i==w:
        print int(x)+int(y)+int(z)+int(w)
        

time.sleep(0)


