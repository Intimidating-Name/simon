import random
import time
import os
import sys


class Game:
    """game controller"""

    def __init__(self, max_levels):
        self.over = False
        self.simon = Simon()
        self.player = Player()
        self.level = self.simon.get_level_number()
        self.max_levels = max_levels

    def next_level(self):
        print("next level")
        self.simon.add_color()
        self.player.increase_score()
        self.print_level()
        self.test_player()

    def print_level(self):
        for x in self.simon.history:
            print(x)
            time.sleep(1)
            os.system('clear')

    def test_player(self):
        for x in self.simon.history:
            test_result = input("What is the next color?")
            if test_result is x[0]:
                print("You have passed this test. On to the next.")
            else:
                print("You lose.")

class Player:
    """player model"""

    def __init__(self):
        self.score = 0

    def increase_score(self):
        self.score = self.score + 1

class Simon:
    """simon model"""

    def __init__(self):
        self.history = []
        self.colors = [('b', "BLUE"),('g', "GREEN"),('r', "RED"),('f', "PURPLE"), ('y', "YELLOW"), ('t', "BROWN"), ('v', "MAGENTA")]

    def get_level_number(self):
        return len(self.history)

    def add_color(self):
        self.history.append(random.choice(self.colors))

game = Game(22)

os.system('clear')

while not game.over:
    game.next_level()
    game.over = True