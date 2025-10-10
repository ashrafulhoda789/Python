# in, not, not in, is, is not
# and, or

a = 3

if a > 4:
    print('Greater')
elif a == 2:
    print('Equal to Two')
else:
    print('Smaller')


boss = True
coin = 'Head'

if boss is not True:
    print('This is Boss')
    if coin == 'Tail':
        print('Bowling')
    else:
        print('Batting')
else:
    print('Not boss')
    if 8%2 == 0 and 5%2 == 0:
        print('All are even number')
    else:
        print("odd number")
        if 5%2 == 0 or 7%2 != 0:
            print('One or both are odd number')

