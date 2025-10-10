# def full_name(first, last):
#     name = f'Full name is : {first} {last}'
#     return name

# # Take parameters in order(serial wise)
# # name = full_name('Jam', 'Jammir')

# name = full_name(last = 'Jammir', first = 'Jam')
# print(name)

def famous_name(First, last, **addition):
    name = f'{First} {last} '
    # print(addition['title'])
    for key, value in addition.items():
        print(key,value)
    return name

name = famous_name(First = 'Ashraful', 
                   last = 'Hoda', Title = 'Jamshed', 
                   title2 = 'Rafu', addition= 'Alo',
                   last2 = 'Tabu')
print(name)

# Return multiple things from an array
# def a_lot(num1, num2):
#     sum = num1 + num2
#     mul = num1*num2
#     sub = num1 - num2
#     return sum, mul, sub
#     # return [sum, mul, sub] # Also return as a list

# all = a_lot(55, 21)
# print(all) 