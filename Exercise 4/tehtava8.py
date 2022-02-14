# Filename      tehtava6.py
# Author:       Jenna Laaksovirta
# Description:  Get and print car info.

class Car:
    def __init__(self, make, model, mileage, price, color, maximum_load_limit, size_of_trunk):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        self.__color = color
        self.__maximum_load_limit = maximum_load_limit
        self.__size_of_trunk = size_of_trunk

    def set_make(self, make):
        self.__make = make
        
    def get_make(self):
        return self.__make

    def set_model(self, model):
        self.__model = model
        
    def get_model(self):
        return self.__model

    def set_mileage(self, mileage):
        self.__mileage = mileage
        
    def get_mileage(self):
        return self.__mileage

    def set_price(self, price):
        self.__price = price
        
    def get_price(self):
        return self.__price

    def set_color(self, color):
            self.__color = color
        
    def get_color(self):
        return self.__color

    def set_maximum_load_limit(self, maximum_load_limit):
        self.__maximum_load_limit = maximum_load_limit
        
    def get_maximum_load_limit(self):
        return self.__maximum_load_limit
            
    def set_size_of_trunk(self, size_of_trunk):
        self.__ = size_of_trunk
        
    def get_size_of_trunk(self):
        return self.__size_of_trunk

    def __str__(self):
        return (f"Make: {self.__make}, model: {self.__model}, mileage: {self.__mileage}, price {self.__price}, color: {self.__color}, maximum_load_limit: {self.__maximum_load_limit}, size of trunk: {self.__size_of_trunk}")

if __name__=="__main__":
    Tesla = Car("Tesla", "Model 3", "0", "67000", "red", "900", "50")
    print(Tesla)