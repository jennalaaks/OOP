# Filename      tehtava5.py
# Author:       Jenna Laaksovirta
# Description:  User need know capital city 10 times.

import random

countries = {}

with open('country.txt') as file:
    for line in file:
        (key, value) = line.split()
        countries[key] = value

points = 0

for i in range(10):
    country = random.choice(list(countries))
    user_input = input(f'The capitalcity of the {country}: ')
    
    if user_input == countries[country]:
        print('Right!')
        points += 1
    else:
        print(f'Wrong! Right answer is {countries[country]}.')

print(f'Your points {points}/10.')