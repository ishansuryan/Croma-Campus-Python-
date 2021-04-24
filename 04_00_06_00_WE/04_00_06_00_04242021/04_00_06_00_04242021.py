# s = 'Hello how are you?'
# #    0123456789
# print(s[4])

# print(s[6:9])

# print(s[::-1])


# conditional Execution of statements
# syntax of if else statement

# if condition: condition should return True or False

a = 1               # <,>,<=,>=,!=, ==

if a>1:
    print('a is grater than 0')
    print('Inside if')
    print(10)
    print(100000)

elif a<1:
    print('a is a negative number')
    
else :
    print('a is eqaul to 1')
    

print('Outside if')
a = 10
b = 1
c = 10

if a ==b ==c:
    print('all the numbers are equal')

elif a>=b:
    if a == b and b>c:
        print('a and b are equal and grater than c')
    
    elif a >=c : 
        if a ==c:
            print('a and c are equal and grater than b')
        
        else : print('a is gratest')
    
    else : print ('c is gratest')

elif b>=c :
    if b ==c :
        print('b and c are equal and grater than a')   
    
    elif b>c:
        print('B is gratest')
    
else : print('c is gratest') 

print(max(1,2,3,4,50,10,6,5,6,5,6,50,50))