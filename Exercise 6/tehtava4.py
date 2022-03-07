# Filename      tehtava4.py
# Author:       Jenna Laaksovirta
# Description:  Create a class mammal and chlid classes.

class Mammal:
    def __init__(self, species, size, weight, noise, diet, id):
        self.__id = id
        self.__species = species
        self.__size = size
        self.__weight = weight
        self.__noise = noise
        self.__diet = diet

    def set_id(self, id):
        self.__id = id

    def set_species(self, species):
        self.__species = species

    def set_size(self, size):
        self.__size = size

    def set_noise(self):
        self.__noise = noise

    def set_diet(self):
        self.__diet = diet

    def set_weight(self, weight):
        self.__weight = weight

    def get_id(self):
        return self.__id

    def get_species(self):
        return self.__species

    def get_size(self):
        return self.__size

    def get_weight(self):
        return self.__weight

    def get_noise(self):
        return self.__noise

    def get_diet(self):
        return self.__diet

    def __str__(self):
        return (f"\nid: {self.__id},\nspecies: {self.__species},\nsize: {self.__size},\nweight: {self.__weight}\nnoise: {self.__noise},\ndiet: {self.__diet}")

class DomesticAnimal(Mammal):
    def __init__(self, species, size, weight, noise, diet, id, owner, name):
        Mammal.__init__(self, species, size, weight, noise, diet, id)
        self.__name = name
        self.__owner = owner

    def set_name(self, name):
        self.__name = name

    def set_owner(self, owner):
        self.__owener = owner
    
    def get_name(self):
        return self.__name

    def get_owner(self):
        return self.__owner

    def __str__(self):
        return (f"{Mammal.__str__(self)},\nname: {self.__name}\nowner: {self.__owner}")

class WildAnimal(Mammal):
    def __init__(self, species, size, weight, noise, diet, id, habitat, endangered):
        Mammal.__init__(self, species, size, weight, noise, diet, id)
        self.__habitat = habitat
        self.__endangered = endangered

    def set_habitat(self, habitat):
        self.__habitat = habitat

    def set_endagered(self, endangered):
        self.__endangered = endangered

    def get_habitat(self):
        return self.__habitat

    def get_endangered(self):
        return self.__endangered

    def __str__(self):
        return (f"{Mammal.__str__(self)}\habitat: {self.__habitat}\nis endangered: {self.__endangered}")

if __name__=="__main__":
    dog = DomesticAnimal('dog', 40, 56, 'Hau!', 'meat', 0, 'Maija Meikäläinen', 'Rekku')
    cat = DomesticAnimal('cat', 35, 4, 'MIAU!', 'fish', 1, 'Karolina Mäkinen', 'Rambo')
    ostrich = WildAnimal('ostrich', 210, 98, 'Kakaa', 'plants', 2, 'Africa', 'no')
    animals = [dog, cat, ostrich]

    for i in animals:
        print(i)