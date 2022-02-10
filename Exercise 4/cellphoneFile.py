class Cellphone:
    def __init__(self):
        self.__manufact = ""
        self.__model = ""
        self.__retail_price = 0
        self.__id = 0

    def set_manufact(self, input):
        self.__manufact = input

    def set_model(self, input):
        self.__model = input

    def set_retail_price(self, input):
        self.__retail_price = input

    def set_id(self, userInput):
        while(True):
            if userInput <= 6 and userInput >= 1:
                self.__id = userInput
                break;
            else:
                    print('Enter phone id between 1-6.')
                    userInput = int(input('Enter the cellpone retail price: '))
    
    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model
    
    def get_retail_price(self):
        return self.__retail_price

    def get_id(self):
        return self.__id