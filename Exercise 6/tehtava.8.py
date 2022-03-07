# Filename      tehtava8.py
# Author:       Jenna Laaksovirta
# Description:  Student and teacher has multiple animals. Program show animals and other informations.

from tehtava4 import DomesticAnimal
from tehtava4 import WildAnimal

class Person:
    def __init__(self, id, name, domesticAnimals, wildAnimals):
        self.__id = id
        self.__name = name
        self.__domesticAnimals = domesticAnimals
        self.__wildAnimals = wildAnimals

    def set_name(self, name):
        self.__name = name
    
    def set_id(self, id):
        self.__id = id

    def set_domesticAnimal(self, domesticAnimals):
        self.__domesticAnimal = domesticAnimals

    def set_wildAnimal(self, wildAnimals):
        self.__wildAnimal = wildAnimals
    
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_domesticAnimal(self):
        return self.__domesticAnimals

    def get_wildAnimal(self):
        return self.__wildAnimals
    
    def __str__(self):
        domesticAnimals = ""
        wildAnimals = ""
        for animal in self.__domesticAnimals: 
            domesticAnimals += animal.get_species() + " "

        for animal in self.__wildAnimals:
            wildAnimals += animal.get_species() + " "

        return (f"id: {self.__id},\nname: {self.__name},\ndomestic animals: {domesticAnimals},\nwild animals: {wildAnimals}")

class Student(Person): 
    def __init__(self, id, name, groupNum, domesticAnimals, wildAnimals):
        Person.__init__(self, id, name, domesticAnimals, wildAnimals)
        self.__groupNum = groupNum

    def set_groupNum(self, groupNum):
        self.__groupNum = groupNum

    def get_groupNum(self):
        return self.__groupNum

    def __str__(self):
        return (f"Teacher {Person.__str__(self)},\ngroup number: {self.__groupNum}")
    
class Teacher(Person):
    def __init__(self, id, name, homeClass, subject, domesticAnimals, wildAnimals):
        Person.__init__(self, id, name, domesticAnimals, wildAnimals)
        self.__homeClass = homeClass
        self.__subject = subject

    def set_homeClass(self, homeClass):
        self.__homeClass = homeClass

    def set_subject(self, subject):
        self.__subject = subject

    def get_homeClass(self):
        return self.__homeClass

    def get_subject(self):
        return self.__subject

    def __str__(self):
        return (f"Student {Person.__str__(self)}, subject: {self.__subject}, home class: {self.__homeClass}")

def main():
    dog = DomesticAnimal('dog', 40, 56, 'Hau!', 'meat', 0, 'Maija Meikäläinen', 'Rekku')
    cat = DomesticAnimal('cat', 35, 4, 'MIAU!', 'fish', 1, 'Karolina Mäkinen', 'Rambo')
    ostrich = WildAnimal('ostrich', 210, 98, 'Kakaa', 'plants', 2, 'Africa', 'no')
    lion = WildAnimal('lion', 140, 220, 'Roar', 'Meat', 3, 'Africa', 'no')

    domesticAnimals = [dog, cat]
    wildAnimals = [ostrich, lion]
    sanna = Teacher(1, "Sanna Maatta", "ICT_2015", "project skills", domesticAnimals, wildAnimals)
    student1 = Student(1, "Jenna Laaksovirta", 5, domesticAnimals, wildAnimals)
    print(sanna)
    print(student1)

main()
