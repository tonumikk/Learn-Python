print "Loop test"

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 
gameday = raw_input("Pick a day of the week: ")

def end_game(why):
    """This will end the game stating the reason why"""
    print why, "Thanks for playing!"
    exit(0)

def pickday():
    """The pickday function will determine what day of the week is picked for the game day
    If the day is not correct, the game ends."""
    gameday 
    if gameday in weekday:
        print "You picked %s" % gameday
    else:
        print "Sorry, %s is not a weekday.  Your options are 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' or 'Sunday'" % gameday
        try_again = raw_input("Would you like to try again? ")

def try_again():
    if try_again == "yes":
        pickday()
    else: 
        end_game("Ok, The game will exit")

while try_again == "yes":
    pickday()
    
