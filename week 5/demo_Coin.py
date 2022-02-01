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

    def __init__(self, sideup, material):
        self.__sideup = sideup
        self.__material = material

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

    # Accessor methos ("setting")
    def set_material(self, material):
        self.__material = material

    # Accessor methos ("getter")
    def get_material(self):
        return self.__material