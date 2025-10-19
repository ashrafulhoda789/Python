def call():
    print('Calling someone I don\'t know')
    return 'call done'

class phone:
    price = 30000
    color = 'White'
    brand = 'Xiaomi'
    features = ['200MP Camera', 'Speaker', 'Hammer']

    def call(self):
        print('calling one person')
    def send_sms(self, phone, sms):
        text = f'sending sms to: {phone} and message: {sms}'
        return text


my_phone = phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(4152, 'Mumir, I missed to miss You')
print(result)

