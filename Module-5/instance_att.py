class Shop:
    shopping_mall = 'Bali Arcade'

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)

mumir = Shop('Mumir')
mumir.add_to_cart('shoes')
mumir.add_to_cart('phone')

print(mumir.cart)

jamshed = Shop('Jamshed')
jamshed.add_to_cart('Watch')
jamshed.add_to_cart('Grapics Card')

print(jamshed.cart)