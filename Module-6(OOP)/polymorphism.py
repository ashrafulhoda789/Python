# poly --> many(multiple)
# morph --> shape

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print('Animal making some sound')

class Goat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        # return super().make_sound()
        print('Ankara messi')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        # return super().make_sound()
        print('meow')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        # return super().make_sound()
        print('gheu gheu')

don = Cat('Tonto')
don.make_sound()

kallo = Dog('Kallo')
kallo.make_sound()

messi = Goat('Messi')
messi.make_sound()

penaldo = Goat('Penaldo')

animals = [don, kallo, messi, penaldo]

for animal in animals:
    animal.make_sound()