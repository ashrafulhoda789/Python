class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print(f'Rice, Meat, Biriani')

    def exercise(self):
        raise NotImplementedError


class Cricketer(Person):
    def __init__(self, name, age, height, weight,team):
        self.team = team
        super().__init__(name, age, height, weight)
    # Override
    def eat(self):
        print('Vegetables')

    def exercise(self):
        print(f'You need to do exercise')
    
    # +  operator overload
    def __add__(self, other):
        return self.age + other.age
    
    # *  operator overload
    def __mul__(self, other):
        return self.age * other.age
    
    # len  operator overload
    def __len__(self):
        return self.height
    
    # >  operator overload
    def __gt__(self, other):
        return self.age > other.age

jamshed = Cricketer('Jamshed', 23, 168, 52, 'BD')
mir = Cricketer('Mir', 12, 150, 47, 'BD')
# jamshed.eat()
# jamshed.exercise()

print(jamshed + mir)
print(jamshed * mir)
print(len(jamshed))
print(jamshed > mir)