import math

def timer(func):
    def inner(*args, **kwargs):
        print('time started')
        # print(func)
        func(*args, **kwargs)
        print('time end')
    return inner

# timer()()

@timer # easier way to decorate
def get_factorial(n):
    print('factorial starting')
    result = math.factorial(n)
    print(f'Factorial of {n} is: {result}')

get_factorial(5)
# timer(get_factorial)() # harder way to decorate