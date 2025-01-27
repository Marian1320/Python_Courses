# Create a class called BankAccount to represent a basic bank account.
# The class should have the following attributes:
# 1. owner: The name of the account owner.
# 2. balance: The current balance of the account.
# Implement the following methods: 1. __init__(self, owner, balance):
# Initializes the BankAccount object with the owner's name and initial balance.
# Ensure that the balance is a non-negative integer.
# 2. get_balance(self): Returns the current balance of the account.
# 3. deposit(self, amount): Adds the specified amount to the account balance.
# Ensure that the amount is a positive integer.
# 4. withdraw(self, amount): Subtracts the specified amount from the account balance.
# Ensure that the amount is a positive integer and does not exceed the current balance.
# Additionally, use @property and @attribute.setter to encapsulate the balance attribute
# and enforce validation rules.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  # Uses the @balance.setter

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = value

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be a positive integer.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be a positive integer.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount



account1 = BankAccount("Mariana", 1500)

print(f"Owner: {account1.owner}, Balance: {account1.get_balance()}")

account1.deposit(700)
print(f"After deposit: {account1.get_balance()}")

account1.withdraw(300)
print(f"After withdrawal: {account1.get_balance()}")
