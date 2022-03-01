# Filename      tehtava5.py
# Author:       Jenna Laaksovirta
# Description:  Create a dictionary wich tell what animal player owns.

class Mammal:
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

    def __str__(self):
        return (f"id: {self.__id}, species: {self.__species}, name: {self.__name}, size: {self.__size}, weight: {self.__weight}")

class Student:
    id = 0
    def __init__(self, firstName, lastName):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__id = Student.id

        Student.id += 1

    def set_firstName(self, firstName):
        self.__firstName = firstName

    def set_lastName(self, lastName):
        self.__lastName = lastName

    def get_firstName(self):
        return self.__firstName

    def get_lastName(self):
        return self.__lastName

def main():
    # Greate students.
    student1 = Student('Anna', 'Tiukunen')
    student2 = Student('Heikki', 'Mattila')
    student3 = Student('Karolina', 'Mäkinen')
    
    #Greate mammals.
    mammal1 = Mammal('Horse', 'Totilas', '350', '175')
    mammal2 = Mammal('Dog', 'Totti', '16', '45')
    mammal3 = Mammal('Cat', 'Rambo', '5', '30')
        

    MammalToStudent = {student1 : mammal1,
                       student2 : mammal2,
                       student3 : mammal3}

    print(f"{student1.get_firstName()} {student1.get_lastName()} own mammal {MammalToStudent[student1]}")
    print(f"{student2.get_firstName()} {student2.get_lastName()} own mammal {MammalToStudent[student2]}")
    print(f"{student3.get_firstName()} {student3.get_lastName()} own mammal {MammalToStudent[student3]}")

main()