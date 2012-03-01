from game_map import *

class Runner(object):
    def __init__(self, start):
        self.start = start

    def play(self):
        next_room = self.start

        while True:
            print '\n'
            print '-' * 7
            print next_room.__doc__
            next_room = next_room.proceed()

firstroom = Chillin()

my_game = Runner(firstroom)

my_game.play()