num_list = [2, -5, 4, 7, 9, 11, 0, 445, -100, 4, 1, 10]

#Järjestetään lista
sorted(num_list)
#Tallennetaan järjestetty lista
num_list = sorted(num_list)

#Tulostetaan numerot pilkuilla eroteltuna
print(*num_list, sep=', ')