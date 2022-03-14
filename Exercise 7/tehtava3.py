# Filename      tehtava3.py
# Author:       Jenna Laaksovirta
# Description:  Students have many pets.

class Student:
    def __init__(self, first_name, last_name, student_ID):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_ID = student_ID
        self.__pets = []
        self.__cars = [] # Add for task 4.

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_student_ID(self, student_ID):
        self.__student_ID = student_ID

    def set_pets(self, pets):
        self.__pets = pets

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_student_ID(self):
        return self.__student_ID

    def get_pets(self):
        return self.__pets

    def get_cars(self):
        return self.__cars

    # Pets
    def add_pet(self, pet):
        self.__pets.append(pet) 

    def remove_pet(self, pet):
        self.__pets.remove(pet)

    def print_pets(self):
        print(*self.__pets, sep = ",\n")

    # Cars
    def add_car(self, car):
        self.__cars.append(car) 

    def remove_owner(self, car):
        self.__cars.remove(car)

    def print_cars(self):
        print(*self.__cars, sep = ",\n")

    def __str__(self):
        return (f'firstname: {self.__first_name}, lastname: {self.__last_name}, student ID: {self.__student_ID}')

class Pet:
    def __init__(self, species, name, size):
        self.__species = species
        self.__name = name
        self.__size = size # For task 4

    def set_species(self, species):
        self.__species = species

    def set_name(self, name):
        self.__name = name

    def set_size(self, size):
        self.__size = size

    def get_species(self):
        return self.__species

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def __str__(self):
        return (f'name: {self.__name}, species: {self.__species} size: {self.__size}')

def printStudentAndAnimal(student):
    print('Student: ')
    print(student)
    print(f"{student.get_first_name()}'s pets: ")
    student.print_pets()
    print('')

if __name__=="__main__":
    ukko = Student('Ukko', 'Tuominen', 1)
    cat = Pet('cat', 'Rambo', 5)
    horse = Pet('horse', 'Vasabi', 400)
    ukko.add_pet(cat)
    ukko.add_pet(horse)
    printStudentAndAnimal(ukko)