# function inside a function

def outer():
    print('Outer function called')
    # global inner
    def inner():
        print('Inner function called')
    return inner

print(outer)
x=outer()    
x()   

def pow(a):
    def inner(b):
        print(b**a)
    return inner

z = pow(3)
print(z)
z(2)                # function closure
z(3)
z(4)
z(5)
# Wa function to take input of pwer and input of number whose value need to be calculated
standard_input= [3,2]

a = int(input('Enter a power number'))
b = int(input('Wnter number whose power value you need to find'))

def power(a):
    def inner(b):
        print(b**a)
    return inner

d = power(a)
d(b)

# function Decorators : enhancing the functionality of function without changng it
def smart_devide(func):
    def inner(a,b):
        if b ==0:
            return 'Devision by zero is not possible'
        return func(a,b)
    return inner

@smart_devide
def devide(a,b):
    return a/b


# function decorated
# devide = smart_devide(devide)     # @smart_devide is equal to this line

x = devide(2,0)
print(x)

# Wap to define a function which takes 2 numbers and displays their sum and 
# wirte a decorator for the same to negate wrong input values
