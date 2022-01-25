import random #import random

def generate_random_number():
    return random.randint(0,6) #valitse random numero ja palauta se

def main():
    print(f"Random number is: {generate_random_number()}") #tulosta numero

main()#kutsu ohjelmaa