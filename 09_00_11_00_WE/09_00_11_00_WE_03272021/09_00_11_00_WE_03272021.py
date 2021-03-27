# Continue Statement
for i in range(1,11):
    if i%2 == 0:
        # continue
        pass
        
    
    else: print(i) 

from math import *
print(pi)

# from calendar import calendar
# print(calendar(2022))

import datetime
string = '28 June 2020'
print(datetime.datetime.now())
print(datetime.datetime.now().strftime('%A %d-%b-%y %I-%M-%S %p'))
date = datetime.datetime.strptime(string ,'%d %B %Y')

print(type(date))
import time

print(time.time())

