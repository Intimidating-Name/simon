import random
#import colorama

class Game:
    """game controller"""

    def __init__(self):
        self.over = False
        self.simon = Simon()
        self.player = Player()
        self.level = self.simon.get_level_number()

    def next_level(self):
        print("next level")

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
        self.colors = [('b', "BLUE"),('g', "GREEN"),('r', "RED"),('f', "PURPLE"), ('y', "YELLOW"), ('t', "BROWN")]

    def get_level_number(self):
        return len(self.history)

game = Game()
while not game.over:
    print(game.level)
    print(game.player.score)
    game.player.increase_score()
    print(game.player.score)
    print(game.simon.colors)
    game.over = True