# Filename      tehtava6.py
# Author:       Jenna Laaksovirta
# Description:  Dices sum tells which animal student owns.

import random

class Mammal:
    id = 0
    def __init__(self, species, name, size, weight):
        self.__id = Mammal.id
        self.__species = species
        self.__name = name
        self.__size = size
        self.__weight = weight

        Mammal.id += 1

    def getId(self):
        return self.__id

    def get_size(self):
        return self.__size

    def __str__(self):
        return (f"id: {self.__id}, species: {self.__species}, name: {self.__name}, size: {self.__size}, weight: {self.__weight}")

    def __gt__(self, other):
        return self.__size > other.__size

class Student:
    id = 0
    def __init__(self, firstName, lastName, dice1, dice2):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__id = Student.id
        self.__dice1 = dice1
        self.__dice2 = dice2

        Student.id += 1

    def set_firstName(self, firstName):
        self.__firstName = firstName

    def set_lastName(self, lastName):
        self.__lastName = lastName

    def get_firstName(self):
        return self.__firstName

    def get_lastName(self):
        return self.__lastName

    def get_dices_sum(self):
        return self.__dice1 + self.__dice2
    
    def __gt__(self, other):
        return self.get_dices_sum() > other.get_dices_sum()

    def __str__(self):
        return (f"{self.__firstName} {self.__lastName} nopan summa {self.get_dices_sum()}")

class Dice:
    def __init__(self):
        self.__sideup = 1

    def roll_the_dice(self):
        self.__sideup = random.randint(1, 6)
        
    def get_dice_sideup(self):
        return self.__sideup

def main():
    # Greate 2 dice.
    dice1 = Dice()
    dice2 = Dice()

    # Roll the dices.
    dice1.roll_the_dice()
    dice2.roll_the_dice()
    
    student1 = Student('Anna', 'Tiukunen', dice1.get_dice_sideup(), dice2.get_dice_sideup())

    # Roll the dices.
    dice1.roll_the_dice()
    dice2.roll_the_dice()

    student2 = Student('Heikki', 'Mattila', dice1.get_dice_sideup(), dice2.get_dice_sideup())
 
    # Roll the dices.
    dice1.roll_the_dice()
    dice2.roll_the_dice()

    student3 = Student('Karolina', 'Mäkinen', dice1.get_dice_sideup(), dice2.get_dice_sideup())

    mammal1 = Mammal('Horse', 'Totilas', 350, 175)
    mammal2 = Mammal('Dog', 'Totti', 16, 45)
    mammal3 = Mammal('Cat', 'Rambo', 5, 30)
        
    Students = [student1, student2, student3]
    Mammals = [mammal1, mammal2, mammal3]


    Students = sorted(Students)
    Mammals = sorted(Mammals)

    # Print results.
    for i in range(len(Students)):
        print(f"{Students[i].get_firstName()} {Students[i].get_lastName()} dice sum is: {Students[i].get_dices_sum()} and own mammal {Mammals[i]}")

main()