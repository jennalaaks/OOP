# Filename      tehtava5.py
# Author:       Jenna Laaksovirta
# Description:  Check students cars and does pet fits to student car.
 
from tehtava3 import Student
from tehtava3 import Pet


class Car:
    def __init__(self, brand, mileage, trunkSize):
        self.__brand = brand
        self.__owners = []
        self.__mileage = mileage
        self.__trunkSize = trunkSize

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def get_mileage(self):
        return self.__mileage

    def get_brand(self):
        return self.__brand

    def get_trunk_size(self):
        return self.__trunkSize
    
    def add_owner(self, owner):
        self.__owners.append(owner) 

    def remove_owner(self, owner):
        self.__owners.remove(owner)

    def print_owners(self):
        print(*self.__owners, sep = ",\n")

    def __str__(self):
        return (f'brand: {self.__brand}, mileage: {self.__mileage} trunk size: {self.__trunkSize}')

def add_car_to_student(student, car):
    student.add_car(car)
    car.add_owner(student)

def pet_to_car(student):
    print(f"{student.get_first_name()}'s Pets to car: ")
    for pet in student.get_pets():
        for car in student.get_cars():
            if pet.get_size() > car.get_trunk_size():
                print(f'{pet.get_name()} need trailer.')
            else:
                print(f'{pet.get_name()} fits to {car.get_brand()} car.')

if __name__=="__main__":
    # Students
    peppi = Student('Peppi', 'Tepponen', 1)
    karolina = Student('Karolina', 'Makinen', 2)
    jenna = Student('Jenna', 'Laaksovirta', 3)

    # Pets
    rambo = Pet('cat', 'Rambo', 5)
    vasabi = Pet('horse', 'Vasabi', 400)

    # Cars
    toyota = Car('Toyota', 230000, 120)
    skoda = Car('Skoda', 30000, 235)

    # Add cars to student
    add_car_to_student(peppi, toyota)
    add_car_to_student(karolina, skoda)
    add_car_to_student(jenna, skoda)

    # Add pets to student
    karolina.add_pet(rambo)
    jenna.add_pet(vasabi)

    # Print results
    print(f'Car {toyota.get_brand()} owners: ')
    toyota.print_owners()
    print()

    print(f'Car {skoda.get_brand()} owners: ')
    skoda.print_owners()
    print()

    # Print one student car
    print(f"Student {karolina.get_first_name()}'s cars: ")
    karolina.print_cars()
    print()

    # Set pets to car
    pet_to_car(jenna)
    print()
    pet_to_car(karolina)