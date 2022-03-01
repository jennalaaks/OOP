# Filename      tehtava4.py
# Author:       Jenna Laaksovirta
# Description:  Create a dictionary so that the player id is a key and each player has one dice. Roll each player’s dice and print out each player’s dice’s side.
import random

class Player:
    id = 0
    def __init__(self):
        self.__firstName = ""
        self.__lastName = ""
        self.__id = Player.id

        Player.id += 1

    def set_firstName(self, firstname):
        self.__firstName = firstname

    def set_lastName(self, lastname):
        self.__lastName = lastname

    def get_firstName(self):
        return self.__firstName

    def get_lastName(self):
        return self.__lastName
    
    def get_id(self):
        return self.__id

class Dice:
    def __init__(self):
        self.__sideup = 1

    def roll_the_dice(self):
        self.__sideup = random.randint(1, 6)
        
    def get_dice_sideup(self):
        return self.__sideup

def main():
    player1 = Player()
    player1.set_firstName("Anna")
    player1.set_lastName("Laakkonen")

    player2 = Player()
    player2.set_firstName("Eero")
    player2.set_lastName("Erikoinen")

    player3 = Player()
    player3.set_firstName("Tuomo")
    player3.set_lastName("Tuollainen")

    dice1 = Dice()
    dice2 = Dice()
    dice3 = Dice()

    # Give dice to players
    diceToPlayer = {player1.get_id() : dice1,
                    player2.get_id() : dice2,
                    player3.get_id() : dice3
                    }

    # Roll dices
    dice1.roll_the_dice()
    dice2.roll_the_dice()
    dice3.roll_the_dice()

    # Print players and dices
    print(f"Player {player1.get_firstName()} {player1.get_lastName()} dice number is {diceToPlayer[player1.get_id()].get_dice_sideup()}")
    print(f"Player {player2.get_firstName()} {player2.get_lastName()} dice number is {diceToPlayer[player2.get_id()].get_dice_sideup()}")
    print(f"Player {player3.get_firstName()} {player3.get_lastName()} dice number is {diceToPlayer[player3.get_id()].get_dice_sideup()}")

main()