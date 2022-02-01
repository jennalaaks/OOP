from cgitb import small
import random

class Dice:
    def __init__(self, name):
        self.__sideup = 1
        self.__name = name

    def set_toss_the_dice(self):
        self.__sideup = random.randint(1, 6)
        
    def get_toss_the_dice(self):
        return self.__sideup

    def get_name(self):
        return self.__name

    def __gt__(self, other):
        return self.get_toss_the_dice() > other.get_toss_the_dice()

    def __str__(self) -> str:
        return f"{self.__name} {self.__sideup}" # Representation

def poistaPaskin(players):
    print( 'Kierroksen huonoin pelaaja: ', min(players).get_name() )
    return [player for player in players if player != min(players)] # Käy läpi players-listan ja koostaa uuden listan. kts. List comprehension

def main():

    players = [ Dice ("Karolina"), Dice ("Jorma"), Dice("Tero")]

    print(players[0])
    print(players[1])
    print(players[2])

    while len(players) > 1:
        for player in players:
            player.set_toss_the_dice()
            print(f"{player.get_name()} nopan luku on: {player.get_toss_the_dice()}")
            
        players = poistaPaskin(players)
        print("")

    print(f"Voittaja on {players[0].get_name()}!")

main()