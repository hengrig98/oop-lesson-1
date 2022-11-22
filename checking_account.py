class CheckingAccount:

    def __init__(self, name) -> None:
        self.name = name
        self.__balance = 0
        

    def credit(self,amount):
        self.__balance += amount

    def debit(self, amount):
        self.__balance -= amount

    def get_balance(self):
        print(f'{self.name} has a balance of ${self.__balance}')

John_Account = CheckingAccount('John')


print(John_Account.__balance)
John_Account.credit(100)
John_Account.debit(20)
# John_Account.balance = 1000000
# print(John_Account.__balance)
John_Account.__balance = 10000
John_Account.get_balance()