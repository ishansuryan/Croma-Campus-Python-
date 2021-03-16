# (0°C × 9/5) + 32 = 32°F
# c = 37
# f = (c* (9/5)) + 32
# print(f)

# print(True and False)
# print(True and True)
# print(False and True)
# print( False and False)

# print(True   or False)
# print(True   or True)
# print(False  or True)
# print( False or False)

# print(not(True   or False))
# print(not(True   or True))
# print(not(False  or True))
# print(not(False  or False))

# s= 'hi'
# print('line no. 22','H' not in s)

# a = 10
# print( 10 is 10)
# print( a == 10)

# a = -0.1
# if  a:
#     print("Non zero number")

# else:
#     print('zero number')
    
# a = 1000
# b = 100
# c = 100

# if a == b == c:
#     print('all three numnbers are equal')

# elif a>=b:
    
#     if a==b and a>c:
#         print('a and b are equal and grater than c')
        
#     elif a==c:
#         print('a and c are eual and grater than b')
    
#     elif a>c:
#         print('a is gratest')
    
#     else :
#         print('c is gratest')

# elif b>=c:
#     if b==c:
#         print('b and c are qualand grater than a',)
#     else:
#         print('b is gratest')

# else:
#     print('c is gratest')    
    





# a = 1000
# b = 1
# c = 100

# if a == b == c:
#     print('all three numnbers are equal')

# elif a<=b:
    
#     if a==b and a<c:
#         print('a and b are equal and smaller than c')
        
#     elif a==c:
#         print('a and c are eual and smaller than b')
    
#     elif a<c:
#         print('a is smallest')
    
#     else :
#         print('c is smallest')

# elif b<=c:
#     if b==c:
#         print('b and c are equal and smaller than a',)
#     else:
#         print('b is smallest')

# else:
#     print('c is smallest') 
    
# Loops

# sytax of for loops:
# for variable in iterable/range:

# for i in range(1,11,2):
#     print(i)
# print()
# s = 'hello'
# for i in s:
#     print(i)

# print()

# for i in range(len(s)):
#     print(s[i])
# num = 19    
# for i in range(1,11):
#     print(f'{num} X {i} =',num*i)

for row in range(5):
    for col in range(row + 1):
        print(end = '*')
    print()

print()

for row in range(5):
    for col in range(5-row):
        print(end = '*')
    print()