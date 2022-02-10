# Filename      tehtava4.py
# Author:       Jenna Laaksovirta
# Description:  The user enters the phone information into the object and then the information is printed.

import cellphoneFile

def main():
    phone = cellphoneFile.Cellphone()
    
    phone.set_manufact(input('Enter the cellpone manufact: '))
    phone.set_model(input('Enter the cellpone model: '))
    phone.set_retail_price(input('Enter the cellpone retail price: '))
    print("")
    print('Here is the data that you provided:')
    print(f'Manufacturer: {phone.get_manufact()}')
    print(f'Model number: {phone.get_model()}')
    print(f'Retail price: {phone.get_retail_price()}')

main()