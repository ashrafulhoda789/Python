class Shopping:
    cart = [] # class attribute or static attribute
    origin = 'China'
    
    def __init__(self, name, location):
        self.name = name # Instance attribute
        self.location = location

    def purchase(self,item, price, amount):
        remaining = amount - price
        print(f'Buying: {item} for price: {price} and remaining {remaining}')
    
    @staticmethod
    def multiply(a, b): # In static method we don't need to use self. In static method we can't use instance
        result = a*b
        print(result)

    @classmethod
    def just_visit(self, item):
        print(f'Just for visiting')

bali_arcade = Shopping('Bali Arcade', 'Chawkbazar')
# bali_arcade.purchase('Shirt', 500, 1000)
# Shopping.purchase('a', 2, 3, 3) # Without classmethod if we want to access function we have to give self parameter also

bali_arcade.just_visit('shirt')
Shopping.just_visit('Shirt') # By using classmethod we can access directly using class without give self parameter

# static method
Shopping.multiply(4, 6)
# bali_arcade.multiply(6,9)