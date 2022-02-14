# Filename      tehtava6.py
# Author:       Jenna Laaksovirta
# Description:  Test whether the animal fits in the car.

from coin import Dice
from Mammal import Mammal
from tehtava8 import Car

def findId(diceNumber, animals):
    for i in animals:
        if diceNumber == i.getId():
            return i

    return None

def main():
    dice = Dice("Lempinoppa")
    animals = [
        Mammal("Peura", "Bambi", 30, 50),
        Mammal("Valas", "Simo", 3000, 500),
        Mammal("Heinäsirkka", "Samu", 1, 1),
        Mammal("Hevonen", "Eero", 300, 175),
        Mammal("Haukka", "Tauno", 4, 3),
        Mammal("Ihminen", "Uni-Kukka", 300, 175),
    ]

    car = Car("Tesla", "Model 3", 0, 67000, "red", 900, 50)

    dice.set_toss_the_dice()

    animal = findId(dice.get_toss_the_dice()-1, animals)
    animal.animalToCar(car)


main()
