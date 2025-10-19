class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price' : price, 'quantity' : quantity}
        self.cart.append(product)

    def remove_item(self, item_name):
        for item in self.cart:
            if item['item'] == item_name:
                self.cart.remove(item)
            else:
                print(f'This item not available in your cart')
                break
    
    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print('Total price', total)
        if amount < total:
            print(f'Please provide {total - amount} more') 
        else:
            extra = amount - total
            print(f'Here is your items and extra money {extra}')

jamshed = Shopping('Jamshed')
jamshed.add_to_cart('Head Phone', 1500, 1)
jamshed.add_to_cart('Watch', 1400, 1)
jamshed.add_to_cart('Pant', 1200, 2)

print(jamshed.cart)
jamshed.checkout(6000)

jamshed.remove_item('Pant')
print(jamshed.cart)