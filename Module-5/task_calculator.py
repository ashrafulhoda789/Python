class Calculator:
    brand = 'Casio ES100'

    def add(self, num1, num2):
        return f'Sum: {num1 + num2}'
    
    def deduct(self, num1, num2):
        return f'Deduction: {num1 - num2}'
    
    def multiply(self, num1, num2):
        return f'Multiply: {num1 * num2}'
    
    def divide(self, num1, num2):
        return f'Divide: {num1 // num2}'

calculator = Calculator()
print(calculator.add(98, 8))
print(calculator.deduct(98, 8))
print(calculator.multiply(98, 8))
print(calculator.divide(98, 8))