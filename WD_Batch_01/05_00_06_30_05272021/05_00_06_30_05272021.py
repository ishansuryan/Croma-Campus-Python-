# pattern number 1:
from typing import Pattern


print('pattern no.1')

for row in range(0,5):
    for column in range(row+1):
        print('*',end = '')
    print()

# Pattern NO.3
print('pattern no.3')

for row in range(0,5):
    for column in range(5-row):
        print('*',end = '')
    print()

#  Pattern NO. 2
print('pattern no.2')

for row in range(5):
    for space in range(5-row-1):
        print(' ', end = '')
    
    for star in range(row+1):
        print('*', end = '')

    print()