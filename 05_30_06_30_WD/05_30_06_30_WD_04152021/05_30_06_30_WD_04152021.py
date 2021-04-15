# # functions
# standard_input = [10,20,30,15]
# def addition():
#     a = int(input('Enter Number 1:'))
#     b = int(input('Enter Number 2:'))
#     print('The sum is:', a+b)
    
# addition()
# # addition()

# def subtract(a,b):
#     print('The Difference is:', a-b)
    
# subtract(9,5)

# def multiply(a,b):
#     return a*b

# x = multiply(2,30)
# print('The multiplication is',x)

# def devide():
#     a = int (input('Enter the number1: '))
#     b = int (input('Enter the number2: '))
#     return a/b

# z = devide()
# print('the devision is:',z)
    
# def outer():
#     print('Outer called hence inner is now defined')
    
#     def inner():
#         print('Inner defined after outer called')
#     inner()


# outer() 

# a = 10

# def number():
#     global a
#     # a = 20
#     print('inside function',a)   

# number()
# print('Outside function',a)

def palindrome(a):
    if len(a) == 1 or len(a) == 0:
        return True
    
    if a[0] == a[-1]:
        palindrome(a[1:-1])
        
x = palindrome('nitin')
print(x)
