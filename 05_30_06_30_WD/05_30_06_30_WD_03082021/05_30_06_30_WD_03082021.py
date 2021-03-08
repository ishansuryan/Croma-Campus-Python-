# string replacement fields

for i in range(1,11):
    print('the number is {1:<3} the square is {2:>3} the cube is {0:^2}'.format(i**3,i,i**2))
                                                                                # 0  1  2
for i in range(1,11):
    print(f'the number is {i} the square is {i**2} the cube is {i**3}')
pi = 22/7
print('the value of pi is*{:3.1f}'.format(pi))
