class Account:
    'This class demonstrate data-hiding'
    def __init__(self,name,balance):
        self.__balance = balance
        self.name = name

    def get_bal_info(self):
        name = ['Ajay','Mukesh','Aaron','James']
        search = input('Enter name :')
        if search in name:
            return print (self.__balance)

        else:
            print('Please enter a valid User .....')

    def get_name_info(self):
        return print(self.name)

    def __str__(self):
        return f'This is Account object with name {self.name} and balance {self.__balance}'

a = Account('Mukesh',250000)
print(a)
a.get_name_info()
# a.get_bal_info()




