# Decorators



# x = devide(10,0)

# def dec_devide(func):
#     def inner(a,b):
#         if b == 0:
#             print('devision by zero is not defined')
#             return 
#         return func(a,b)
#     return inner

# @dec_devide
# def devide(a,b):
#     return a/b


# devide = dec_devide(devide)     # devide = inner
# x = devide(10,0)

# arguments and keyword arguments

def add(*args, **kwargs):
    print(type(args))
    s = 0
    for i in args:
        s +=i
    print(type(kwargs))
    print('  ',kwargs['a'])
    return s

print(add(1,2,3,4,5, a = 10,b =1,ccc=20))
# print(add(10,20, bvbgbgb=45))
