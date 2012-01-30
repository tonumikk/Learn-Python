print "Who picks up kids from pool?"

print """
    There are three kids:  Annika, Oliver and Chloe 
    and 3 parents: Chloe's mom Rebecca, Annika and Olivers mom and dad
    Barbara and Tonu.  Your answers to the questions will determine who picks 
    up kids from pool based on kids swimming schedule, sickness and parent 
    availability""" 

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 
play_again = True

def end_game(why):
    """The end_game function will allow you to start playing the game again or end it."""
    print why
    keep_going = raw_input("Would you like to play again?: ")

    if keep_going == "no":
        play_again = False
    elif keep_going == "yes":
        pickday()
    else:
        print "All right, you typed '%s'.  I will take it as a 'Yes!'" % keep_going
        pickday()

def pickday():
    """The pickday function will determine what day of the week is picked for the game day
    If the day is not correct, you can start playing again from the beginning."""
    gameday = raw_input("Pick a day of the week: ")
    gameday 

    if gameday in weekday:
        print "You picked %s" % gameday
        right_day(gameday) 
    else:
        print "Sorry, %s is not a weekday.  Your options are 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' or 'Sunday'" % gameday
        end_game("You mistyped the weekday.")

def right_day(gameday):
    """The right_day function determines if there is swimming on a given weekday.  If not, you can start playing again from the beginning."""

    if gameday == "Tuesday" or gameday == "Wednesday" or gameday == "Thursday":
        sick_child(gameday)
    else:
        end_game("There is no swimming on Mondays, Fridays, Saturdays or Sundays.")  

def who_sick(gameday):
    """The who_sick function determines who is sick"""
    sick_person = raw_input("Who is sick?: ")
    print "I see, %s is sick today" % sick_person

    if sick_person == "Oliver" and gameday == "Wednesday":
        print "Since it is Wednesday and Oliver is sick, there are no kids who need rides from pool today."
        end_game("Thanks, this ends the game!")
    elif sick_person == "Chloe" and gameday == "Tuesday":
        print "Oh darn, Rebecca cannot give a ride on %s because Chloe is sick.  It would have to be either Barbara or Tonu." % gameday
        barbara_available(gameday)
    else:
        print "The sickness doesn't matter on %s.  We still need to give rides to healthy kids." % gameday
        run_normal(gameday)

def sick_child(gameday):
    """The sick_child function checks if any of the kids is sick and will decide which function to run next. """
    anyone_sick = raw_input("Are any of the kids sick today?: ")

    if anyone_sick == "yes":
        print "Too bad, we have to make special arrangements."
        who_sick(gameday)
    elif anyone_sick == "no":
        print "Good, we have a normal schedule on %s." % gameday
        run_normal(gameday)
    else:
        end_game("Sorry you need to type either 'yes' or 'no'.") 

def run_normal(gameday):
    """ The run_normal function will decide who picks up kids if no kid is sick """

    if gameday == "Tuesday":
        print "Excellent, Rebecca will pick up kids on %s." % gameday
        end_game("Thanks, this ends the game!")
    else:
        barbara_available(gameday)

def barbara_available(gameday):
    """ The barbara_available function will decide if Barbara is available and decide the driver accordingly. """
    b_available = raw_input("Is Barbara available today: ")

    if b_available == "yes":
        print "Wonderful, Barbara will pick up kids on %s." % gameday
        end_game("Thanks, this ends the game!")
    elif b_available == "no":
        print "Ok, Tonu will pick up kids on %s." % gameday
        end_game("Thanks, this ends the game!")
    else:
        end_game("Sorry you need to type either 'yes' or 'no'.")           

# Run the program
pickday()

# If play_again gets set to False, the game exits
exit(0)
