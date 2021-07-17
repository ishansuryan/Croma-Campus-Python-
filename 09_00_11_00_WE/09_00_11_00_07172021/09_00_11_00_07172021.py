# # Error Handling
# a = 10              # risult of some other calculations
# b = 0               # risult of some other calculations

# try:
#     print(a/b)
# except:
#     print('Devision by zero is not defined.')

# Functions in python
# What is a function?
# A block of code which can be called n number of times to do a specific task. 
# Syntax: def name_of_function():       # def is a keyword 
# standard_input = [1,2,13,4,5,6,7,8,9]            # for arepl

# def add_2_num():
#     a = int(input('Enter a number '))
#     b = int(input('Enter a number '))
#     print(a+b)
    
# # How to call a function
# add_2_num()
# add_2_num()

# def add_without_return(a,b):                # a, b are positional arguments
#     print(a+b)

# def add_with_return(a,b):
#     return a+b

# add_without_return(2,1)
# var = add_with_return(10,3)
# print(var)

# name space 

# a = 10
# print('A before function',a)

# def some_func():
#     # global a
#     a = 20
#     print('a inside function', a)
    
# some_func()
# print('a after function call',a )

# decorators and passing a function to function

def smart_devide(func):
    def inner(a,b):
        if b == 0:
            print('Devision by zero is not possible')
            return
        return func(a,b)
    return inner

@smart_devide
def devision(a,b):
    print('The devision is:->',a/b)

# devision = smart_devide(devision)           # equivalent to saying devision = inner
devision(0,0.)

