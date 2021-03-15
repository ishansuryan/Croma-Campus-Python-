# functions
def standard_input():
    l = [10,2,5,-52,3]
    for i in l:
        yield i

# a = int(input("Enter Number 1:"))
# def add():
#     b = int(input("Enter Number 2:"))
#     print("The sum is:",a+b)

# add()
# print(a)
# add_1 = add()
# add_2 = add()


# def add_1(a,b):
#     print('The sum is:',a+b)
    
# print('line number 18:',add_1(10,-3))

# def add_2(a,b):
#     return a+b

# x = add_2(10,-9)

def calculator(a,b,choice):
    def add():
        print(a+b)
    
    def minus():
        print(a-b)              # a = minus

    def multiply():
        print(a*b)
    
    def devide():
        print(a/b)
    
    d = {1:add, 2:minus, 3: devide, 4:multiply}
    d[choice]()

def inputt():
    a = int(input("Enter the number1:"))
    b = int(input('Enter the number2:'))
    return a,b

num1,num2 = inputt()
def choi():
    choice = int(input("Enter 1 for addition\n2 for subtraction\n3 for devision\n4 for multiplication"))
    return choice

l = [1,2,3,4]

while True:
    choice = choi()
    if choice in l:
        calculator(num1,num2,choice)
        break
