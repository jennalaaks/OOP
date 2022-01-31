# Filename tehtava7.py
# Source: Tony Gaddia: Starting out with Python, fourth edition
# Author: Jenna Laaksovirta
# Description: Coin object and tossing

import random

class Coin:
    
    def __init__(self):
        self.__sideup = 'Heads'

    def toss(self):
        print("Tossing the coin…")

        coin = random.randint(0, 4)
    
        if coin == 0:
            self.__sideup = 'Heads'
        if coin == 1:
            self.__sideup = 'Tails'
        if coin == 2:
            self.__sideup = 'Coin lands on the table upright and not flat showing heads or tails.'
        if coin == 3:
            self.__sideup = 'Coin drops on the ground and disappears on a rabbit hole.'
        if coin == 4:
            self.__sideup = 'Coin defies gravity and gets lost on a wormhole in space.'

    def get_sideup(self):
        return self.__sideup

def main():

    my_coin = Coin()

    print('This side up:', my_coin.get_sideup())
    my_coin.toss()

    print('Now this side is up:', my_coin.get_sideup())

main()