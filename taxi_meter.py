# Taxi meter exercise

class TaxiMeter():
    def __init__(self, milesTraveled):
        self.miles = milesTraveled    
    
    def getFare(self):
        print "Your trip was %r miles long" % self.miles
        print "...and it cost you %r dollars" % (self.miles * 3)
        
while True:
    question = raw_input("Would you like to play the game? yes/no: ")
    if question == "yes":
        trip = TaxiMeter(input("How long was your trip: "))
        trip.getFare()
    else:
        break
    

        