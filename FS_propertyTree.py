#!/usr/bin/python

class Engine:
    """initializes an Engine"""
    def __init__(self):
        self.reverser=False
        self.throtle_rev=0
        self.reverser_angle_rad=0

    """For testing purposes prints the engine current values"""
    def __str__(self):
        return """The engine reverser value is %s, 
               throtle reverser is %f, 
               and reverser angle is %f rads""" % (self.reverser, self.throtle_rev, self.reverser_angle_rad)
