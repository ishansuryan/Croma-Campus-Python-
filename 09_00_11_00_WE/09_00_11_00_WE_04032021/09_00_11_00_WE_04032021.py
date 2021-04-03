# standard_input = [-1,20,5,10,3,12]

# def addition():
#     a = int(input(" Enter number1: "))
#     b = int(input(" Enter number2: "))
#     print('the sum is: ', a+b)

# def addition_(a,b=0):
#     print('* the sum is: ', a+b)

# def addition_r(a,b):
#     return a+b

# def addition_1():
#     a = int(input(" Enter number1: "))
#     b = int(input(" Enter number2: "))
#     return a+b


# addition_(10)
# addition()
# result = addition_r(50,-60)
# print('The sum is:',result)
# r = addition_1()
# print(r)
# standard_input = [-1,20,5,10,3,12]
# x =int(input())
# b = x if x >=0 else -10
# def sub(a,b):
#     print(a-b)

# sub(b,2) 

# c = 20
# print('c before function defination', c)
# def test():
#     global c
#     c = 10 
#     print('c inside function',c)
# print('c before function call', c)
# test()   
# print('c after finction call and global declaration',c)

# standard_input = [14,30,40,'y',1,10,-5]

# def addd(a,b):
#     return a+b

# def minus(a,b):
#     return(a-b)

# def multiply(a,b):
#     return a*b

# def devide(a,b):
#     return a/b

# def inpt():
#     a = int(input("Enter Number1: "))
#     b = int(input("Enter Number2: "))
#     return a,b

# def calculator():
#     choice = int(input("Enter choice for operation:\n1 for addidiotn\n2 for subtraction\n3 for multiplication\n4 for devision"))
#     d = {1:addd,2:minus,3:multiply,4:devide}
#     n1,n2 = inpt()
#     try:
#         return d[choice](n1,n2)
#     except KeyError:
#         print('Wrong input Do you want to try again "y/n"')
#         ch = input("Enter choice")
#         if ch.lower() == 'y':
#             return calculator()
#         else :
#             return 'OK function close'

# print(calculator())

def palindrome(l):
    
    if len(l) < 1:
        return True
    
    if l[0] == l[-1]:
        return palindrome(l[1:-1])
    
    else: 
        return False
    
    
    
    # else : return False
    
    return palindrome(l[1:-1])

print(palindrome('12321'))
s ='nitin'
print(s[1:-1])