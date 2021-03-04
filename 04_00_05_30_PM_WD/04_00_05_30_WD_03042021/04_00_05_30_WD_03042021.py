# WAP to find the factorial of a number of

# n = 5
# factorial = 1

# for i in range(1,n+1):
#     factorial *= i 

# print(factorial)

# WAP to print fibanachi number upto given number

# fib = [0,1]
# n = 9
# risult = 0
# if n == 0:
#     print('fibonachi number is '. fib[0])

# elif n == 1:
#     print('fibonachi number is '. fib[1])

# else:
#     for i in range(n+1):
#         risult = fib[i-2] + fib[i-1]
#         if i>1:
#             fib.append(risult)

# print('fibonachi of {} is'.format(n),fib[-1])


# Dictionaries

a = {1:1,2:{0.0:4},3:9,2:10}
b=a
print(a)
print(b[2])
b[2]= 5
print(a)

d={}
e =dict()
print(type(d))
print(type(e))

print(a.keys())
print(a.values())
print(a.items())

l = [(1,(1,2,0)),(2,4),(3,9)]
f =dict(l)
print('f is',f)
print(a.get(9))
print(a[9])
