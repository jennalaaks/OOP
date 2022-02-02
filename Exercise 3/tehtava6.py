# Filename      tehtava6.py
# Author:       Jenna Laaksovirta
# Description:   Toss the dice and get color and extra feature. Sum the dices num.

import random

class Dice:
    def __init__(self):
        self.__sideup = 1

    def set_toss_the_dice(self):
        self.__sideup = random.randint(1, 6)
  
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