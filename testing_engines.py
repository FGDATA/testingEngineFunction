#!/usr/bin/python

from FS_propertyTree import Engine
     ##Now the Engine Class has been imported.

class Engines727(Engine):  
    """The rev thrus function"""
    def toggleFastRevThrust(self):
        self.reverser=True
        self.throtle_rev=0.5
        self.reverser_angle_rad=3.14

###########TESTING################

print """
Testing Begins by creating the Engine Stack\n
"""
##Create the stack of 3 engines for B727
engines=[Engines727() for engines in range(3)]
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

print """
__________________________________________________________\n
Testing ends by sending the toggleFastRevThrust function to all the engines of the stack\n
"""
for myEngine in engines:
    myEngine.toggleFastRevThrust()
    print myEngine



