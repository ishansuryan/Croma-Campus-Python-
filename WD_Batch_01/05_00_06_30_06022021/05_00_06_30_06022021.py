a = []
# a[0] = 32
print(type(a), a)
a.append(32)
print(a)

b = [32]
print(b)

c = [3, 10, 'HI']
a.append(c)
b.extend(c)
print('a is', a, f'length of a is {len(a)}')
print('b is', b, f'length of b is {len(b)}')
print(a[1])

l = [1, 2, [3, [4, 5, [6, 7, 8, [9, 10]]]]]
print('length of l is', len(l))
print(l[2][1][2][3][1])
# print(l[::-1])

a = [1, 2, 3, 4, 5, 1, 1, 1, 2, 3, 23, 3, 3, 3, 3, 3, 3, 3]
b = a.copy()
b[1] = 30
print(a.count(3))
print(b)
print(a.index(3, 5))
a.insert(5, 'Ten')
print(a)

z = a.pop(5)
print(z)
print(a)
a.remove(23)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
'''
Write a Python program to count the number of strings where the string length is 2 or more 
and the first and last character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']'''
