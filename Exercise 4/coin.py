# Filename      tehtava7.py
# Author:       Jenna Laaksovirta
# Description:  3 dice game where one player leaves each round.
   
import random

class Dice:
    def __init__(self, name):
        self.__sideup = 1
        self.__name = name

    def set_toss_the_dice(self):
        self.__sideup = random.randint(1, 6)
        
    def get_toss_the_dice(self):
        return self.__sideup

    def get_name(self):
        return self.__name

    def __gt__(self, other):
        return self.get_toss_the_dice() > other.get_toss_the_dice()

    def removePlayer(players):
        print( f'{min(players).get_name()} has a small number of dice.')
        return [player for player in players if player != min(players)] # Go through the players list and compile a new list. (List comprehension)