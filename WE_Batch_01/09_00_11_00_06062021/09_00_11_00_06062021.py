# s = 'c:\\newfolder\\tables\\books\sprinf_file'
# print(s)
# '''
# c:
# ewfolder    ables_ooks\spring_file

# \spring_file
# '''

# s= 'he siad the "He\'s gonna come today"'
# print(s)

# s = r'c:\newfolder\tables\books\sprinf_file'
# print(s)

# s = 'file path = c:\\new folder\\tables \n calculation is a\\b'
# print(s)

# string formatting and string replacement fields

for i in range(1,11):
    print('2 X i = 2*i'.format(i,2*i ))

print()

for i in range(1,11):
    print('2 X {0} = {0}'.format(i))#,2*i))


for i in range(1,11):
   print('the number is {1:<2} square is {2:>3} the cube is {0:^5}'.format(i**3,i,i**2,))


# decimal formatting with dtring formatting

pi = 22/7

print('{:.51f}'.format(pi))

for i in range(1,11):
    print(f'2 X {i} = {2*i}')
    
for i in range(1,11):
    print('2 X %d = %d'%(i,2*i))