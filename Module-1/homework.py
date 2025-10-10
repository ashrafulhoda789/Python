# 1.
# a = int(input('First number: '))
# b = int(input('Second number: '))
# c = int(input('Third number: '))

# if a > b and a > c:
#     print(a, 'is maximum')
# elif b > a and b > c:
#     print(b, 'is maximum')
# else:
#     print(c, 'is maximum')

# 2.

# a = int(input('First number: '))
# b = int(input('Second number: '))
# c = int(input('Third number: '))

# sum = a + b + c
# print('Sum:', sum)

# 3.

# for i in range(39,68):
#     if i%2 == 1:
#         print(i)

# 4.

marks = float(input('Enter your mark: '))

if marks >= 80 and marks <= 100:
    print('A+')
elif marks >= 70 and marks < 80:
    print('A')
elif marks >= 60 and marks < 70:
    print('A-')
elif marks >= 50 and marks < 60:
    print('B')
elif marks >= 40 and marks < 50:
    print('C')
elif marks >= 33 and marks < 40:
    print('D')
else:
    print('F')