# Filename tehtava6.py
# Source: Tony Gaddia: Starting out with Python, fourth edition
# Author: Jenna Laaksovirta
# Description: Coin object and tossing

import random

class Coin:
    
    def __init__(self):
        self.__sideup = 'Heads'

    def toss(self):
        if random.randint(0 , 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup

def main():

    my_coin = Coin()

    print('This side up', my_coin.get_sideup())
    my_coin.toss()

    print('This side up', my_coin.get_sideup())

main()