# Encapsulation --> hide details
# Access Modifier: public, private, protected

class Bank:
    def __init__(self, holder_name, initial_deposit):
        self.holder_name = holder_name # public attribute
        self._branch = 'banani 11' # protected. It can use in outside of the class
        self.__balance = initial_deposit # private

    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
        else:
            return f'Low balance'

jamshed = Bank('Jamshed', 8500)
jamshed.deposit(1000)
print(jamshed.get_balance())

# print(dir(jamshed))
print(jamshed._Bank__balance)