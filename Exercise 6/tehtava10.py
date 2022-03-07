# Filename      tehtava10.py
# Author:       Jenna Laaksovirta
# Description:  Create different houses and set owner to houses. Print results.

class House:
    def __init__(self, color, material, yearOfConstruction):
        self.__color = color
        self.__material = material
        self.__yearOfConstruction = yearOfConstruction

    def set_color(self, color):
        self.__color = color

    def set_material(self, material):
        self.__material = material

    def set__yearOfConstruction(self, year):
        self.set__yearOfConstruction = year

    def get_color(self):
        return self.__color

    def get_material(self):
        return self.__material

    def get__yearOfConstruction(self):
        return self.set__yearOfConstruction

    def __str__(self):
        return (f'house color: {self.__color} \nmaterial: {self.__material}, \nyear of construction: {self.__yearOfConstruction} ')

class TerracedHouse(House):
    def __init__(self, color, material, yearOfConstruction, numberOfDwellings, numberOfParkingSpaces):
        House.__init__(self, color, material, yearOfConstruction)
        self.__numberOfDwellings = numberOfDwellings
        self.__numberOfParkingSpaces = numberOfParkingSpaces

    def set_numberOfDwellings(self, num):
        self.__numberOfDwellings = num
    
    def set_numberOfParkingSpaces(self, num):
        self.__numberOfParkingSpaces = num

    def get_numberOfDwellings(self):
        return self.__numberOfDwellings
    
    def get_numberOfParkingSpaces(self):
        return self.__numberOfParkingSpaces

    def __str__(self):
        return (f'{House.__init__(self)} \nhouse type: town house \nnumber of dwellings: {self.__numberOfDwellings} \nnumber of parking spaces: {self.__numberOfParkingSpaces} ')

class ApartmentHouse(House):
    def __init__(self, color, material, yearOfConstruction, numberOfDwellings, numberOfParkingSpaces, numberOfFloors):
        House.__init__(self, color, material, yearOfConstruction)
        self.__numberOfDwellings = numberOfDwellings
        self.__numberOfParkingSpaces = numberOfParkingSpaces
        self.__numberOfFloors = numberOfFloors

    def set_numberOfDwellings(self, num):
        self.__numberOfDwellings = num
    
    def set_numberOfParkingSpaces(self, num):
        self.__numberOfParkingSpaces = num

    def set_numberOfFloors(self, num):
        self.__numberOfFloors = num

    def get_numberOfDwellings(self):
        return self.__numberOfDwellings
    
    def get_numberOfParkingSpaces(self):
        return self.__numberOfParkingSpaces

    def get_numberOfFloors(self):
        return self.__numberOfFloors

    def __str__(self):
        return (f'{House.__str__(self)} \nhouse type: apartment house \nnumber of dwellings: {self.__numberOfDwellings} \nnumber of parking spaces: {self.__numberOfParkingSpaces} \nnumber of floors: {self.__numberOfFloors} ')

class TownHouse(House):
    def __init__(self, color, material, yearOfConstruction, squareMeters, isGarage, numberOfFloors):
        House.__init__(self, color, material, yearOfConstruction)
        self.__squareMeters = squareMeters
        self.__isGarage = isGarage
        self.__numberOfFloors = numberOfFloors

    def set_squareMeters(self, squareMeters):
        self.__squareMeters = squareMeters
    
    def set_isGarage(self, isGarage):
        self.__isGarage = isGarage

    def set_numberOfFloors(self, num):
        self.__numberOfFloors = num

    def get_squareMeters(self):
        return self.__squareMeters
    
    def get_isGarage(self):
        return self.__isGarage

    def get_numberOfFloors(self):
        return self.__numberOfFloors

    def __str__(self):
        return (f'{House.__str__(self)} \nhouse type: town house \nsquare meters: {self.__squareMeters} \nis garage: {self.__isGarage} \nnumber of floors: {self.__numberOfFloors} ')

class Person:
    def __init__(self, id, name, age):
        self.__id = id
        self.__name = name
        self.__age = age

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age):
        self.__age = age

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__age

    def get_age(self):
        return self.__age

    def __str__(self):
        return (f'\nname: {self.__name} \nage: {self.__age}')

def main():
    person0 = Person(0, 'Ville Virtanen', 54)
    house0 = TownHouse('red', 'wood', 1995, 125, 'yes', 2)

    person1 = Person(1, 'Tuulikki Rantala', 75)
    house1 = ApartmentHouse('white', 'rock', '2015', 8, 20, 46)

    houseToOwners = {
        house0 : person0,
        house1 : person1
    }
    
    index = 1
    for key, value in houseToOwners.items():
        print(f'{index}. HOUSE DETAILS:')
        print(key, '\n\nOWNER DETAILS: ', value)
        print('')
        index += 1

main()
    
    
    