# read only --> you can't set the value and can not be changed.
# getter --> Get a value of a property through a method. Most of the time, you will get the value of a private attribute.
# setter --> Set a value of property through a method. Most of the time, you will set the value of a private attribute.

class User:
    def __init__(self, name, age, money):
        self._name = name
        self._age = age
        self.__money = money

    # getter without any setter is readonly attribute
    @property
    def age(self):
        return self._age
    # getter
    @property
    def salary(self):
        return self.__money
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            return 'Salary can not be negative'
        self.__money += value

jamshed = User('Jamshu', 21, 12000)
# print(jamshed.__money)
# print(jamshed.age())
print(jamshed.age)
print(jamshed.salary)
jamshed.salary = 4500
print(jamshed.salary)