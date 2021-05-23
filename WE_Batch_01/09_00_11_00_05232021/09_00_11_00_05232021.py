# lambda function :-> one lined un-named function

def el(x):
    return x[1]

l = [(1,2),(2,1),(3,0),(5,5),(6,7)]

from functools import reduce
# l.sort(key = el)
l.sort(key = lambda x: x[1])
print(l)


def convert(x):
    return float(x)**2

l = ['1','2','3','4']
print(l)
l = list(map(lambda x: int(x),l))
print(l)

l1 = list(filter(lambda x:int(x)%2 ==0, l))
print(l1)

l2 = reduce(lambda x,a: int(x)*int(a), l)
print(l2)

# list comprehension syntax [expression for variable in iterable]
l3 = [x**2 for x in range(10)]
print(l3)

import re
s = '''(902)-(449)-(4802)
1234567890'''
p = ('(\([\d]{3}\))-(\([\d]{3}\))')
x = re.search(p,s)
print(x)
print(x.groups())