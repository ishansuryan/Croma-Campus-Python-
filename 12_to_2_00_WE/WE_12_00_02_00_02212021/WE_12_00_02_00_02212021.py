s = 'hello how are you'
# print('The index of value is',s.find('z'))
# print(s.index('z'))

# for i in range(1,11):
#     # print("the number is:",i,'the sqaure is:',i**2,'the cube is:',i**3)
#     print("the number is:{} the sqaure is:{} the cube is:{}".format(i,i**2,i**3))

# print(s.isalnum())

# print('hello'.isalpha())
# print('1234567890'.isdecimal())
# print('1.2'.isdigit())
print('r'.isidentifier())
print('wa'.islower())
print('12'.isnumeric())
print('c:\\new folder'.isprintable())
new_s = s.split()
print(type(new_s))
print('\\'.join(new_s))
print("hello".rjust(10,'+'))
print('     5454      '.lstrip())
print(s.partition('z'))
print(s.replace('o','z'))
print(s.rsplit(' '))
print("hi".zfill(5))