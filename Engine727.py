from FS_propertyTree import Engine
     ##Now the Engine and Gear classes has been imported.

class Engine727(Engine):
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
