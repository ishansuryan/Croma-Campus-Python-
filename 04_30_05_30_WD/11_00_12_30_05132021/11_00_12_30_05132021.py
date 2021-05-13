# Modules
# import math as m
# print(m.sqrt(4))
# from math import sqrt,sin,pi,cos
# print(sqrt(4))

# from math import *

# print(sin(90*(180/pi)))
# print(sin(90*(pi/180)))
# help(sin)

import time

# print(time.time())
# help(time)

import datetime

t = datetime.datetime.now()
print(t)
print(t.strftime("%d/%B/%Y %I:%M:%S %p"))

s = '12-January-2021'

x = datetime.datetime.strptime( s, '%d-%B-%Y',)

print(type(x))
print(x)

import random
otp = random.randint(100000,999999)
print(otp)

otp = random.randrange(100000,1000000)
print('New otp', otp)

help('modules')