# def sum(num1, num2, num3=0):
#     result = num1 + num2 + num3
#     return result

# res = sum(99, 11,5)
# print(res)

# args

def all_sum(num1, num2,*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum += num
    return sum

total = all_sum(45,56, 89, 11, 81, 5, 2, 77)
print(total)

# def do_a_lot(*args):
#     print(args)

