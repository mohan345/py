#!/usr/bin/python

import time

x=raw_input("enter anyhting")
x=int(x)
if x==1:
        print x
elif x==2:
        time.sleep(2)
        print x
elif x==3:
        z=raw_input()
        y=raw_input()
        print int(z) + int(y)
elif x==4:
        w=raw_input()
        e=raw_input()
        d=w+e
        print d
else:
        print "wrong input"



time.sleep(0)



