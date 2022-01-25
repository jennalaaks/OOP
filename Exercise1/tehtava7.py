def main():
    num = 2
    maximum_value = int(input("Give maximum value: ")) #Käyttäjä antaa maksimiarvon
    return maximum_value

def procession(max):
    num = 3
    taul = []
    while num <= max:
        taul.append(num) #Lisätään numerot taulukkoon
        print(num)
        num += 3 #Lisätään kolme muuttujaan num

    return taul #Palautetaan taulukko myöhempää käyttöä varten

def number_of_terms(nums):
    print("Number of terms:", len(nums)) #Len laskee taulukon pituuden

def sum_of_terms(nums):
    print("Sum of terms: ",sum(nums)) #Sum summaa taulukon alkiot

def sum_of_squared_terms(nums):
    sum = 0
    for i in nums:
        sum += i**2 #Taulukon alkio potenssiin 2
    
    print("Sum of squared terms is:",sum)

maximum_value = main()
numbers = procession(maximum_value) #Tallennetaan maksimiarvo muuttujaan
number_of_terms(numbers)
sum_of_terms(numbers)
sum_of_squared_terms(numbers)
