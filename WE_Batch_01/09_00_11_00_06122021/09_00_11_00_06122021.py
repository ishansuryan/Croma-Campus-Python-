# '''
# Variable  naming conventions
# Variable name can start with and alphabet or _
# variable name can have numbers inside or at the end only
# Variable name cannot have spaces in between
# Variable name cannot start with numbers
# '''
# a  = 10
# a1 = 10
# a_1 = 200
# # a 1 = 300       # not a VALID VARIABLE NAME
# # 1a = 30           # not valid variable name
# a_ = 20

# # Changing Variable Types
# print(type(a))
# a = str(a)
# print(type(a))
# a = float(a)
# print(type(a))
# a = '10.2'
# a = int(float(a))
# print(type(a))
# # a = complex(a)
# # print(type(a))

# # Decision Making Process or If else statements

# if type(a) is complex:
#     print('a is  a complex number')
#     print("this indent is to show that the print statement is inside if statement")
# # a= str(a)
# elif type(a) == str:
#     print('A is of sting type')
#     print('inside if statement')

# else:
#     print('none of above conditions were True')
#     print('hence the else statement is executed')

'''
Logical operators in Pyhton
>  :- Grater than
<  :- smaller than
>= :- grate rthan equal to
>= :- smaller than equal to
!= :- not equal to
is 
in
not in
'''

'''Wap to find largest of 3 numbers'''

a = 10
b = 1
c = 10

if a == b == c:
    print( 'A,b,c are equal')

else :
    if a >= b:
        if a == b:
            if a > c:
                print('A and b are equal and grater than C')
            
            else:
                print('C is gratest')
        
        elif a >= c:
            if a ==c :
                print('A and C are equal and grater than B')
            else:
                print(' A is gratest')
        
        else :
            print('C is gratest')
    
    elif b>=c:
        if b==c:
            print('B and C are equal and grater than A')
        
        elif b>c:
            print( 'B is gratest')
        
    else:
        print('C is gratest')            
    