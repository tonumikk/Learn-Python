from sys import exit

class Chillin(object):
    """It's 8pm on a Friday night in Madison. You're lounging on the couch with your 
roommates watching Dazed and Confused. What is your first drink?
    1. beer
    2. whiskey
    3. vodka
    4. bowl
"""
    def __init__(self):
        self.prompt = '> '

    def proceed(self):
        drink = raw_input(self.prompt)

        if drink == '1' or drink == 'beer':
            print '\n Anytime is the right time.'
            print 'You crack open the first beer and sip it down.'
            room = Pregame()
            return room
        #rest of drinks will be written the same way


class Pregame(object):
    """It's time to really step up your pregame.
How many drinks do you take?
"""

    def proceed(self):
        drinks = raw_input('> ')
    #and so on