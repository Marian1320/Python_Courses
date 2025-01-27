# Create a hierarchy of classes representing different types of bank accounts. Start
# with a base class called BankAccount. Then, create two subclasses,
# SavingsAccount and CheckingAccount. Each subclass should inherit from the
# BankAccount class.
# ● The BankAccount class should have the following attributes and methods:
# ○ Attributes: account_number, balance
# ○ Methods: __init__ (constructor), deposit, withdraw, and get_balance
# ● The SavingsAccount class should inherit from BankAccount and have an
# additional attribute interest_rate. Override the deposit method to add
# interest to the balance when a deposit is made.
# ● The CheckingAccount class should inherit from BankAccount and have an
# additional attribute overdraft_fee. Override the withdraw method to deduct
# the overdraft fee if a withdrawal causes the balance to go below zero.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            interest = amount * self.interest_rate
            self.balance += amount + interest
            print(f"Deposited {amount} with interest {interest}")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0, overdraft_fee=35):
        super().__init__(account_number, balance)
        self.overdraft_fee = overdraft_fee

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= (amount + self.overdraft_fee)
            print(f"Withdrawn {amount} with fee {self.overdraft_fee}")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}")


savings = SavingsAccount("1234", 1500, 0.04)
savings.deposit(500)
print(savings.get_balance())

checking = CheckingAccount("6789", 700, 25)
checking.withdraw(600)
print(checking.get_balance())
