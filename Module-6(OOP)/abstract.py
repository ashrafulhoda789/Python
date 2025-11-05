from abc import ABC, abstractmethod # abc = Abstract base class

class Animal(ABC):
    @abstractmethod # enforce all derived class to have a eat method
    def eat(self):
        print('I need food')
    
    @abstractmethod
    def move(self):
        print('Moving')

class Monkey(Animal):
    def __init__(self,name):
        self.catagory = 'Monkey'
        self.name = name
        super().__init__()
    
    def eat(self):
        print('I am eating banana')
    def move(self):
        print(f'{self.name} moving')

lucky = Monkey('Lucky')
lucky.eat()
lucky.move()