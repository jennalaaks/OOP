from tehtava8 import Car

class Mammal():
    id = 0
    def __init__(self, species, name, size, weight):
        self.__id = Mammal.id
        self.__species = species
        self.__name = name
        self.__size = size
        self.__weight = weight

        Mammal.id += 1

    def getId(self):
        return self.__id

    def animalToCar(self, car):

        mahtuu = True

        if self.__size > car.get_size_of_trunk():
            print(f"{self.__name} ei mahu!")
            mahtuu = False
        
        if self.__weight > car. get_maximum_load_limit():
            print(f"{self.__name} on liian painava!")
            mahtuu = False

        if mahtuu:
            print(f"{self.__name} laitettu auton kyytii!")

    def __str__(self):
        return (f"id: {self.__id}, species: {self.__species}, name: {self.__name}, size: {self.__name}, weight: {self.__weight}")

