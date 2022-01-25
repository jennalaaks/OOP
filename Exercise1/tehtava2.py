#Luodaan lista
num_list = []

#Luodaan for-toistolause jossa kysytään käyttäjältä numeroa 10 kertaa
for i in range(0, 10):
    user_input = int(input("Enter number: "))
    num_list.append(user_input) #Lisätään käyttäjän syöte listaan

print(*num_list, sep=', ')

string_list = []

for i in range(0, 10):
    user_input = input("Enter something: ")
    string_list.append(user_input)

print(', '.join(string_list))