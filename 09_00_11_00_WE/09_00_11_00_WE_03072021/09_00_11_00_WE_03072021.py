# a = []
# print(type(a))

# b =list()
# print(type(b))
# d = range(9)
# print(type(d))
c = list(range(9))
# print(type(c))

# e= [range(9)]
# print(e)
# print(c[-1:-5:-1])

# print('id of c is: ',id(c))
# b=c
# print('id ob b is: ', id(b))
# b[1] = 10
# print('b is',b)
# print('id ob b is: ', id(b))
# print('c is',c)

# s1 = 'Hello'
# print('id of s1 is: ',id(s1))
# s2 = s1
# print('id of s2 is: ',id(s2))
# s2 = 'hello'
# print('id of s2 is: ',id(s2))
# print(s1)
# s2 = '1'

# l = [10,20, [[15,30],40]]
# print(l[2][0][1],l[2][1])

# l_append = []
# l_extend = []
# l1 = [1,2,3,4,5,6,1,1,1,2,5,3,6,6,6,6,6,6,]
# l_append.append(l1)
# l_append.append('Hello')
# print('l_append is:', l_append)
# l_extend.extend(l1)
# l_extend.extend('Hello')
# print('l_extend is:', l_extend)
# d = c.copy()  
# e = c[:]
# print('id of c is:',id(c))
# print('id of d is:',id(d))
# print('id of e is:',id(e))
# print(l1.count(6))
# print(f'index of {1} is:', l1.index(1,2,7))
# l1.insert(0,10)
# print(l1)
# l1.pop(10)
# x=l1.remove(10)
# print(x,l1)

# l2 = [6,7,5,4,3,2,1]

# risult = 1

# for i in l2:
#     risult*= i

# print(risult)

# risult = 0

# for i in l2:
#     risult+= i

# print(risult)

l = ['abc', 'xyz', 'aba', '1221']
n = 0
for i in l:
    if len(i)>2 and i[0] == i[-1]:
        n+= 1

print(n)