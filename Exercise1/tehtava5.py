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
        if i % 2 == 0:
            count += 1

    print(count)

list = user_input() #Tallennetaan lista muuttujaan, jotta listaa voidaan käyttää funktioissa.
neg_nums(list)
even_nums(list)
