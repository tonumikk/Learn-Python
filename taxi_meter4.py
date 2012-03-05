taxi_driver_day = [] # list to store taxi ride objects

class TaxiMeter(object):
    passanger_count = 0 # sets some initial values for totals
    total_miles = 0
    total_fare = 0
    
    def __init__(self, milesTraveled, passangerName, passangerDestination): # Gets the TaxiMeter ready for input
        self.miles = milesTraveled
        self.passanger = passangerName
        self.destination = passangerDestination
        TaxiMeter.passanger_count += 1
        TaxiMeter.total_miles += self.miles # adds trip miles to the previous total trip miles
        
    def __str__(self):
        message = "Name: " + self.passanger + ", "
        message = message + "Destination: " + self.destination + ", "
        message = message + "Miles Travelled: " + str(self.miles) + ", "
        message = message + "Fare: " + str(self.fare_a)
        print "\n"
        return message
    
    def fare(self): # fare is method of the TaxiMeter class
        self.fare_a = self.miles*3
        TaxiMeter.total_fare += self.fare_a # add trip fare to the previous total trip fare
    
class InputOutput(object):
    
    print """
You are a taxi driver.  You just started your work day.  You see a 
passanger hailing a cab.
    """        
    while True:
        question = raw_input("You ask yourself: 'Am I up for a trip?' yes/no: ")
        if question == "yes":
            print "You stop and greet the passenger."
            name = raw_input("Hello what is your name?: ")
            destination = raw_input("...and where would you like to go today?: ")
            print "You drive %s to %s" % (name, destination)
            trip = input("How long was your trip: ")
            trip_a = TaxiMeter(trip, name, destination) # makes an instance of the TaxiMeter class
            print "%s traveled %r miles to the %s" % (trip_a.passanger, trip_a.miles, trip_a.destination)
            trip_a.fare() # calls the fare method
            print "... and it cost him/her %r dollars" % trip_a.fare_a
            taxi_driver_day.append(str(trip_a)) # adds each instance to the list as a new item
        else:
            print "That ends your work today!"
            print "Here are your rides for today ..."
            
            for item in taxi_driver_day: # print the list each item in it's own row
                print item
            
            print "Here are your daily totals ... "
            #number_of_passangers = len(taxi_driver_day)    - This is another way to get passanger count                       
            print "You gave rides to %r passangers" % TaxiMeter.passanger_count
            print "You traveled a total of %r miles" % TaxiMeter.total_miles
            print "... and you collected a total of %r dollars" % TaxiMeter.total_fare
            break

InputOutput() 

