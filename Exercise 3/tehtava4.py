# Filename tehtava4.py
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

    def set_currency(self, parametri):
        #rand = random.randint(0, 4)

        if parametri == 0:
            self.__currency = 'Euro'
        elif parametri == 1:
            self.__currency = 'Pound'
        elif parametri == 2:
            self.__currency = 'Dollar'
        elif parametri == 3:
            self.__currency = 'Ruble'
        else:
            self.__currency = 'Yen'

    def get_currency(self):
        return self.__currency


def main():

    my_coin = Coin()

    print('This side up', my_coin.get_sideup())

    print('This side up', my_coin.get_sideup())

    print('Currency (original):', my_coin.get_currency())

    print('Currency (new):', my_coin.get_currency())

    my_coin.set_currency(3)

    print('Currency (new):', my_coin.get_currency())

    my_coin.__currency = "Blue" # Try set new value

    print('Currency (new):', my_coin.get_currency()) # Value is still Ruble

main()