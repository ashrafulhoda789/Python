class Phone:
    manufactured = 'China'

    # Constructor
    def __init__(self,owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, phone, sms):
        text = f'Sending to: {phone} {sms}'
        print(text)

my_phone = Phone('Lei Jun', 'Xiamoi', 30000)
print(my_phone.owner, my_phone.brand,my_phone.price)

her_phone = Phone('She', 'IPhone', 120000)
print(her_phone.owner,her_phone.brand,her_phone.price)

my_phone.send_sms('Xiaomi','I love you')
