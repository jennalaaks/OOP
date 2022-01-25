# Filename tehtava3.py
# Author: Jenna Laaksovirta
# Description: Tells grade by given points.

def main():
    user_input = int(input("Give points: "))

    if user_input >= 108 and user_input <= 120:
        print("Grade 5")

    elif user_input >= 96 and user_input < 108:
        print("Grade 4")

    elif user_input >= 84 and user_input < 96:
        print("Grade 3")

    elif user_input >= 72 and user_input < 84:
        print("Grade 2")

    elif user_input >= 60 and user_input < 72:
        print("Grade 1")

    elif user_input < 60 and user_input >= 0:
        print("Grade 0")

    else:
        print("Give number that is bigger than 0 and smaller than 120.")

main()