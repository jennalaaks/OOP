# File:     main.py
# Author:   Sanna Maatta
#Description: Main function for coin

import demo_Coin

def main():
    my_coin = demo_Coin.Coin("Anything", "Silver")

    #print('This side up', my_coin.get_sideup())

    print("Tossing the coin...")
    my_coin.toss()

    print('This side up', my_coin.get_sideup())

    print('Material is...', my_coin.get_material())
    my_coin.set_material("Gold")
    print('Material is now:', my_coin.get_material())
    

# Calling the main function
main()