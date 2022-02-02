# Filename      tehtava5.py
# Author:       Jenna Laaksovirta
# Description:   Toss the dice and get color and extra feature.

import random

class Dice:
    def __init__(self):
        self.__sideup = 1
        self.__feature = "Fluffy"
        self.__color = "white"

    def set_toss_the_dice(self):
        return self.__sideup
        
    def get_toss_the_dice(self):
        return self.__sideup

    def set_color(self):
        rand = random.randint(0, 5)
        
        if rand == 0:
            self.__color = 'Green'
        elif rand == 1:
            self.__color = 'Yellow'
        elif rand == 2:
            self.__color = 'Red'
        elif rand == 3:
            self.__color = 'Blue'
        elif rand == 4:
            self.__color = 'Brown'
        elif rand == 5:
            self.__color = 'Purple'
        else:
            self.__color = 'Orange'

    def get_color(self):
        return self.__color

    def set_feature(self):
        rand = random.randint(0, 5)
        
        if rand == 0:
            self.__color = 'Hairy'
        elif rand == 1:
            self.__color = 'Beautiful'
        elif rand == 2:
            self.__color = 'Nice'
        elif rand == 3:
            self.__color = 'Angry'
        elif rand == 4:
            self.__color = 'Fierce'
        elif rand == 5:
            self.__color = 'Hot'
        else:
            self.__color = 'Ugly'

    def get_feature(self):
        return self.__feature

def main():
    my_dice = Dice()

    my_dice.set_toss_the_dice()
    print('Rolling the dice...')
    print('The dice number:', my_dice.get_toss_the_dice())
    
    my_dice.set_color()
    print('The dice coloris:', my_dice.get_color())

    my_dice.set_feature()
    print('The Dice feature is:', my_dice.get_feature())

main()
    