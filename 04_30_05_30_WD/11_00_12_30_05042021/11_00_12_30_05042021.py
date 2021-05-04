l = [1,2,3,5,6,8,8,'Hello',10.2,[3,5,7,9,[11,13,15]], True, False]
print(type(l))

print(l[1::2])

s_ = 'Hello world'
l1 = list(s_)
print(l1)
s = s_
# mutable immutable
print('id of s before change',id(s))
s='t'
print('id of s after change',id(s))
print('S_:',s_)
a = l

print('id of l is',id(l))
print('id of a is',id(a))

a[1] = 100
print('id of after change',id(a))

print(l)

print('Line no.25:',l[9][4][0])

for i in l:
    print(i)

ls = [1,2,3,4,5,6,7,8,9,10]
sum_ = 0
for i in ls:
    sum_+=i

print(sum_)

print(sum(ls))
