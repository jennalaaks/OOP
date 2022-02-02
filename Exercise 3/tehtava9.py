# Filename      tehtava9.py
# Author:       Jenna Laaksovirta
# Description:  The user enters the phone information into the object and then the information is printed.

class Cellphone:
    def __init__(self):
        self.__manufact = ""
        self.__model = ""
        self.__retail_price = 0

    def set_manufact(self, input):
        self.__manufact = input

    def set_model(self, input):
        self.__model = input

    def set_retail_price(self, input):
        self.__retail_price = input
    
    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model
    
    def get_retail_price(self):
        return self.__retail_price

def main():
    phone = Cellphone()
    
    phone.set_manufact(input('Enter the cellpone manufact: '))
    phone.set_model(input('Enter the cellpone model: '))
    phone.set_retail_price(input('Enter the cellpone retail price: '))
    print("")
    print('Here is the data that you provided:')
    print(f'Manufacturer: {phone.get_manufact()}')
    print(f'Model number: {phone.get_model()}')
    print(f'Retail price: {phone.get_retail_price()}')

main()