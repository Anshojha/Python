class BankAccount:
    def __init__(self):
        self.balance =0

    def withdraw(self  , amount ):
        self.balance -= amount
        return self.balance
    def deposit(self , amount ):
        self.balance += amount
        return self.balance
    
a = BankAccount()
b = BankAccount()

a.deposit(100)
b.deposit(50)

print(a.withdraw(50))
print(b.withdraw(50))