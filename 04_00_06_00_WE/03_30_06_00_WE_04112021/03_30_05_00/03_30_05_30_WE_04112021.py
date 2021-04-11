# Strings

# a  = 'Hello'
# print(type(a))


# String Indexing and slicing
# s = 'How are you?'
# #    0123456789

# print(s[2])
# print(s[-1])
# print(s[0:3])
# print(s[4:7])
# print(s[0:-1:2])
# print(s[-3:])
# print(s[-3:-10:-1])
# print(s[::-1])      # reversing ideom

# for i in range(1,11):
#     # print('The number is {2:<2} the sqaure is {0:>3} the cube is {1:^5}'.format(i**2,i**3,i))
#     print(f'The number is {i:2} the sqaure is {i**2:3} the cube is {i**3:4}') 
    
# print('the value of pi is_{:10.9f}'.format(22/7))

s = 'hELLO How ArE yOu?'

print(s.capitalize())   
print(s.casefold())
print(s.lower())
print(s.upper().center(30,'-'))
print(s.lower().count('h'))
print(s.endswith('yOu?'))
print(s.lower().find('o0'))
print(s.lower().index('o'))