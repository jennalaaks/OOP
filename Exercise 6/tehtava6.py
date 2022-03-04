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
    
    def get_id(self)
        return self.__id
    
    def __str__(self):
        pass

class Student(Person):
    def __init__(self, id, name, groupNum, domesticAnimal):
        Person.__init__(self, id, name)
        self.__groupNum = groupNum
        self.__domesticAnimal = domesticAnimal

    def set_groupNum(self, groupNum):
        self.__groupNum = groupNum

    def set_domesticAnimal(self, domesticAnimal):
        self.__domesticAnimal = domesticAnimal

    def get_groupNum(self):
        return self.__groupNum

    def get_domesticAnimal(self):
        return self.__domesticAnimal

    def __str__(self):
        pass
    
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
        pass

def main():
    pass

main()
