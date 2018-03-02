#!/usr/bin/python

class EngineJet:
    """initializes an Engine"""
    def __init__(self):
        self.throtle_pos=0

    def __str__(self):
        return "The engine throtle_pos is %f" %(self.throtle_pos)

class EngineJet_reverser(EngineJet):
    """initializes an EngineJet then add the Reverser"""
    def __init__(self):
        EngineJet.__init__(self)
        self.reverser=False
        self.throtle_rev=0
        self.reverser_angle_rad=0
        self.reverser_pos_norm=0

    """For testing purposes prints the engine current values"""
    def __str__(self):
        return """The engine reverser value is %s, 
        throtle reverser is %f, 
        throtle_pos is %f,
        and reverser angle is %f rads""" %(self.reverser,
                                           self.throtle_rev,
                                           self.throtle_pos, 
                                           self.reverser_angle_rad)
    
    """The default and simpler rev thrust function"""
    def toggleFastRevThrust(self):
        if not self.reverser:
            self.reverser=True
            return self.reverser
        if self.reverser:
            self.reverser=False
            return self.reverser

class Gear:
    def __init__(self):
        self.wow=True

    def __str__(self):
        return self.wow

    def toggleGear(self):
        if self.wow:
            self.wow=False
            return self
        if not self.wow:
            self.wow=True
            return self
