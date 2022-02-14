# Filename      tehtava7.py
# Author:       Jenna Laaksovirta
# Description:  The user enters the phone information into the object and then the information is printed.

import cellphoneFile2
import coin

if __name__=="__main__":

    phones = []

    #for phone in phones:
    for phone in range(6):
        phones.append(cellphoneFile2.Cellphone())
        print(f'Enter {phone + 1}. phone information.')
        phones[phone].set_manufact(input('Enter the cellpone manufact: '))
        phones[phone].set_model(input('Enter the cellpone model: '))
        phones[phone].set_retail_price(input('Enter the cellpone retail price: '))
        print('')

    for phone in phones:
        print(f'Phone id:{phone.get_id()} information: ')
        print(f'Manufacturer: {phone.get_manufact()}')
        print(f'Model number: {phone.get_model()}')
        print(f'Retail price: {phone.get_retail_price()}')
        print('')

    players = [ coin.Dice ("Karolina"), coin.Dice ("Jorma"), coin.Dice("Tero")]

    while len(players) > 1:
        for player in players:
            player.set_toss_the_dice()
            print( f"{player.get_name()} dice number is {player.get_toss_the_dice()}" )
            
        players = coin.Dice.removePlayer(players)
        print("")

    print(f"Winner is {players[0].get_name()}!")
    print(f"Winner phone is {phones[players[0].get_toss_the_dice()].get_manufact()}")