# Filename tehtava5.py
# Author: Jenna Laaksovirta
# Description: Calculate average of students grades.

def calc_average(students):
    values = students.values()
    average = sum(values) / len(students)
    return average

def main():
    # Greate dictionary list
    students = {}

    # For loop where ask user input
    for i in range(0, 5):
        student_name = input("Student name: ")

        grade = int(input("Student grade: "))

        students[student_name] = grade

    print('Students average: ', calc_average(students))

main()