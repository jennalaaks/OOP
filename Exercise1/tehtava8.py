import random

vaihtoehdot = ["kivi", "paperi", "sakset"]

computer_points = 0
user_points = 0

for i in range(0, 3):
    user = input("Valitse kivi, paperi tai sakset: ")
    computer = random.choice(vaihtoehdot)

    if ((computer == "sakset") and (user == "paperi") or 
    (computer == "kivi") and (user == "sakset") or
    (computer == "paperi") and (user == "kivi")):
        print(f"Vastustaja valitsi {computer}. Hävisit pelin")
        computer_points += 1
    if (computer == user):
        print(f"Vastustaja valitsi {computer}. Tasapeli!")
        computer_points += 1
        user_points += 1
    else:
        print(f"Vastustaja valitsi {computer}. Voitit pelin!")
        user_points += 1

print(f"Tietokone: {computer_points}. pistettä")
print(f"Sinä: {user_points}. pistettä")