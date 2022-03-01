# Filename      tehtava2.py
# Author:       Jenna Laaksovirta
# Description:  Create a class mammal and chlid classes.

class Mammal:
    def __init__(self, species, size, weight, id):
        self.__id = id
        self.__species = species
        self.__size = size
        self.__weight = weight

    def set_id(self, id):
        self.__id = id

    def set_species(self, species):
        self.__species = species

    def set_size(self, size):
        self.__size = size

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

    def __str__(self):
        return (f"id: {self.__id}, species: {self.__species}, size: {self.__size}, weight: {self.__weight}")

class Dog(Mammal):
    def __init__(self, noise, owner, diet, name,species, size, weight, id):
        Mammal.__init__(self, species, size, weight, id)
        self.__noise = noise
        self.__owner = owner
        self.__diet = diet
        self.__name = name

    def set_noise(self, noise):
        self.__noise = noise
 
    def set_owner(self, owner):
        self.__owner = owner
   
    def set_diet(self, diet):
        self.__noise = diet
    
    def set_name(self, name):
        self.__name = name

    def get_noise(self):
        return self.__noise

    def get_weight(self):
        return self.__owner

    def get_diet(self):
        return self.__diet

    def get_name(self):
        return self.__name

    def __str__(self):
        return (f"{Mammal.__str__(self)} noise: {self.__noise}, owner: {self.__owner}, diet: {self.__diet}, name: {self.__name}")

class Cat(Mammal):
    def __init__(self, noise, owner, diet, name,species, size, weight, id):
        Mammal.__init__(self, species, size, weight, id)
        self.__noise = noise
        self.__owner = owner
        self.__diet = diet
        self.__name = name

    def set_noise(self, noise):
        self.__noise = noise
 
    def set_owner(self, owner):
        self.__owner = owner
   
    def set_diet(self, diet):
        self.__noise = diet
    
    def set_name(self, name):
        self.__name = name

    def get_noise(self):
        return self.__noise

    def get_weight(self):
        return self.__owner

    def get_diet(self):
        return self.__diet

    def get_name(self):
        return self.__name

    def __str__(self):
        return (f"{Mammal.__str__(self)} noise: {self.__noise}, owner: {self.__owner}, diet: {self.__diet}, name: {self.__name}")

class Elephant(Mammal):
    def __init__(self, noise, owner, diet, name,species, size, weight, id):
        Mammal.__init__(self, species, size, weight, id)
        self.__noise = noise
        self.__owner = owner
        self.__diet = diet
        self.__name = name

    def set_noise(self, noise):
        self.__noise = noise
 
    def set_owner(self, owner):
        self.__owner = owner
   
    def set_diet(self, diet):
        self.__noise = diet
    
    def set_name(self, name):
        self.__name = name

    def get_noise(self):
        return self.__noise

    def get_weight(self):
        return self.__owner

    def get_diet(self):
        return self.__diet

    def get_name(self):
        return self.__name

    def __str__(self):
        return (f"{Mammal.__str__(self)} noise: {self.__noise}, owner: {self.__owner}, diet: {self.__diet}, name: {self.__name}")

def main():
    dog = Dog("hau!", "Kimmo", "meat", "Raimo", "dog", 20, 34, 1)
    cat = Cat("MIAAU", "Karolina", "fish", "Rambo", "cat", 35, 3, 2)
    elephant = Elephant("Truuut!", "Balsam", "plants", "Keijo", "elephant", 1250, 200, 3)
    print(dog)
    print(cat)
    print(elephant)

main()