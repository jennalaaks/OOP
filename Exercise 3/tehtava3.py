# Filename tehtava3.py
# Author: Jenna Laaksovirta
# Description: Coin object and tossing

import random

class Coin:
    
    def __init__(self):
        self.__sideup = 'Heads'
        self.__currency = 'Euro'

    def toss(self):
        if random.randint(0 , 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup

    def currency(self):
        rand = random.randint(0, 4)

        if rand == 0:
            self.__currency = 'Euro'
        elif rand == 1:
            self.__currency = 'Pound'
        elif rand == 2:
            self.__currency = 'Dollar'
        elif rand == 3:
            self.__currency = 'Ruble'
        else:
            self.__currency = 'Yen'

    def get_currency(self):
        return self.__currency


def main():

    my_coin = Coin()

    print('This side up', my_coin.get_sideup())

    my_coin.toss()

    print('This side up', my_coin.get_sideup())

    print('Currency (original):', my_coin.get_currency())
    my_coin.currency()
    print('Currency (new):', my_coin.get_currency())


main()