# Filename      tehtava3.py
# Author:       Jenna Laaksovirta
# Description:  Game where the best sum of three rolls wins.
import random

class Player:
    def __init__(self, name):
        self.__sideup = 1
        self.__dices_sum = 0
        self.__name = name

    def set_toss_the_dice(self):
        self.__sideup =  random.randint(1, 6)
        
    def get_toss_the_dice(self):
        return self.__sideup

    def set_dices_sum(self, num):
        self.__dices_sum += num
    
    def force_sum(self, num):
        self.__dices_sum = num
        
    def get_dices_sum(self):
        return self.__dices_sum

    def get_name(self):
        return self.__name

    #def __eq__(self, other):
    #    return self.__dices_sum == other.__dices_sum

    def __gt__(self, other):
        return self.__dices_sum > other.__dices_sum

    def __str__(self):
        return f"{self.__name}:{self.__dices_sum}"

def rolldices(players):
    for player in players:
        for throw in range(3):
            player.set_toss_the_dice()
            player.set_dices_sum(player.get_toss_the_dice())

# Set dices in array.
players = [Player("Tuulikki"), Player("Annikki"), Player("Jaska")]

# Roll the dices.
rolldices(players)

players.sort()
#players[-2].force_sum(18)
#players[-1].force_sum(18)

for i in players:
    print(i)

if players[-2].get_dices_sum() is not players[-1].get_dices_sum():
    print(f'Winner is {players[-1]}')
else:
    print(f"{players[-2].get_name()} ja {players[-1].get_name()} nopat heitetää uuestaa.")
    temp1 = 0
    temp2 = 0

    while temp1 == temp2:
        players[-1].set_toss_the_dice()
        temp1 = players[-1].get_toss_the_dice()
        players[-2].set_toss_the_dice()
        temp2 = players[-2].get_toss_the_dice()
        print(f"{players[-2].get_name()}:{players[-2].get_toss_the_dice()} ja {players[-1].get_name()}:{players[-1].get_toss_the_dice()}")
    
    if temp1 > temp2:
        print(f'Winner is {players[-1].get_name()}')
    else:
        print(f'Winner is {players[-2].get_name()}')