# list --> []
# tuple --> ()
# set --> {}

# set : unique items collection. No duplicate

numbers = [12, 56, 98, 78, 56, 12, 6, 98]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(55)
print(numbers_set)

# numbers_set[1] = 5 # not possible

for item in numbers_set:
    print(item)

if 9 in numbers_set:
    print('9 Exist')
elif 98 in numbers_set:
    print('98 Exist')

A = {1, 3, 5}
B = {1, 2, 3, 4, 5}
print(A & B) # intersection (A n B)
print(A | B) # union (A U B)