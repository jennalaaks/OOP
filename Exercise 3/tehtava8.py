# Filename      tehtava7.py
# Author:       Jenna Laaksovirta
# Description:  3 dice game where one player leaves each round. 
#               if there is a draw, the color of the dice will decide.
   
import random

class Dice:
    def __init__(self, name):
        self.__sideup = 1
        self.__name = name
        self.__color = random.randint(1, 6)

    def set_toss_the_dice(self):
        self.__sideup = random.randint(1, 6)
        
    def get_toss_the_dice(self):
        return self.__sideup

    def get_name(self):
        return self.__name

    def get_color(self):
        if self.__color == 1:
            return 'green'
        elif self.__color == 2:
            return 'yellow'
        elif self.__color == 3:
            return 'red'
        elif self.__color == 4:
            return 'blue'
        elif self.__color == 5:
            return 'brown'
        else:
            return 'purple'

    def __gt__(self, other):
        if self.get_toss_the_dice() == other.get_toss_the_dice():
            return self.__color > other.__color
        else:
            return self.get_toss_the_dice() > other.get_toss_the_dice()

def removePlayer(players):
    print( f'{min(players).get_name()} has a small number of dice.')
    return [player for player in players if player != min(players)] # Go through the players list and compile a new list. (List comprehension)

def main():

    players = [ Dice ("Karolina"), Dice ("Jorma"), Dice("Tero")]

    while len(players) > 1:
        for player in players:
            player.set_toss_the_dice()
            print(f"{player.get_name()} dice number is {player.get_toss_the_dice()} and the dice color is {player.get_color()}")
            
        players = removePlayer(players)
        print("")

    print(f"Winner is {players[0].get_name()}!")

main()