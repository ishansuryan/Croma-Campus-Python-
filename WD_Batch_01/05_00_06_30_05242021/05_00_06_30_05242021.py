# python Numbers and variables

'''
Variable naming Conventions of python:
1. Variable name cannot start with number.
2. Variable name cannot have spaces
3. Numbers can come in or at the end of variable 
4. variable names can have _ 
'''
_a = 10
a_ = 1
a1 = 2
a_1 = 3
a = 0
__c__= .23          # Not preferable

a = '1'
print(type(a))

a = 1
print(type(a))

a = 1.0
print(type(a))

a = True
print(type(a))

a = complex(1)
print(type(a))

a = None
print(type(a))

# Statements in Python
a = 10+3*1/2*20-2**3
print(a)

# a = a+1             # a+=1
a -= 1          # a = a-1
print(a)

# decision making in python

# if statements:
# Syntax :-> if condition:
a = 200

if a>20:
    print('a is grater than 20')
    print('Empty line 51')

elif a == 20:
    print('a is 20')

else:
    print('a is smaller than 20')

# Rules for if elif and else:
'''
1. There must be if statement before elif oer else
2. there must be atleast  1 if or elif statement brfore else
3. else will always be last statemnt ia decision block
4. there can be n numbers of if statement in a program
'''
# Write a program to take input from user of diagonal poits 
#and check wether the shape is square or rectangke.]

x1 = int(input('Enter Point1 x value'))
y1 = int(input('Enter Point1 y value'))

x2 = input('Enter Point2 x value')
y2 = input('Enter Point2 y value')

print(type(x1),type(y1),type(x2),type(y2))

if int(x2)-x1 == int(y2)-y1:
    print('It is a square')

else:
    print('it is not a square')