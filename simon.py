import random
import time
import os
import sys
import colorama


class Game:
    """game controller"""

    def __init__(self, max_levels):
        self.over = False
        self.simon = Simon()
        self.player = Player()
        self.level = self.simon.get_level_number()
        self.max_levels = max_levels
        self.regular_mode = False
        self.timeout = 2

    def next_level(self):
        print("next level")
        self.simon.add_color()
        self.player.increase_score()
        self.print_level()
        self.test_player()
        self.timeout = self.timeout - (self.timeout * 0.1)

    def print_level(self):
        for x in self.simon.history:
            self.clear_screen()
            print(self.get_color(x) if self.regular_mode else self.get_random_color()+str(x))
            print(colorama.Fore.WHITE)
            time.sleep(self.timeout)
            self.clear_screen()
            time.sleep(0.499995)

    def get_color(self, tuple):
        if tuple[1] is "BLUE":
            return colorama.Fore.BLUE
        if tuple[1] is "GREEN":
            return colorama.Fore.GREEN
        if tuple[1] is "RED":
            return colorama.Fore.RED
        if tuple[1] is "YELLOW":
            return colorama.Fore.YELLOW
        if tuple[1] is "CYAN":
            return colorama.Fore.CYAN
        if tuple[1] is "MAGENTA":
            return colorama.Fore.MAGENTA

    def get_random_color(self):
        random_color_tuple = random.choice(self.simon.colors)
        random_color = self.get_color(random_color_tuple)
        return random_color

    def test_player(self):
        for x in self.simon.history:
            test_result = input("What is the next color?")
            if test_result is x[0]:
                print("You have passed this test. On to the next.")
                self.player.increase_score()
            else:
                print("You lose.")
                self.over = True
                break

    def clear_screen(self):
        print("\033[H\033[J")

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
        self.colors = [('b', "BLUE"), ('g', "GREEN"), ('r', "RED"), ('y', "YELLOW"), ('t', "CYAN"), ('v', "MAGENTA")]

    def get_level_number(self):
        return len(self.history)

    def add_color(self):
        self.history.append(random.choice(self.colors))

game = Game(22)

game.clear_screen()

mode_choice = input("Do you want to play regular or cognitive dissonance?")

if mode_choice is "regular":
    game.regular_mode = True
elif mode_choice is "cognitive dissonance":
    game.regular_mode = False
elif mode_choice is "the second one":
    print("The words are right there for you to spell from. If you are curious, cognitive dissonance is where there is a color but it's not the color that the color is.")
else:
    print("You have been defaulted to cognitive dissonance.")

while not game.over:
    print("The next level is level number " + str(game.simon.get_level_number()))
    game.next_level()
    print("Your current score is " + str(game.player.score))