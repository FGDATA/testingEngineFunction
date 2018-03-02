#!/usr/bin/python

from FS_propertyTree import Engine, Gear
     ##Now the Engine and Gear classes has been imported.

class Engines727(Engine):
    """Overload the init Test"""
    def __init__(self):
        Engine.__init__(self)
        """
        initialization of Classes could be a neat way of adding new nodes to the property tree
        and expanding a basic configuration;
        like here /engine[N]/manufacturer and 
                  /engine[N]/model
        """
        self.manufacturer="Pratt & Whitney"
        self.model="JT8D-1/7/9"
    
    """The rev thrus function"""
    def toggleFastRevThrust(self):
        if not self.reverser and self.throtle_pos<=0.05:
            self.reverser=True
            self.throtle_rev=0.5
            self.reverser_angle_rad=3.14
            self.reverser_pos_norm=1
            return True
        if self.reverser:
            self.reverser=False
            self.throtle_rev=0
            self.reverser_angle_rad=0
            self.reverser_pos_norm=0
            return True
            

###########TESTING################

print """
Testing Begins by creating the Engine Stack\n
"""
##Create the stack of 3 engines for B727
engines=[Engines727() for engines in range(3)]
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



