# Filename      tehtava6.py
# Author:       Jenna Laaksovirta
# Description:   Toss the dice and get color and extra feature. Sum the dices num.

import random

class Dice:
    def __init__(self):
        self.__sideup = 1

    def set_toss_the_dice(self):
        rand = random.randint(0, 5)
        
        if rand == 0:
            self.__sideup = 1
        elif rand == 1:
            self.__sideup = 2
        elif rand == 2:
            self.__sideup = 3
        elif rand == 3:
            self.__sideup = 3
        elif rand == 4:
            self.__sideup = 4
        elif rand == 5:
            self.__sideup = 5
        else:
            self.__sideup = 6
        
    def get_toss_the_dice(self):
        return self.__sideup

def main():
    my_dice1 = Dice()
    my_dice2 = Dice()

    my_dice1.set_toss_the_dice()
    print('Rolling the first dice...')
    print('The dice number:', my_dice1.get_toss_the_dice())

    my_dice2.set_toss_the_dice()
    print('Rolling the second dice...')
    print('The dice number:', my_dice2.get_toss_the_dice())

    print('Sum of dices:', (my_dice1.get_toss_the_dice() + my_dice2.get_toss_the_dice()))
    
    

main()