# File: demo_coin.py
# Source: Tony Gaddia: Starting out with Python, fourth edition
# Modified by: Sanna Maatta & Anne Jumppanen
# Description: Coin object and tossing

import random

# The Coin class simulates a coin that can
# be flipped.

class Coin:
    
    # The __init__ method initializes the
    # side data attribute with 'Heads'

    def __init__(self):
        self.__sideup = 'Heads'

    # The toss method generates a random number
    # in the range of 0 throught 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0 , 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # The get _sideup method returns the value
    # references by sideup.

    def get_sideup(self):
        return self.__sideup

# The main function.
def main():

    # Create an object from the Coin class.
    my_coin = Coin()

    # Display the side of the coin that is facing up.
    print('This side up', my_coin.get_sideup())

    # Toss the coin.
    my_coin.toss()
    #my_coin.__sideup = 'Something'

    # Display the side of the coin that is facing up.
    print('This side up', my_coin.get_sideup())

# Call the main function.
main()


    