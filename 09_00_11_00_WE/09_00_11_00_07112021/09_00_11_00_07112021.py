# Modules
import random

# otp generator program using radom module

# otp = random.randint(1000,9999)
# print(otp)
# l = [x for x in range(1,100)]
# random.seed(35)
# random.shuffle(l)
# print(l)

# time module

import time

print(time.time())

start = time.time()
x= 50000**0.5 
print('time taken is', time.time()-start)

dt = time.strftime('%a %b-%d-%Y %I:%M:%S %P')
print(dt)

from datetime import datetime
s = 'Sun Jul-11-2021 10:32:50 am'

x = datetime.strptime(s,'%a %b-%d-%Y %I:%M:%S %p')
print(type(x), x.month)

import os
# print(os.getcwd())

print(time.timezone)

# file handling

# file = open('Test file.txt','w')
# file.write('Hello how are you?\n')
# file.write("Hello world")
# file.close()

# f_read = open('Test file.txt', 'r')
# r = f_read.readlines()
# print(r)
# f_read.seek(0)
# print()
# print('line is: ',f_read.readline())
# print(f_read.readline())

csv = open('name_marks.csv','w')
name =  ['Ram', 'Shyam', 'Mohan', 'Dilip']
marks = [75,89,52,33]
for i in range(len(name)):
    print(f'{name[i]},{marks[i]}',file = csv, flush = True)
csv.close() 


name[i] + ',' + str(marks[i]) + '\n'