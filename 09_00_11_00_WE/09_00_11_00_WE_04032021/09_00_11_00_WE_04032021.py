standard_input = [1,20,5,10,3,12]

def addition():
    a = int(input(" Enter number1: "))
    b = int(input(" Enter number2: "))
    print('the sum is: ', a+b)

def addition_(a,b=0):
    print('* the sum is: ', a+b)

def addition_r(a,b):
    return a+b

def addition_1():
    a = int(input(" Enter number1: "))
    b = int(input(" Enter number2: "))
    return a+b


addition_(10)
addition()
result = addition_r(50,-60)
print('The sum is:',result)
r = addition_1()
print(r)