def addition(a,b):
    print('The sum is',a+b)
    
addition(1,3) 

def minus(a,b):
    return a-b

r = minus(1,6)
print('The diffefence is',r)

addition(3,5)
print(addition(1,3))

print(minus(20,10))

from datetime import datetime

def dat_tim():
    var = datetime.now()
    var_ = var.strftime('%A %d-%B-%Y %H:%M:%S')
    return var_

print(dat_tim())

# global a
a = 10

def test():
    global a
    a = 20 
    print('From Inside the function',a)

print('Before and outside the function',a)

# test()

print('After and outside the function',a)

def daa(*a):
    print(sum(a))

daa(1,2,3,5,6)
daa(3,30,2)
daa(1,2,2,2,2,2,5,5,5,5,5,)