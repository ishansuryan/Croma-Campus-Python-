# string formatting

for i in range(1,11):
    # print('the number is {2:<3} the sqaure is {0:>3} the cube is {1:^5}'.format(i**2,i**3,i))
    print(f'the number is {i:<3} the sqaure is {i**2:>3} the cube is {i**3:^5}')
b = 22/7
print('The value of pi is {:10.51f}'.format(b))

print(r'c:\new folder\tables')