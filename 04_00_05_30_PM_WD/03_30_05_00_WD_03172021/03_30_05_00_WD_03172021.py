import time
n = 10

def factorial(n=1):
    if n ==1:
        return 1
    
    return n * factorial(n-1)
start_time = time.time()
time.sleep(1)
print(factorial(n))
print('recursion time:',time.time()-start_time)


factorial = 1
start_time = time.time()
time.sleep(1)

for i in range(1,n+1):
    factorial *= i

print('for loop time: ',time.time()-start_time)
print(factorial)


# a = 10

# def func():
#     global a
#     a+=1
#     print( 'a in function',a)
    
# func()
# print('a outside function',a)


# def func():
#     def add(a,b):
#         return a+b
    
#     return add
# c = func()

# print(c(3,5))

# def pow(func):
#     def result(b):
#         return b**func
#     return result

# x =pow(func()(1,1))
# print(x(12))