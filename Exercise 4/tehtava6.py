# Filename      tehtava6.py
# Author:       Jenna Laaksovirta
# Description:  The user enters the phone information into the object and then the information is printed.

import cellphoneFile

def main():

    phones = [cellphoneFile.Cellphone(), cellphoneFile.Cellphone(), cellphoneFile.Cellphone()]

    #for phone in phones:
    for index, phone in enumerate(phones, start=1):
        print(f'Enter {index}. phone information.')
        phone.set_manufact(input('Enter the cellpone manufact: '))
        phone.set_model(input('Enter the cellpone model: '))
        phone.set_retail_price(input('Enter the cellpone retail price: '))
        phone.set_id(int(input('Enter the cellpone id: ')))
        print('')

    for index, phone in enumerate(phones, start=1):
        print(f'Phone {index}. information: ')
        print(f'Manufacturer: {phone.get_manufact()}')
        print(f'Model number: {phone.get_model()}')
        print(f'Retail price: {phone.get_retail_price()}')
        print(f'Id: {phone.get_id()}')
        print('')

        
main()