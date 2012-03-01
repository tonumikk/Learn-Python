# Taxi meter exercise

"""
Taxi meter exercise demonstrates how to use two classes for inputting miles travelled, calculating the taxi fare
and then displaying the miles travelled and taxi fare.  The calculation for taxi fare is separated into it's own class TaxiMeter,
and input of miles travelled (trip) and taxi fare are in a class called InputOutput.  
"""

# Version 1 where TaxiMeter class gets input, performs the calculation and displays the results
# This uses only one class.

# Version 2 where TaxiMeter does NOT have a method for calculating the fare.

class TaxiMeter(object):
    def __init__(self, milesTraveled):
        self.miles = milesTraveled    
        self.fare = (self.miles * 3)
        print self.miles
        print self.fare

class InputOutput(object):
        
    while True:
        question = raw_input("Would you like to play the game? yes/no: ")
        if question == "yes":
            trip = input("How long was your trip: ")
            TaxiMeter(trip) # calls to TaxiMeter class with trip instance.  Trip gets passed as an argument.
        else:
            break
    
InputOutput() 
        


# Version 3 where TaxiMeter has a method for calculating the fare.        