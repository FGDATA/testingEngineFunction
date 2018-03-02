from FS_propertyTree import EngineJet_reverser
##Importing the Default EngineJet_reverser and modify it by inheritance

class Engine727(EngineJet_reverser):
    """
    initialization of Classes could be a neat way of adding new nodes to the property tree
    and expanding a basic configuration;
    like here /engine[N]/manufacturer and 
              /engine[N]/model
    """
    def __init__(self):
        EngineJet_reverser.__init__(self)
        self.manufacturer="Pratt & Whitney"
        self.model="JT8D-1/7/9"
    
    """The rev thrust function gets overloaded to mimmic the Nasal file example"""
    def toggleFastRevThrust(self):
        if not self.reverser and self.throtle_pos<=0.05:
            self.throtle_rev=0.5
            self.reverser_angle_rad=3.14
            self.reverser_pos_norm=1
            self.reverser=True
            return self.reverser
        if self.reverser:
            self.throtle_rev=0
            self.reverser_angle_rad=0
            self.reverser_pos_norm=0
            self.reverser=False
            return self.reverser
