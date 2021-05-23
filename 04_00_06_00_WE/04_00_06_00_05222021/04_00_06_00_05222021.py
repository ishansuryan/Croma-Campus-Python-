# random module

import random
# print(help(random))
# otp = random.randint(100000,999999)
# print(otp)

s = 'hello world'
print(random.choice(s))


l = [1,2,3,4,5,6,7,8,9]
random.shuffle(l)
print(l)

# Functions
standard_input = [10,30,1,2,3,4,5,6,7,89,]
# def add():
#     a = int(input('Enter a Number'))
#     b = int(input('Enter a Number'))
#     print('The sum is:',a+b)


def add(a,b):
    print('The sum is:',a-b)
add(1,2)
z = add(2,1)
print('Line No 28:->',z)
# add()
print('this is after function call 3 times')
# add()

# returning a value from a function

def multiply(a,b):
    return a*b
    print('after return')

result = multiply(2,6)
print(result)