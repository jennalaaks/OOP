def user_input(): #Kysytään käyttäjän syöte
    user_input = 1
    num_list = []

    while not (user_input == 0): #Kysytään käyttäjältä niin kauan syötettä, kunnes se on 0
        user_input = int(input("Enter numbers: "))
        num_list.append(user_input)

    return num_list

def neg_nums(lista): #Etsitään listasta negatiiviset numerot
    count = 0
    for i in lista:
        if i < 0:
            count += 1
    print(count)

def even_nums(lista): #Etsitään parilliset numerot
    count = 0
    for i in lista:
        if i % 3 == 0:
            count += 1

    print(count)

def sum_positive_nums(lista):
    count = 0
    for i in lista:
        if i >= 0:
            count += i

    print(f"Sum of positive integers divisible by three is: {count}")

list = user_input() #Tallennetaan lista muuttujaan, jotta listaa voidaan käyttää funktioissa.
neg_nums(list)
even_nums(list)
sum_positive_nums(list)
