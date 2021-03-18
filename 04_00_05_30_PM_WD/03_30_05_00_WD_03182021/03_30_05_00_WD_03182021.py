# Decorators



# x = devide(10,0)

def dec_devide(func):
    def inner(a,b):
        if b == 0:
            print('devision by zero is not defined')
            return 
        return func(a,b)
    return inner

@dec_devide
def devide(a,b):
    return a/b


# devide = dec_devide(devide)     # devide = inner
x = devide(10,0)