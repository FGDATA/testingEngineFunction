#!/usr/bin/python
#import the default Gear and import the modified EngineJet_reverser Engine727
#and use it to test the functionality
from FS_propertyTree import Gear
from Engine727 import Engine727

###########TESTING################

print """
Testing Begins by creating the Engine Stack and the Craft Gears\n
"""
engines=[Engine727() for engines in range(3)]
gears=[Gear() for gears in range(3)]

#Show these engines
for myEngine in engines:
    print myEngine

print """
__________________________________________________________________\n
Testing Continues by modifying the throtle_rev of the second engine to 0.25 specifically\n
The engines[1] values now are:
"""
#modifying and showing the second engine (engines[1]) of the stack
engines[1].throtle_rev=0.25
print engines[1]

#testing the new node of a 727 Engine; manufacturer
print "My 727 engine manufacturer is " + engines[1].manufacturer + "\n"

#Testing the toggleFastRevThrust function, twice to see it does toggle in fact
print """
__________________________________________________________\n
Testing ends by sending the toggleFastRevThrust function to all the engines of the stack\n
"""

print """Toggle"""
for myEngine in engines:
    if all(gears): #test whether all gears Wow
        myEngine.toggleFastRevThrust()
    print myEngine

print """Toggle"""
for myEngine in engines:
    if gears[0].wow and gears[1].wow: #test whether gears Wow
        myEngine.toggleFastRevThrust()
    print myEngine

##Toggle the Gears now, 
for myGears in gears:
    myGears.toggleGear()
#and test that can't reverse anymore
print """Toggle not executed because gears.wow are false now"""
for myEngine in engines:
    if gears[0].wow and gears[1].wow: #test whether gears Wow
        myEngine.toggleFastRevThrust()
    print myEngine



