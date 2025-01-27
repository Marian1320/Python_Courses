# Create a Python class representing a basic calculator with methods for addition,
# subtraction, multiplication, and division.

class BasicCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


calculator = BasicCalculator()
print("Add", calculator.add(10, 5))
print("Sub", calculator.subtract(10, 5))
print("Mult", calculator.multiply(10, 5))
print("Div", calculator.divide(10, 5))
