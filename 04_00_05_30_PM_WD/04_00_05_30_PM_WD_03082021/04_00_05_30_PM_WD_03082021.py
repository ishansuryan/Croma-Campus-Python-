# Program to find armstrong number
# n = 370

# l = list(str(n))
# sum = 0
# for i in l:
#     sum += int(i)**(len(l))

# if sum == n:
#     print('number is armstrong number')

# else:
#     print('number is not armstrong number')

# Tuples are non mutable lists 

tup = (1,2,3)

print(tup[2:0:-1])

tup = (1,2,2)

tup = ()
t1 = (10,)
print('Type of t1 is',type(t1)) 
   
l = list(range(9))
l1 = [0,1,2,3,4,5,6,7,8,9,10]
t_l = tuple(l1)

print(t_l)

s = 'Hello'
t_s = tuple(s)
print(t_s)
t_s_l = list(t_s)
print(t_s_l)

# Sets
l = [9,1,1,2,2,3,4,5,4,5,6,8,9,5,1,2,3,8]
ls = set(l)
print(ls)

l = {1,2,3,2,5,6,9,7,8,7,4,8}
print('id of l is', id(l))
l.add(10)
print('id of l is', id(l))
print('l is', l)

a = {1,2,3,4,5,6}
b = {5,6,7,8,9,10}
f = a.union((b))
a.symmetric_difference_update(b)
print('a is:', a)
print('a union b is:',f)
# d = a.intersection(b)
# print('d is',d)
# c = a.difference(b)
# print(c)
# a.difference_update(b)
# print('a is after difference_update',a)
# a.discard(1)
# print('a is after discard',a)

# d.pop()
# print(d)
tup = (1,2,3,4)
a,b,c,d = tup       # unpacking a tuple

tup = tup + (10,)
print(tup)