# function decorators
def smart_devide(func):
    def inner(a,b):
        if b == 0:
            print('Devision by zero is not defined')
            return
        else:
            return func(a,b)
    
    return inner    
print()

@smart_devide
def devide (a,b):
    return a/b

# devide = smart_devide(devide)           #(10,0)

devide(10,0)


# Function Closures


def pow(x):
    def inner(y):
        print(y**x)
    
    return inner

x = pow(2)              # x= inner
x(3)
x(66)

y = pow(3)
y(4)