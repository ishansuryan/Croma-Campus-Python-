# functions 

# def devide(a, b=1):
#     return a/b

# print("The devision is:", devide(2,4))

# name space 

a = 10
print('A before function call:',a)
def func():
    global a                            # making a variable global
    a = 20                              # a is local to function only when global a is not given
    print('A inside function:', a)

func()
print('A after functin call',a)

# function recursion

# def add(l):
#     if len(l) == 1:
#         return l[0]
#     return l[0]+add(l[1:])

# s = add([1,2,3,4,5,6,7,8,9])
# print(s)


# Wap to Check wetehr a given string is a palindrome or not function should return true or false

def palindrome(s):
    s = str(s)
    if len(s) == 1:
        return True
    elif s[0] == s[-1]:
        if len(s)==2:
            return True
        else:
            return palindrome((s[1:-1]))
    return False

print(palindrome(1221))

# Wap to find the factorial for given number

def factorial(n):
    if n == 1 or n ==0:
        return 1
    return n*factorial(n-1)

print(factorial(4))