class Account:

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance

    def display(self):

        print("Account Holder:", self.name)
        print("Balance:", self.balance)


class SavingAccount(Account):

    def interest(self, rate):

        result = self.balance * rate / 100

        print("Interest:", result)


obj = SavingAccount("Sam", 10000)

obj.display()

obj.interest(5)