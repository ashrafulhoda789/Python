# Global variable
balance = 3000

def buy_thing(item, price):
    # local scope variable
    # You can access global variable without using global keyword
    # But if you want to modify global varable, you have to use the global keyword
    global balance
    print(f'Previous balance', balance)
    balance = balance - price
    print(f'Balance after buying {item}', balance)


buy_thing('Phone',2000)
print('Global balance after buy', balance)