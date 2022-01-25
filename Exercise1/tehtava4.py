def function():
    user_input = 1
    #Luodaan muuttuja
    neg_num = 0
    while not (user_input == 0): #Kysytään käyttäjältä niin kauan syötettä, kunnes se on 0
        user_input = int(input("Enter something nice: "))
        if user_input < 0: #Jos luku on alle 0, lisätään muuttujaan neg_num 1
            neg_num += 1 #Lisätään muuttujaan 1

    print(f"Number of negative integers is: {neg_num}") #Tulostetaan neg_num arvo
        
function()