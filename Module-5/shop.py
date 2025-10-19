class Shop:
    cart = [] # class attribute
    def __init__(self, buyer):
        self.buyer = buyer
    
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