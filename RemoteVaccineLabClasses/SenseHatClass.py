##########################################################
# SenseHat Class File                                    #
# date: Nov 15 2020                                      #
# name: Harshil Verma                                    #
##########################################################



class SenseHat:
    
    def __init__(self, temperature, pressure):
        self.temperature = temperature
        self.pressure = pressure 
    
    
    def getTemp(self):
        return self.temperature
    
        
    def getPress(self):
        return self.pressure
        
      
