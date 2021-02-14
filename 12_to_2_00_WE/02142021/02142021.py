a = 10
print('First type of a is:',  type(a))

a = 10.2
print('Second type of a is:',type(a))

a = '10.2'
print('third type of a is :', type(a))

a = complex(real = 1, imag = 6)
print(a, ' type of a is', type(a))

for i in range(1,11):
    print('number is: {:<3} square is: {:^4} cube is: {:>3}'.format(i,i**2,i**3,))
    #< for left justification, > for right justificstion, ^ for center justification

import math

pi = math.pi

print(f"{pi:.55f}")       

print('this is first string','This is second string')

print("this is third string")     