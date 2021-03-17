# def factorial(n=1):
#     if n ==1:
#         return 1
    
#     return n * factorial(n-1)

# print(factorial(3))

# a = 10

# def func():
#     global a
#     a+=1
#     print( 'a in function',a)
    
# func()
# print('a outside function',a)


def func():
    def add(a,b):
        return a+b
    
    return add
c = func()

print(c(3,5))

def pow(func):
    def result(b):
        return b**func
    return result

x =pow(func()(1,1))
print(x(12))