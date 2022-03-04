# Filename      tehtava6.py
# Author:       Jenna Laaksovirta
# Description:  Create a class person and two chlid classes which are student and teacher.

class Person:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def set_name(self, name):
        self.__name = name
    
    def set_id(self, id):
        self.__id = id
    
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def __str__(self):
        return (f"id: {self.__id}, name: {self.__name}")

class Student(Person): 
    def __init__(self, id, name, groupNum, domesticAnimal,wildAnimal):
        Person.__init__(self, id, name)
        self.__groupNum = groupNum
        self.__domesticAnimal = domesticAnimal
        self.__wildAnimal = wildAnimal

    def set_groupNum(self, groupNum):
        self.__groupNum = groupNum

    def set_domesticAnimal(self, domesticAnimal):
        self.__domesticAnimal = domesticAnimal

    def set_wildAnimal(self, wildAnimal):
        self.__wildAnimal = wildAnimal

    def get_groupNum(self):
        return self.__groupNum

    def get_domesticAnimal(self):
        return self.__domesticAnimal

    def get_wildAnimal(self):
        return self.__wildAnimal

    def __str__(self):
        return (f"Teacher {Person.__str__(self)}, group number: {self.__groupNum}, domestic animal: {self.__domesticAnimal}, wild animal: {self.__wildAnimal}")
    
class Teacher(Person):
    def __init__(self, id, name, homeClass, subject):
        Person.__init__(self, id, name)
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
    sanna = Teacher(1, "Sanna Maatta", "ICT_2015", "project skills")
    student1 = Student(1, "Jenna Laaksovirta", 5, "dog", "beaver")
    print(sanna)
    print(student1)

main()
