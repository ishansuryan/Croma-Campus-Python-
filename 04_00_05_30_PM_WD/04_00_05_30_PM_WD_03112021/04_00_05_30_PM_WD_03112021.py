# a = 2
# try :
#     b= int('a')
    
# except ValueError:
#     print('cannot convert string to intiger')
    
# b = 0
# try:
#     print(a/b)
#     b = int('s')

# except (ZeroDivisionError,ValueError):
#     print('devision by zero is not defines')
    
# except(TypeError):
#     print("value must be an integer or float")

# import numpy as np
# print(tuple(np.__version__.split('.')))

# assert tuple(np.__version__.split('.')) >= ('1','19','5'), 'numpy version is lower than required'
# print('numpy is above required version')

import sys,os
# print('\nthe argv command:\n',sys.argv[0])
# print(sys.path)
# print(sys.modules)
# print(sys.version)
# print('\nThe current working directory is:\n',os.getcwd())


# import math as ma

# print(ma.cos(90))

# from math import *

# print(tan(90))

import random
s = 'hello'
print(random.choices(s,k=5))
# random.seed(10)
otp = random.randint(100000,999999)
print(otp)
x = list(s)
random.shuffle(x)
print(random.randrange(100000,999999))
print(x)
print(random.random())