class TaxiMeter(object):
    def __init__(self, milesTraveled):
        self.miles = milesTraveled    
        print "Your trip was %r miles long" % self.miles
        self.fare()
    def fare(self):    
        self.fare = (self.miles * 3)
        print "...and you paid %r dollars" % self.fare

class InputOutput(object):
        
    while True:
        question = raw_input("Would you like to play the game? yes/no: ")
        if question == "yes":
            trip = input("How long was your trip: ")
            TaxiMeter(trip) # calls to TaxiMeter class with trip instance.  Trip gets passed as an argument.
        else:
            break
    
InputOutput() 