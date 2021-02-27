''' Decision making in python.

Rules of if else statements:

Syantx: if condition(which risults in true or false):(colon is a must)
after colon conme to next line and have indentation Se eg Below:'''

if True:
    pass        # till this indentation is there we will remain inside is statement. And
                # indentation will remain same throughout the program. Generally idenatation 
                # is of 4 spaces or 1 tab.

elif True:      # if statement is necessary for elif. There can be n number of elif statements
    pass        # below if statement.

else:           # there is condition in else and we need either 1 if or elif statement
    pass        # before else statement.

' Logical operators <,>,<=,>=,!=, ==, and, or , not, in , not in, is, ' 
a = '15'
if type(a) is str:
    print("This is a string")

if '1' in a:
    print('The number 1 is inside string')

a,b,c = 100,10,10

# Method 1

if a==b==c :
    print('all thre  are equal')
            
elif a>b:
        if a>=c:
            if a == c:
                print("a and c are equal and gareer than b")
            else:
                print('a is the gratest number')
        else:
            print('c is the gartest number')
            
elif a==b:
    if a>c: print("a and b are equal and grater than c")

elif b>=c:
    if b == c:
        print('b and c are equal and grater than a')
    else:
        print('b is gratest')

else:
    print('c is gratest')
    
'''
   And          risult
a       b
0       1           0
1       0           0
1       1           1
0       0           0

    or 
    
1       0           1
0       1           1
1       1           1
0       0           0

'''
a = -1
# print(type(a))
if a:
    print('a is not empty')

else: print('a is empty')

a = []
# len(a) == 0
if not a:
    print('The element is empty')


a = 'strings'
print(a[True:])