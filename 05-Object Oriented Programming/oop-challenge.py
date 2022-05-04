# Create a Bank Account class with attributes owner and balance, and methods deposit and withdraw
## Withdrawals may not exceed the available balance

class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return "We just deposited {} into your account".format(amount)

    def withdrawal(self,amount):
        if amount >= self.balance:
            return "You can't take that much out!"
        else:
            self.balance = self.balance - amount 
            return "You've taken {} dollars out of your account".format(amount)

my_account = BankAccount("rebecca", 600)

print(my_account.owner,my_account.balance)

print(my_account.deposit(100))

print(my_account.balance)

print(my_account.withdrawal(300))

print(my_account.balance)
