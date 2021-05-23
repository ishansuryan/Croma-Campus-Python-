# Error Handling

# a = 10
# b = 2 #0

# try:
#     print(a/b)

# except ZeroDivisionError:
#     print('devision by zero is not possible')

# except TypeError:
#     print("B is none vlaue please enter a value in b")

# except:
#     print('last except')

# else:
#     print('only printed when try block executed')

# finally:
#     print('finally block executed')

# print('after error handled')


# Assertion an error:

# import numpy as np
# print(np.__version__)

# assert np.__version__ > '1.20.3', 'Please update your numpy to version 1.20.3 or higher'

# raising an error

# a = 10
# b = 0

# if b == 0:
#     raise ZeroDivisionError ('devision by zero not defined please check ypur value')

# else with a loop

# a = 1

# while a>-1:
#     print(a)
#     if a == 2:
#         break
#     a -=1  

# else:
#     print('loop ended normally')

# Modules in Python

# import math

# print(math.sin(90*math.pi/180))

# from math import sin,pi
# print(sin(90*pi/180))

from math import *
print(cos(90))

import time
print(time.time())

from datetime import datetime
print(datetime.now())