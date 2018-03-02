#!/usr/bin/python
from FS_propertyTree import Gear
from Engine727 import *

###########TESTING################

print """
Testing Begins by creating the Engine Stack\n
"""
##Create the stack of 3 engines for B727
engines=[Engine727() for engines in range(3)]
##Create the stack of 2 Gears for B727
gears=[Gear() for gears in range(2)]

#Show them
for myEngine in engines:
    print myEngine

print """
__________________________________________________________________\n
Testing Continues by modifying the throtle_rev of the second engine to 0.25 specifically\n
The Engine 1 values now are:
"""
#modifying and showing the second engine (engines[1]) of the stack
engines[1].throtle_rev=0.25
print engines[1]

print "My 727 engine manufacturer is " + engines[1].manufacturer + "\n"

print """
__________________________________________________________\n
Testing ends by sending the toggleFastRevThrust function to all the engines of the stack\n
"""
for myEngine in engines:
    if gears[0].wow and gears[1].wow: #test whether gears Wow 
        myEngine.toggleFastRevThrust()
        print myEngine

print """Toggle"""
for myEngine in engines:
    if gears[0].wow and gears[1].wow: #test whether gears Wow
        myEngine.toggleFastRevThrust()
        print myEngine



