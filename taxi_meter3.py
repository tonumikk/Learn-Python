class TaxiMeter(object):
    def __init__(self, milesTraveled): # Gets the TaxiMeter ready for input
        self.miles = milesTraveled    
        
    def fare(self): # fare is method of the TaxiMeter class
        self.fare_a = self.miles*3
        
        

class InputOutput(object):
        
    while True:
        question = raw_input("Would you like to play the game? yes/no: ")
        if question == "yes":
            trip = input("How long was your trip: ")
            trip_a = TaxiMeter(trip) # makes an instance of the TaxiMeter class
            print "You traveled %r miles" % trip_a.miles
            trip_a.fare() # calls the fare method
            print "... and it costs you %r dollars" % trip_a.fare_a        
        else:
            break
    
InputOutput() 